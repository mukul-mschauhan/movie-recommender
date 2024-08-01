# pip install streamlit langchain google-generativeai langchain-google-genai
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the Page - Title of the Page
st.title("Movie Recommender System using Google Gemini˙✧˖°🍿 ༘ ⋆｡˚")
user_input = st.text_input("Enter a movie title, genre or keywords (e.g. sci-fi movie)")

# LLM Model...
# Prompt Template
demo_template = '''Based on the Input, here are some movie recommendations\
    for {user_input}:\n'''
template = PromptTemplate(input_variable = ['user_input'], 
                          template=demo_template)

# Initialise the Gemini Pro Model
llms = ChatGoogleGenerativeAI(model = "gemini-pro", 
                              api_key = "AIzaSyBOyi_88OdnheqC6c9wsma6HxnAryd5CtI")

# Generate the Recommendations when the User Provides Input
if user_input:
    prompt = template.format(user_input = user_input)
    recommendations = llms.predict(text = prompt)
    st.write(f"Recommendations for you:\n {recommendations}")
else:
    st.write(" ")