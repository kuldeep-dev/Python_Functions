
"""
 install win32com module
 step 1 = create api from newaapi.org
 step 2 = install google chrome extension jsonview 


"""
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__name__':
    speak("news for today....Lets begin")
    url = "https://newapi.ord....."
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on the next news..Listen Carefully")
    print("Thanks for Listing....")    