import streamlit as st
import pandas as pd

from PIL import Image

import os
import shutil

if __name__ == "__main__":
    
    app_logo = Image.open("app_logo.png")
    st.set_page_config(
        page_title="Vector Addition Program",
        page_icon=app_logo,
    )
