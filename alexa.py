import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_instruction():
    command = ''
    instruction = "Sorry, I couldn't understand that. Please repeat your command."
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source, timeout=5, phrase_time_limit=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print('User Command:', command)
                instruction = ''  # Reset instruction if a valid command is recognized
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.WaitTimeoutError:
        print("Timed out while waiting for speech")
    return command, instruction

def my_alexa():
    command, instruction = take_instruction()
    print('Processed Command:', command)
    if any(keyword in command for keyword in ['play', 'music', 'song']):
        # Extract the song name from the command
        song = command.replace('play', '').replace('music', '').replace('song', '')
        try:
            pywhatkit.playonyt(song.strip())
        except Exception as e:
            print(f"Could not play song: {e}")
            talk("I'm sorry, I couldn't play that song")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        talk('Today is ' + current_date)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, 1)
            print('Wikipedia Summary:', info)
            talk(info)
        except Exception as e:
            print(f"Could not get information about {person}: {e}")
            talk("I'm sorry, I couldn't find information about that person")
    elif 'are you single' in command:
        talk("I'm in a committed relationship with technology. We make a great couple!")
    elif 'joke' in command:
        try:
            joke = pyjokes.get_joke()
            print('Joke:', joke)
            talk(joke)
        except Exception as e:
            print(f"Could not get joke: {e}")
            talk("I'm sorry, I couldn't tell a joke right now")
    else:
        talk(instruction)

while True:
    my_alexa()