import speech_recognition as sr

class Recognition:
    def __init__(self):
        self.recognition = sr.Recognizer() 
        
    def recognize(self):
        with sr.Microphone() as source:
            print('Say something!')
            audio = self.recognition.listen(source, )
        try:
            print("You said " + self.recognition.recognize_google(audio))
            return self.recognition.recognize_google(audio)
        except sr.UnknownValueError:
            print('Google could not understand audio')
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))