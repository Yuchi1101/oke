import streamlit as st

# CSS untuk background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/Yuchi1101/my-images/main/patrick.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Aplikasi Serius dengan Background Patrick")
st.write("Selamat datang di aplikasi berbasis meme 😎")
