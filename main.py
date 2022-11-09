import streamlit as st
from PIL import Image

st.markdown("""# Vector Addition Calculator
hahahahahahahaha lagay ng description""")

app_logo = Image.open("app_logo.png")
st.set_page_config(
  page_title="Vector Addition Calculator",
  page_icon=app_logo,
)
