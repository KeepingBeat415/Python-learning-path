# ---- Lemmma of Words ----
import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lemma1 = lemmatizer.lemmatize('vegetable', 'n')