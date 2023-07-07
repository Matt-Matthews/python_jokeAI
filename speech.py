import pyttsx3

class Speech :
    def __init__ (self):
        self.rate = 140
        self.volume = 1.0
    
        self.engine = pyttsx3.init()
        self.voice = self.engine.getProperty('voices')[0]

        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('volume', self.volume)
        self.engine.setProperty('voice', self.voice.id)
    
    def speak(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()
        self.engine.stop()