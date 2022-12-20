import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init("espeak")

engine.setProperty('rate', 120)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', 'us-mbrola-1')


# set female voice on Windows
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    print('Alvin: ' + text)
    engine.runAndWait()


talk('hello rashmi')


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            # listener.adjust_for_ambient_noise(source, duration=0.2)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            sources = command

            # listen to commands only contains the word 'alvin'
            if 'alvin' in command:
                talk('yes rashmi')
                command = command.replace('alvin', '')
                print(command)
    except:
        print('something went wrong')
        sources = 'error'
    return sources


def run_alvin():
    command = take_command()
    dead = False

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("it's " + time + " now")
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is ' in command:
        thing = command.replace('what is ', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'error' in command:
        talk('sorry I couldn\'t hear you.')
    elif 'thank you' in command:
        talk('my pleasure.')
    elif 'shut down' in command:
        talk('ok Rashmi. Have a nice day.')
        dead = True
    else:
        talk('sorry rashmi. please say that again.')
    return dead


while True:
    status = run_alvin()
    if status:
        break
