import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import threading
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
stop_event = threading.Event()

def start_listening():
    stop_event.clear()  # Clear the event flag
    listen_thread = threading.Thread(target=listen_and_update)
    listen_thread.start()

def stop_listening():
    stop_event.set()  # Set the event flag to stop the listening thread

def listen_and_update():
    with sr.Microphone() as source:
        while not stop_event.is_set():
            try:
                print('Listening...')
                text = listener.listen(source)
                command = listener.recognize_google(text)
                command = command.lower()
                print('User Command:', command)
                response_box.delete(1.0, tk.END)  # Clear previous text
                response_box.insert(tk.END, command)  # Insert new text
                process_command(command)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

def process_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song.strip())
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        talk('Today is ' + current_date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print('Wikipedia Summary:', info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print('Joke:', joke)
        talk(joke)
    elif 'stop' in command:
        stop_listening()
    else:
        talk("Sorry, I couldn't understand that.")

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Create a Tkinter window
window = tk.Tk()
window.title("Voice Assistant")

# Create a frame to hold widgets
frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

# Create a text box to display responses
response_box = tk.Text(frame, height=10, width=50)
response_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create start button
start_button = ttk.Button(frame, text="Start Listening", command=start_listening, style='TButton')
start_button.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="w")

# Create stop button
stop_button = ttk.Button(frame, text="Stop Listening", command=stop_listening, style='TButton')
stop_button.grid(row=1, column=1, padx=(5, 10), pady=10, sticky="e")

# Change style of buttons
style = ttk.Style()
style.configure('TButton', foreground='black', background='#4CAF50', font=('Helvetica', 12), borderwidth=0, width=20)

# Disable resizing of the window
window.resizable(False, False)

window.mainloop()
