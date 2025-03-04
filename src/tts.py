import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf
from playsound import playsound

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print(device)

model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler_tts_mini_v0.1").to(device)
tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler_tts_mini_v0.1")

prompt = "Let’s delve into one of these timeless classics, The Lottery Ticket by Anton Chekhov (1887). In this story, Ivan Dmitritch and his wife are thrilled when they discover they might have won the lottery. They immediately begin to dream of what they would do with their potential newfound wealth. In the course of daydreaming, the couple reveals their true wishes and plans until they are brought back to reality. Chekhov’s story is a melancholy examination of human nature, the impact of money, and the surprising results of our deeply held desires. It's a journey of hope, disappointment, and self-discovery that will leave you pondering long after you’ve finished reading."
description = "A female speaker delivers narration of bedtime story to a kid. The voice is clear and not very fast."

input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
audio_arr = generation.cpu().numpy().squeeze()
speech_file="parler_tts_out.wav"
sf.write(speech_file, audio_arr, model.config.sampling_rate)




# for playing note.wav file
playsound(speech_file)
print('playing sound using  playsound')