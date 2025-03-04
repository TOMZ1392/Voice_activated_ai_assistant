# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:26:12 2024

@author: T
"""

from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

samp_text="Let’s delve into one of these timeless classics, The Lottery Ticket by Anton Chekhov (1887). In this story, Ivan Dmitritch and his wife are thrilled when they discover they might have won the lottery. They immediately begin to dream of what they would do with their potential newfound wealth. In the course of daydreaming, the couple reveals their true wishes and plans until they are brought back to reality. Chekhov’s story is a melancholy examination of human nature, the impact of money, and the surprising results of our deeply held desires. It's a journey of hope, disappointment, and self-discovery that will leave you pondering long after you’ve finished reading."
# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=samp_text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')