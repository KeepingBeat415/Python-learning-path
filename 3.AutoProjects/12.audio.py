from pydub import AudioSegment

# convert into list with second
original = AudioSegment.from_wav('beat.wav')

reversed = original.reverse()

reversed.export('reversed.wav')

first_row = orignal[0:2000] # first 2 second audio

# merge audio
merged = original + AudioSegment.silent(1000) + reversed
merged.export('merged.wav')

# ---- overlay/mix audio ----
beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')

beat2 = beat * 2
beat2.export('beat2.wav')

mixed = beat2.overlay(sax)
mixed.export('mixed.wav')

# ---- speech recognition ----
from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

with AudioFile('chile.wav') as audio_file:
    audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)

print(text)