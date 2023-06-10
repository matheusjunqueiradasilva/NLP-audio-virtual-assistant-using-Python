from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import subprocess

class Suport:
    def __init__(self):
     pass
    def create_audio(self, audio, msn):
        try:
            self.audio = audio
            self.mensager= msn
            g_tts = gTTS(self.mensager, lang="pt-br")
            g_tts.save(self.audio)
            playsound(self.audio)
          
        except:
            pass
            

    def monitor_audio(self):
                recog = sr.Recognizer()
                with sr.Microphone() as mc:

                    while True:

                        print("Aguardando Comando")
                        audio = recog.listen(mc)
                        
                        try: 
                            self.mensager = recog.recognize_google(audio, language='pt-br')
                            self.mensager = self.mensager.lower()
                            self.create_audio(self.mensager)
                            print(self.mensager)
                            return self.mensager
                                             

                        except sr.UnknownValueError:
                            pass

    def comand(self):

        try:
            self.monitor_audio()
            if self.mensager == 'abrir league of legends' or self.mensager == 'abrir lolzinho':
                    subprocess.run('"D:/riot/Riot Games/League of Legends/LeagueClient.exe"')
                    print("Abrindo LoLzinho")
                    try: os.remove("mensagem.mp4")
                    except:
                        pass
                
            elif self.mensager == 'abrir google' or self.mensager == 'abra o google':
                    subprocess.run('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
                    print("Abrindo o Google")
                    try: os.remove("mensagem.mp4")
                    except:
                        pass
        except:
             pass
        
    def main(self):
        while True:
            self.comand()

Suport().main()


