# ---- Lemmma of Words ----
import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lemma1 = lemmatizer.lemmatize('vegetable', 'n')

# ---- Process Audio File ----
form speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# initial recognizer
recognizer = Recognizer()

# open audio file, then load with content as audio object
with AudioFile('chile.wav') as audio_file:
    audio = recognizer.record(audio_file)
# convert into text
text = recognizer.recognize_google(audio)
# load library 
nltk.download('vader_lexicon')

# initial sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# label with score
scores = analyzer.polarity_scores(text)

if scores['compound'] > 0:
    print('Positive Speech')
else:
    print('Negative Speech')


