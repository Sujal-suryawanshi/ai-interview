import asyncio
from typing import Dict, Any, Tuple, List
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

from utils.llm_call import get_response_from_llm, parse_json_response
from utils.prompts import next_question_generation, feedback_generation

# Thread pool for synchronous LLM calls
executor = ThreadPoolExecutor(max_workers=4)

class InterviewAnalysisError(Exception):
    """Custom exception for interview analysis errors"""
    pass

@lru_cache(maxsize=128)
def _cache_key(prompt: str) -> str:
    """Generate cache key for prompt (optional caching mechanism)"""
    return hash(prompt)

async def _make_llm_call_async(prompt: str, default_keys: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Make an asynchronous LLM call in a thread pool and ensure default fields exist.
    """
    default_keys = default_keys or {}
    try:
        loop = asyncio.get_event_loop()
        response_text = await loop.run_in_executor(executor, get_response_from_llm, prompt)
        response = parse_json_response(response_text)
    except Exception as e:
        print(f"LLM call failed: {e}")
        response = {}

    # Ensure all default keys exist
    for key, default_value in default_keys.items():
        response.setdefault(key, default_value)
    return response

async def get_next_question(
    previous_question: str, 
    candidate_response: str, 
    resume_highlights: str, 
    job_description: str
) -> str:
    """
    Generate the next interview question safely.
    """
    final_prompt = next_question_generation.format(
        previous_question=previous_question,
        candidate_response=candidate_response,
        resume_highlights=resume_highlights,
        job_description=job_description,
    )
    
    response = await _make_llm_call_async(
        final_prompt,
        default_keys={"next_question": "Could you elaborate on your key technical skills?"}
    )
    
    return response["next_question"]

async def get_feedback_of_candidate_response(
    question: str, 
    candidate_response: str, 
    job_description: str, 
    resume_highlights: str
) -> Dict[str, Any]:
    """
    Generate feedback safely for a candidate's response.
    """
    final_prompt = feedback_generation.format(
        question=question,
        candidate_response=candidate_response,
        job_description=job_description,
        resume_highlights=resume_highlights,
    )

    response = await _make_llm_call_async(
        final_prompt,
        default_keys={"feedback": "Could not generate feedback.", "score": 0}
    )

    # Validate score
    try:
        score = float(response.get("score", 0))
        if not (0 <= score <= 10):
            score = 0
    except (ValueError, TypeError):
        score = 0

    return {
        "feedback": response.get("feedback", "Could not generate feedback."),
        "score": score
    }

async def analyze_candidate_response_and_generate_new_question(
    question: str, 
    candidate_response: str, 
    job_description: str, 
    resume_highlights: str,
    timeout: float = 30.0
) -> Tuple[str, Dict[str, Any]]:
    """
    Analyze candidate response and generate next question concurrently with timeout.
    """
    try:
        feedback_task = get_feedback_of_candidate_response(
            question, candidate_response, job_description, resume_highlights
        )
        next_question_task = get_next_question(
            question, candidate_response, resume_highlights, job_description
        )

        feedback, next_question = await asyncio.wait_for(
            asyncio.gather(feedback_task, next_question_task),
            timeout=timeout
        )
        return next_question, feedback

    except asyncio.TimeoutError:
        print("Timeout: LLM calls took too long.")
        return "Could you summarize your key technical skills?", {
            "feedback": "Feedback could not be generated due to timeout.", 
            "score": 0
        }
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Could you summarize your key technical skills?", {
            "feedback": f"Feedback could not be generated: {e}", 
            "score": 0
        }

def calculate_overall_score(feedback_list):
    """Calculate average score and qualitative rating"""
    if not feedback_list:
        return 0.0, "N/A"

    total = sum(conv.get("Evaluation", 0) for conv in feedback_list)
    avg_score = total / len(feedback_list)

    if avg_score >= 8:
        rating = "Excellent"
    elif avg_score >= 6:
        rating = "Good"
    elif avg_score >= 4:
        rating = "Average"
    else:
        rating = "Poor"

    return avg_score, rating
