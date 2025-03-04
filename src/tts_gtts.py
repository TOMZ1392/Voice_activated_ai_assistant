from gtts import gTTS
import spacy
from io import BytesIO
from pygame import mixer
import time
import threading as thr

story="""Sure! Here's a story about a dog and cat 

**The Adventures of Max and Whiskers**

Once upon a time in a cozy little town, there lived a dog named Max and a cat named Whiskers. Max was a playful Golden Retriever with a heart of gold, and Whiskers was a clever tabby cat with a knack for getting into mischief.

Max and Whiskers lived in the same neighborhood and often saw each other during their daily adventures. Despite their differences, they shared a special bond and loved exploring together.

"""
story2="""One sunny morning, Max and Whiskers decided to venture into the nearby forest. They had heard rumors of a hidden treasure buried deep within the woods. With excitement in their hearts, they set off on their journey.

As they walked through the forest, they encountered various challenges. Max used his strength to move fallen branches out of their way, while Whiskers used her agility to climb trees and scout the path ahead. They made a great team, always looking out for each other.

After hours of searching, they stumbled upon an old, abandoned cabin. Inside, they found a dusty map that seemed to lead to the treasure. With renewed determination, they followed the map's clues, which took them through winding paths and across bubbling streams.

Finally, they reached a clearing where a large oak tree stood. According to the map, the treasure was buried beneath its roots. Max and Whiskers dug together, their paws working in unison. After a while, they uncovered a small chest filled with sparkling jewels and gold coins.

But the real treasure, they realized, was the friendship they had forged along the way. Max and Whiskers returned to their neighborhood, not just with riches, but with memories of an unforgettable adventure.

From that day on, Max and Whiskers were inseparable. They continued to explore, solve mysteries, and share countless adventures, always knowing that together, they could overcome any challenge.

And so, the dog and the cat lived happily ever after, proving that true friendship knows no bounds."""


nlp = spacy.load('en_core_web_sm')

text = story + story2
tokens = nlp(text)

for sent in tokens.sents:
    print(sent)





class ProcTTS:
    __mp3_fp:None
    text=''
    
    def get_mp3fp(self):
        return self.__mp3_fp
        
    def __init__(self,t):
        self.text=t
        
    def speak(self):
        
        if self.__mp3_fp:
            mixer.init()
            self.__mp3_fp.seek(0)
            mixer.music.load(self.__mp3_fp, "mp3")
            mixer.music.play()
        else:
            print('TTS data unavailable')

    
    def genTTS(self):
        self.__mp3_fp = BytesIO()
        tts = gTTS(self.text)
        tts.write_to_fp(self.__mp3_fp)
    
        

#text_data=[story,story2]
th_list=[]
for t in tokens.sents:
    obj=ProcTTS(str(t))
    tr=thr.Thread(target=obj.genTTS(),)
    tr.start()
    th_list.append((obj,tr))
    
    
ctr=0
print(len(th_list))

for i in range(0,len(th_list)):
    print(i)
    if i == ctr:
        th_list[i][1].join()
        print(th_list[i][0].text)
        print(th_list[i][0].get_mp3fp())
        th_list[1][0].speak()
        ctr+=1
