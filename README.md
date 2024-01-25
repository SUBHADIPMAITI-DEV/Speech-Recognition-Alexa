# Speech-Recognition-Alexa
  A simple Python script that uses various libraries for speech recognition and text-to-speech to create a basic virtual assistant similar to Alexa. The script allows users to interact with the virtual assistant by giving voice commands for tasks like playing music, checking the time, date, fetching information from Wikipedia, telling jokes, and more.

# Prerequisites
  Make sure you have Python installed on your machine. You can download it from python.org.

# Installation
  Install the required Python packages using pip:

1. SpeechRecognition:
      This is a library that provides support for speech recognition in Python. It allows you to recognize speech from various audio sources.

  ```
  pip install SpeechRecognition
  ```

2. pyttsx3:
     This library is a text-to-speech conversion library in Python. It provides a simple interface to convert text into spoken words using various speech engines.
   
  ```
  pip install pyttsx3
  ```

3. pywhatkit:
    A Python library that allows you to perform various tasks using the web. In this script, it's being used to play a song on YouTube based on a user's     command.

  ```
  pip install pywhatkit
  ```

4. Wikipedia:
     This is a Python wrapper for the Wikipedia API. It simplifies the process of fetching information from Wikipedia.

  ```
  pip install wikipedia
  ```

5. pyjokes: A library that provides a collection of jokes for use in Python programs. In the script, it's used to generate and tell jokes.

  ```
  pip install pyjokes
  ```

# Usage
  Run the script in your terminal or command prompt:

  ```
  python alexa.py
  ```

1. The virtual assistant will start listening for your voice commands.

2. You can give commands such as:

  * "Play [song name]"

  * "What is the time?"

  * "Tell me a joke"

  * "Who is [person]?"

3. The virtual assistant will respond accordingly.

# Code Description
  The script defines a virtual assistant (my_alexa()) that continuously listens for voice commands using the SpeechRecognition library. When a command is     recognized, the assistant performs various tasks based on the command, such as playing a song, fetching the current time, date, or providing information from Wikipedia. The assistant also has a sense of humor and can tell jokes using the pyjokes library.

* Feel free to extend and modify the script according to your preferences and needs.

# Note: Make sure your microphone is properly configured and accessible by the script for accurate speech recognition.
