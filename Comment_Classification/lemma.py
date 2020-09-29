
# import these modules 
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 
def lem(sentence):
    Sentence = ""
    for word in sentence.split():
        lemma = lemmatizer.lemmatize(word, pos='a')
        Sentence += lemma
        Sentence += " "
    Sentence = Sentence.strip()
    return Sentence

if __name__ == '__main__':
    print('')
