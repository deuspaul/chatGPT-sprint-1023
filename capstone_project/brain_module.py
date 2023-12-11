#!/usr/bin/env python3

import os
import openai
from dotenv import load_dotenv

class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library
        openai.api_key = self.api_key

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "This tool is useful to convert audio messages in spanish to text (specially those from whatsapp)"

    def request_transcription(self, audio_file):
        """
        Make a request to the OpenAI Audio endpoint API

        Args:
        - file (file): The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
        - language (str, optional): The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.

        Returns:
        - str: The transcribed text.
        """
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="es",
            response_format="json"
        )

        return transcript.text
    
    def request_openai(self, message, role="system"):
        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """

        # Create a chat completion with the provided message and role
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": role, "content": message}],
            temperature=0,
        )

        return response.choices[0].message.content
