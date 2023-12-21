import openai
import streamlit as st

def get_response_from_chatgpt(text):
    prompt= f"Identify and return the sentiment either positive or negative in given text. text: {text}"
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
                {"role": "system", "content": "You are a helpful Text Sentiment Analyzer That returns One Word Sentiment."},
                {"role": "user", "content":prompt }
        ],
        temperature = 0.1
        )
    sentiment = response.choices[0].message.content
    return sentiment

st.title("ChatGPT Text Sentiment Analyzer")

keys = st.text_input("Enter your OpenAI API key")

if not keys:
    st.warning("Please enter your OpenAI API key")
else:
    openai.api_key = keys

    text = st.text_input("Enter Text", value="I like pizza")

    if st.button("Submit"):
        if keys:
            with st.spinner("OpenAI is processing"):
                try:
                    sentiment = get_response_from_chatgpt(text)
                    st.success("Completed Successfully")
                    st.write(f"Sentiment: {sentiment}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter your OpenAI API key")
