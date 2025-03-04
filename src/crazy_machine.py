from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=1,
    # other params...
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are good at story teller. Based on the input  {input} respond in a very polite and softly. Keep a check on the length of response",
        ),
        ("human", "{input}"),
    ]
)

r = sr.Recognizer() 
chain = prompt | llm
tmp_file='./src/cm_temp.mp3'
while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.5)
            
            #listens for the user's input 
            print("listening..")
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say: " ,MyText)
            if MyText:

                res=chain.invoke(
                    {
                    
                        "input": MyText,
                    }
                    )
                print(f"AI: {res.content}")
                tts=gTTS(res.content,lang='en',tld='com.au')
                try:
                    
                    tts.save(tmp_file)
                    
                    playsound(tmp_file)
                    os.remove(tmp_file)
                    #os.system("afplay " + tmp_file)
                    time.sleep(1)
                except Exception as ex:
                      print("Playback failed!! : ", str(ex))
                      
            
            
    except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
                print("unknown error occurred")