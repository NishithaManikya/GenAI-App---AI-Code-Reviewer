from openai import OpenAI
import streamlit as st
import json

f=open("keys/.key.txt")
key=f.read()
client=OpenAI(api_key=key)

st.title(" Python Code Reviewer")


prompt = st.text_area("Enter your Python code", height=200)


        




if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": """You are a friendly AI Assistant of Python code debugger.
you will take a Python code as a user input. Your job role is to explain the bugs and fix the bug.
and generate the correct code in output. you will generate output in JSON file.
your output sample is given below:
{"Bugs": "errors of code", "Fixed_code": "correct code"}"""},

            {"role": "user", "content": f"explain the Bugs and Fixed_code: {prompt}"}
        ],
        temperature=0.5
    )

    try:
        review = json.loads(response.choices[0].message.content)
        st.write(review)
        st.write(review["Bugs"])
        st.code(review["Fixed_code"], language='python')
    except (IndexError, KeyError, json.JSONDecodeError) as e:
        st.error("Failed to process response. Please try again.")
