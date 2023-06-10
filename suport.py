from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import subprocess

class Support:
    def __init__(self):
        pass
    
    def create_audio(self, audio, message):
        try:
            self.audio = audio
            self.message = message
            g_tts = gTTS(self.message, lang="pt-br")
            g_tts.save(self.audio)
            playsound(self.audio)
        except:
            pass
    
    def monitor_audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mc:
            while True:
                print("Waiting for command")
                audio = recognizer.listen(mc)
                
                try:
                    self.message = recognizer.recognize_google(audio, language='pt-br')
                    self.message = self.message.lower()
                    self.create_audio(self.message)
                    print(self.message)
                    return self.message
                except sr.UnknownValueError:
                    pass
    
    def command(self):
        try:
            self.monitor_audio()
            if self.message == 'open league of legends' or self.message == 'open lol':
                subprocess.run('"D:/riot/Riot Games/League of Legends/LeagueClient.exe"')
                print("Opening League of Legends")
                try:
                    os.remove("message.mp4")
                except:
                    pass
            elif self.message == 'open google':
                subprocess.run('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
                print("Opening Google")
                try:
                    os.remove("message.mp4")
                except:
                    pass
        except:
            pass
    
    def main(self):
        while True:
            self.command()

Support().main()