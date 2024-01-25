# Speech-Recognition-Alexa 🤖
  * A simple Python script that uses various libraries for speech recognition and text-to-speech to create a basic virtual assistant similar to Alexa. The script allows users to interact with the virtual assistant by giving voice commands for tasks like playing music, checking the time, date, fetching information from Wikipedia, telling jokes, and more.

# Prerequisites
  * Make sure you have Python installed on your machine. You can download it from python.org.

# Installation
  * Install the required Python packages from the requirements.txt file using pip:

  ```
  pip install -r requirements.txt
  ```

# Usage
  * Run the script in your terminal or command prompt:

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
