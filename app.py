import streamlit as st
import pickle

model = pickle.load(open("training_model.sav", "rb"))

st.title("Twitter Sentiment Analysis")

tweet = st.text_area("Enter a Tweet")

if st.button("Analyze Sentiment"):
    prediction = model.predict([tweet])[0]

    if prediction == 0:
        st.error("Negative Tweet 😠")
    else:
        st.success("Positive Tweet 😊")
