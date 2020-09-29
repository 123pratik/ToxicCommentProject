from google.protobuf import message
import streamlit as st
import tags
import punc
import process
import re
import pickle
import nltk
import lemma
import numpy as np
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.naive_bayes import GaussianNB
from skmultilearn.problem_transform import ClassifierChain
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

vec = pickle.load(open('bowvec1.pkl', 'rb'))
model = pickle.load(open('CC_clf_bow_model1.pkl', 'rb'))

categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
lb = LabelEncoder().fit(categories)
encoded = lb.transform(categories)


model1 = CC_clf_bow = ClassifierChain(LogisticRegression())


page = st.sidebar.selectbox(
  'Choose a page', ['Prediction', 'Details'])
if page == 'Prediction':
    
    st.header('Toxic comment classifier')
    message = st.text_area('Enter you text', 'Type here')
    
    
    categories = {'toxic' : 0, 'severe_toxic' : 1, 'obscene' : 2, 'threat' : 3, 'insult' : 4, 'identity_hate': 5}
    if st.button('Process'):
        text = message
        text = tags.tagremoval(text)
        text = punc.Puncremoval(text)
        text = process.processed(text)
        text = lemma.lem(text)
        st.write(f'Transformed text :  \n{text}')
        vect_text = vec.transform([text]).toarray()
        prediction = model.predict(vect_text)
        final_result = prediction.toarray()
        st.write('1] Toxic 2] severe_toxic 3] obscene 4] threat 5] insult 6] Identity_hate')
        
        st.success('Classified as {}'.format(final_result))
        st.write('In result, 1 indicates positive and 0 indicates negative')

elif page == 'Details':
    st.write('This project is a part of Made with ML incubator')