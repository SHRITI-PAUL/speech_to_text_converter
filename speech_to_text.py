import speech_recognition as sr
s=sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as mic:
      print("say something")
      s.adjust_for_ambient_noise(mic,duration=1)
      audio=s.listen(mic)
      print("recognizing...")
      text=s.recognize_google(audio)
      print("we said:" +text)

if __name__== "__main__":
    speech_to_text()  
