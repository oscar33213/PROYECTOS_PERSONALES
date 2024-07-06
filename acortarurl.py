import streamlit as st
import pyshorteners

def shortem_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

st.set_page_config(page_title="URL Shortener", page_icon="🔗", layout="centered")
st.title("URL Shortener")
url = st.text_input("Enter the URL")

if st.button("Generate Short URL"):
    if url:
        try:
            shortened_url = shortem_url(url)
            st.success("URL shortened successfully!")
            st.write("Shortened URL: ", shortened_url)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL")

