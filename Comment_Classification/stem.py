import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
def stemming(sentence):
    Sentence = ""
    for word in sentence.split():
        stem = stemmer.stem(word)
        Sentence += stem
        Sentence += " "
    Sentence = Sentence.strip()
    return Sentence

if __name__ == '__main__':
    print('')