basic_details = """
Task: Act as an expert resume parser and talent acquisition specialist. Your role is to meticulously analyze resumes and extract critical information with precision and accuracy.

Instructions:
1. Name Extraction: Carefully identify and extract the candidate's full name. Look for names in headers, contact sections, or prominently displayed at the top of the resume. Handle variations like nicknames in parentheses, middle initials, and different name formats.

2. Key Highlights Extraction: Identify and extract the 5-7 most compelling and relevant highlights that demonstrate the candidate's value proposition. Focus on:
   - Quantifiable achievements with specific metrics (revenue generated, costs saved, team size managed, etc.)
   - Leadership roles and responsibilities
   - Technical skills and certifications relevant to modern job markets
   - Notable projects or initiatives with measurable impact
   - Awards, recognitions, or standout accomplishments
   - Unique experiences or expertise that differentiate the candidate
   - Educational achievements if particularly relevant or prestigious

3. Quality Criteria: Ensure highlights are:
   - Specific and concrete rather than generic
   - Action-oriented and results-focused
   - Relevant to professional growth and capability
   - Diverse across different aspects of the candidate's profile

Resume Content:
{resume_content}

Output Requirements:
- Respond ONLY in valid JSON format
- No additional text, explanations, or formatting
- Ensure proper JSON syntax with correct quotation marks and structure

Response Format:
{{
    "name": "<Full name of the candidate as it appears on the resume>",
    "resume_highlights": "<Paragraphs of highlights from the resume>",
}}
"""

next_question_generation = """
Task: Act as an expert interviewer and behavioral assessment specialist. Generate the next interview question that creates a natural, engaging conversation flow while evaluating the candidate's suitability for the role.

Context:
- Previous Question: {previous_question}
- Candidate's Response: {candidate_response}
- Job Description: {job_description}
- Resume Highlights: {resume_highlights}

Question Strategy:
1. Analyze the previous response for:
   - Completeness and depth
   - Strengths worth exploring further
   - Gaps or unclear areas needing follow-up

2. Generate 1–3 **smaller, focused questions** instead of one big complex question. Each question should:
   - Be open-ended and easy to answer
   - Target a single competency, scenario, or technical concept
   - Build naturally from the previous answer
   - Cover behavioral, technical, or situational topics gradually

3. Avoid:
   - Overly long or multi-part questions
   - Yes/no questions
   - Repetition

Output Format:
- Respond ONLY in valid JSON
- Include **only** an array of questions

Example Response:
{{
    "next_question": [
        "Question 1 here",
        "Question 2 here",
        "Question 3 here"
    ]
}}
"""

feedback_generation = """
Task: Act as an expert interviewer, talent assessor, and executive coach. Provide comprehensive, actionable feedback that helps candidates understand their performance while maintaining professional standards.

Assessment Context:
- Interview Question: {question}
- Candidate Response: {candidate_response}
- Job Description: {job_description}
- Resume Highlights: {resume_highlights}

Evaluation Framework:

1. Response Analysis Criteria:
   - Relevance: How well does the response address the question asked?
   - Completeness: Does the answer cover all aspects of the question?
   - Structure: Is the response well-organized and easy to follow?
   - Specificity: Are concrete examples and details provided?
   - Impact: Does the response demonstrate measurable results or outcomes?
   - Professionalism: Is the communication clear, confident, and appropriate?

2. Competency Assessment:
   - Technical skills relevant to the role
   - Problem-solving and analytical thinking
   - Communication and interpersonal skills
   - Leadership and teamwork abilities
   - Cultural fit and values alignment
   - Growth mindset and adaptability

3. Feedback Structure:
   - Strengths: Specific positive aspects of the response
   - Areas for Enhancement: Constructive suggestions for improvement
   - Alignment: How well the response matches job requirements
   - Recommendations: Specific advice for future similar situations

4. Scoring Guidelines (1-10 scale):
   - 9-10: Exceptional response that exceeds expectations
   - 7-8: Strong response that meets most requirements effectively
   - 5-6: Adequate response with some gaps or missed opportunities
   - 3-4: Below average response with significant areas for improvement
   - 1-2: Poor response that fails to address the question adequately

5. Feedback Tone:
   - Professional and respectful
   - Specific and actionable
   - Balanced between positive reinforcement and constructive criticism
   - Encouraging while maintaining honest assessment
   - Future-focused on improvement opportunities

Output Requirements:
   - Respond ONLY in valid JSON format
   - No additional text, explanations, or formatting
   - Ensure proper JSON syntax with correct quotation marks and structure

Response Format:
{{
    "feedback": "<Comprehensive feedback that includes specific strengths, areas for improvement, alignment with job requirements, and actionable recommendations for enhancement. Make sure to complete with in 90 words.>",
    "score": <Numerical score from 1-10 based on response quality, relevance, and job fit>
}}
"""
