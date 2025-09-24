#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import joblib

# Load your trained model
model = joblib.load("/mnt/data/models_reply_classifier/baseline_logreg_tfidf.joblib")  # Replace with your model path

# App title
st.title("Text Sentiment Prediction")
st.write("Enter text below and get sentiment prediction:")

# Text input
user_input = st.text_area("Your Text Here:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Model expects list of texts
        text = [user_input]
        label = model.predict(text)[0]
        confidence = max(model.predict_proba(text)[0])

        st.success(f"**Prediction:** {label}")
        st.info(f"**Confidence:** {confidence:.2f}")


# In[ ]:




