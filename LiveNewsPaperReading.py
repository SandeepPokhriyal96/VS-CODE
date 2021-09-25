
def speak(str):

    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if _name_ == '__main__':
    speak("Welcome Which type of News You want")
    speak("Press 1 for business")
    speak("Press 2 for Entertainment")
    speak("Press 3 for Health")
    speak("Press 4 for Science")
    speak("Press 5 for Sports")
    speak("Press 6 for Technology")

x= int(input ())

if x == 1:

    if _name_ == '__main__':
        speak("Top 5 Business News is")
        import requests
        import json

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=in&category=business&'
               'apiKey=2c97997fe0e04f1798f0b392a750625f')

        respose = requests.get(url)
        text = respose.text
        my_json = json.loads(text)
        for i in range(0, 6):
            speak(my_json['articles'][i]['title'])

elif x==2:
    if _name_ == '__main__':
        speak("Top 5 Entertainment News are")
        import requests
        import json

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=in&category=entertainment&'
               'apiKey=2c97997fe0e04f1798f0b392a750625f')

        respose = requests.get(url)
        text = respose.text
        my_json = json.loads(text)
        for i in range(0, 6):
            speak(my_json['articles'][i]['title'])

elif x==3:

    if _name_ == '__main__':
        speak("Top 5 Health News are")
        import requests
        import json

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=in&category=health&'
               'apiKey=2c97997fe0e04f1798f0b392a750625f')

        respose = requests.get(url)
        text = respose.text
        my_json = json.loads(text)
        for i in range(0, 3):
            speak(my_json['articles'][i]['title'])

elif x==4:
    if _name_ == '__main__':
        speak("Top 5 Science News are")
        import requests
        import json

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=in&category=science&'
               'apiKey=2c97997fe0e04f1798f0b392a750625f')

        respose = requests.get(url)
        text = respose.text
        my_json = json.loads(text)
        for i in range(0, 5):
            speak(my_json['articles'][i]['title'])

elif x==5:
    if _name_ == '__main__':
        speak("Top 5 Sports News are")
        import requests
        import json

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=in&category=sports&'
               'apiKey=2c97997fe0e04f1798f0b392a750625f')

        respose = requests.get(url)
        text = respose.text
        my_json = json.loads(text)
        for i in range(0, 6):
            speak(my_json['articles'][i]['title'])


elif x==6:
    if _name_ == '__main__':
        speak("Top 5 Technology News are")
        import requests
        import json

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=in&category=technology&'
               'apiKey=2c97997fe0e04f1798f0b392a750625f')

        respose = requests.get(url)
        text = respose.text
        my_json = json.loads(text)
        for i in range(0, 6):
            speak(my_json['articles'][i]['title'])

else:
    if _name_ == '__main__':
        speak("wrong input")
