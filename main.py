/*© 2022. arindamdas13. All Rights Reserved*/
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
# import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

# client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Sir!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant Paradox. ')
speak('How may I help you?.... Give me commands')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that!!')
        # query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay Sir, Opening YouTube')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay Sir, Opening Google')
            webbrowser.open('www.google.co.in')
        
        elif 'Ghani Khan Choudhury Institute of Engineering and Technology' in query:
            speak('okay Sir, I will remember the name. Opening Ghani Khan Choudhury Institute of Engineering and Technology')
            webbrowser.open('www.gkciet.ac.in')


        elif 'do you know the name of my college' in query:
            speak('No Sir.. I do not know your college name.  What is your college name?')

        elif 'now do you know my college name' in query:
            speak('Yes Sir!.... Now I know your college name. I will remember it always.')
            speak(' Do you want to open its home page again?')
        
        elif 'ok open it once again' in query:
            webbrowser.open('www.gkciet.ac.in')
            speak('Yes sir!... I will open it in another tab for you..')
            speak('Opening Ghani Khan Choudhury Institute of Engineering and Technology')
            speak('This is the home page of Ghani Khan Choudhury Institute of Engineering and Technology')
            
        
        elif 'tell me about this college' in query:
            speak('okay Sir, Opening Ghani Khan Choudhury Institute of Engineering and Technology')
            webbrowser.open('www.gkciet.ac.in/about')
            speak('Ghani Khan Choudhury Institute of Engineering & Technology (GKCIET), Malda, West Bengal was established in 2010 by Ministry of Human Resource Development, Govt. of India under the mentorship of National Institute of Technology, Durgapur and in the memory of Sri A.B.A. Ghani Khan Choudhury who had contributed immensely to societal development of the region. Institute is to become fountain-head in providing technological excellence in academics through formal/ non-formal Technical Education, Entrepreneurship & Research to meet the changing global needs of the society by transforming itself into Technical University. Okey Sir.. Can I continue?')
            

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        

        elif "what\'s up" in query or 'how are you paradox' in query:
            stMsgs = ['Just doing my thing!', 'I am fine sir!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'good bye' in query or 'goodbye paradox' in query or 'goodbye' in query or 'top' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, I will always free for you! have a good day. ')
            sys.exit()
           
        elif 'hello paradox' in query:
            speak('Hello Sir')

        elif 'bye paradox' in query:
            speak('Ok Sir, have a good day.')
            speak('I will always free for you sir!, Bye Sir!!')
            sys.exit()

        
                                    
        elif 'play music' in query:
            music_folder = 'F:\\New Musics'
            music = [1, 2, 3, 4, 5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    # res = client.query(query)
                    # results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        
