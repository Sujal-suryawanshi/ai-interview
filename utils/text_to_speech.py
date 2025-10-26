import asyncio
import edge_tts
import pygame
import tempfile
import os
import time


async def speak_edge_tts(text, voice="en-US-AriaNeural", rate="+0%", pitch="+0Hz"):
    """
    High-quality TTS using Microsoft Edge voices
    """
    try:
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            temp_path = tmp_file.name

        await communicate.save(temp_path)

        time.sleep(0.5)  # Ensure file write completes

        if os.path.exists(temp_path):
            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)

            pygame.mixer.quit()
            time.sleep(0.2)
            os.remove(temp_path)
        else:
            print(f"Edge-TTS Error: Temp file was not created.")
            print("Text:", text)

    except Exception as e:
        print(f"Edge-TTS Error: {e}")
        print("Text:", text)


def speak_text(text, voice="en-US-GuyNeural", rate="+0%", pitch="+0Hz"):
    """Synchronous wrapper for Edge-TTS"""
    asyncio.run(speak_edge_tts(text, voice, rate, pitch))