import streamlit as st
# from apikey import google_gemini_api_keys
# import os
# import google.generativeai as genai


st.set_page_config(page_title="AI Blogging Assistant", layout="wide")
st.title("AI Blogging Assistant")
st.subheader("First LLM project help me to learn about LLMs.")

# # Configure Google AI API key
# genai.configure(api_key=google_gemini_api_keys)

# def generate(t,k,w):
#     # Use the correct model
#     # Input prompt
#     # Generate content

#     model = genai.GenerativeModel("gemini-1.5-flash")
#     prompt = f"""Generate a comprehensive, engaging blog post relevant to the given title "{t}" and Keywords "{k}". The blog should be approximately "{w}" words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""
#     response = model.generate_content(prompt)
    # st.write(response.text)


with st.sidebar:
    st.title("Input You Blog Details")
    st.subheader("Enter details of the blog you want to generate")

    t=st.text_input("Blog Title")

    k=st.text_area("Keywords (Comma-seprated)")

    w=st.slider("Number of Words",min_value=100,max_value=1000,step=100)

    images=st.number_input("Number of Images",min_value=0,step=1)

    submit_button=st.button("Submit")

if submit_button:
    st.write("--------------------------------------------------------------------------------------------------------")
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png")
    st.write("API Key of the project is deleted.")
    # generate(t,k,w)
