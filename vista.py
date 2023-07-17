from speech import Speech 
from  recognition import Recognition
# from search import Googlesearch
import pyjokes

vistaRecognize = Recognition()
vistaSpeech = Speech()
answer = ''
print(answer.find('yes'))
vistaSpeech.speak('Do you wanna hear a joke?')

while answer.find('no') == -1:
    answer = vistaRecognize.recognize()
    print(answer)
    # if answer.find('no') != -1: answer = 'no'
    if answer.find('yes') != -1:
        joke = pyjokes.get_joke(language="en", category="all")
        print(joke)
        vistaSpeech.speak(joke)
        vistaSpeech.speak('Do you wanna hear another joke?')
        answer = vistaRecognize.recognize()
    elif answer.find('yes') == -1 | answer.find('no') == -1 : vistaSpeech.speak('i only reply to yes and no')
    
vistaSpeech.speak('Goodbye bitch!')