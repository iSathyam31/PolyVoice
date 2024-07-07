import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        
    try:
        text=r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print("Could not request result from google speech recogition service: {0}".format(e))    

def llm_model(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_text)
    result = response.text
    return result

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    
    ## Saving the speech from the given text in the mp3 format
    tts.save("speech.mp3")