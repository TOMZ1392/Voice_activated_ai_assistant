from gtts import gTTS
from playsound import playsound
spe="""One sunny morning, Max and Whiskers decided to venture into the nearby forest. They had heard rumors of a hidden treasure buried deep within the woods. With excitement in their hearts, they set off on their journey.

As they walked through the forest, they encountered various challenges. Max used his strength to move fallen branches out of their way, while Whiskers used her agility to climb trees and scout the path ahead. They made a great team, always looking out for each other.

After hours of searching, they stumbled upon an old, abandoned cabin."""
tts=gTTS(spe,lang='en',tld='com.au')
tts.save('test.mp3')
playsound('test.mp3')