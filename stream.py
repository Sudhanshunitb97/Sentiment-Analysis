import streamlit as st
import numpy as np
import re
import pickle
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

@st.cache_resource
def load_models():
    w2vmodel = Word2Vec.load("w2vmodel_2.model")
    with open("regressor_2.pkl", "rb") as f:
        regressor_2 = pickle.load(f)
    return w2vmodel, regressor_2

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)  # fixed regex
    tokens = text.split()
    return [word for word in tokens if word not in ENGLISH_STOP_WORDS]

def get_avg_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else None

w2vmodel, regressor_2 = load_models()

st.title("🔮 JEE Coaching Review Rating Predictor")
review = st.text_area("Enter your review below:")

if st.button("Predict Rating"):
    tokens = preprocess(review)
    vec = get_avg_vector(tokens, w2vmodel)

    if vec is None:
        st.error(" None of the words were recognized. Try a different review.")
        st.warning(" Debug info:")
        st.code(tokens)
        known_words = [word for word in tokens if word in w2vmodel.wv]
        st.warning(f" Known words found: {known_words}")
    else:
        rating = regressor_2.predict(vec.reshape(1, -1))[0]
        st.success(f" Predicted Rating: {rating:.2f} / 10")
