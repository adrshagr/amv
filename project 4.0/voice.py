import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)
engine.say("The current weather in Lucknow is Clear Sky with temperatue 20 degree celcius.")
engine.runAndWait()