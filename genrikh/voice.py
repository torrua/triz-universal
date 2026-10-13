"""
ElevenLabs Voice Interface for Genrikh.
Synthesizes spoken audio briefings of Genrikh's inventive solutions,
providing audio summaries for executives, clients, and on-the-go engineers.
"""

import os
import httpx
from typing import Optional
from pathlib import Path

DEFAULT_VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Rachel / natural clear voice

class ElevenLabsVoice:
    def __init__(self, api_key: Optional[str] = None, voice_id: str = DEFAULT_VOICE_ID):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = os.getenv("ELEVENLABS_VOICE_ID", voice_id)

    def is_available(self) -> bool:
        return bool(self.api_key)

    def generate_audio(self, text: str, output_path: str = "genrikh_briefing.mp3") -> Optional[str]:
        """
        Synthesize speech from Layer 1 text and save to mp3 file.
        Returns the output path if successful, None otherwise.
        """
        if not self.is_available():
            return None

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }
        # Strip markdown syntax for cleaner speech
        clean_text = text.replace("#", "").replace("*", "").replace("`", "").strip()

        payload = {
            "text": clean_text[:2500], # safe length for briefing
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        try:
            with httpx.Client(timeout=30.0) as client:
                resp = client.post(url, json=payload, headers=headers)
                resp.raise_for_status()
                Path(output_path).write_bytes(resp.content)
                return output_path
        except Exception as e:
            return None
