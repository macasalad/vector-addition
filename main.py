import streamlit as st
from PIL import Image
import numpy as np

if __name__ == "__main__":
    
    applogo = Image.open("app_logo.png")
    st.set_page_config(
        page_title="Vector Addition Program",
        page_icon=applogo,
    )
    
    st.markdown("""# Vector Addition Calculator
hahahahahahahaha lagay ng description""")
    
    with st.expander("Credits", expanded = False):
        st.markdown("""wahaha credits""")
