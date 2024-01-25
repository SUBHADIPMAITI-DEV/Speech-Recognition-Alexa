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
            voice = listener.listen(source)
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
    return command, instruction

def my_alexa():
    command, instruction = take_instruction()
    print('Processed Command:', command)
    if any(keyword in command for keyword in ['play', 'music', 'song']):
        # Extract the song name from the command
        song = command.replace('play', '').replace('music', '').replace('song', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song.strip())
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        talk('Today is ' + current_date)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print('Wikipedia Summary:', info)
        talk(info)
    elif 'are you single' in command:
        talk("I'm in a committed relationship with technology. We make a great couple!")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print('Joke:', joke)
        talk(joke)
    else:
        talk(instruction)

while True:
    my_alexa()
