import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
# You can adjust the voice and other properties here
# engine.setProperty('rate', 150)  # Speed of speech (words per minute)
# engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Say the given text
text_to_speak = "the context of the scene is likely a school boy crossing the road with traffic lights and cars"
engine.say(text_to_speak)

# Wait for the speech to finish
engine.runAndWait()
