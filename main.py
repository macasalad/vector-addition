import streamlit as st
from PIL import Image
import numpy as np

if __name__ == "__main__":

    st.markdown("""# Vector Addition Calculator
    hahahahahahahaha lagay ng description""")
    app_logo = Image.open("app_logo.png")
    st.set_page_config(
        page_title="Vector Addition Calculator",
        page_icon=app_logo,
    )
    
    resultant_vector_x = 0
    resultant_vector_y = 0
    ans = "Yes"

    while ans == "Yes":
        ans = st.text_input("Would you like to add a vector (Yes/No): ")
        if ans == "Yes" or ans == "No":
            if ans == "Yes":
                print("Input magnitude of vector: ", end="")
                vector_magnitude = float(input())
                print("Input direction of vector (in degrees, from the positive x-axis): ", end="")
                vector_direction = float(input())
                resultant_vector_x += (vector_magnitude*(np.cos(np.deg2rad(vector_direction))))
                resultant_vector_y += (vector_magnitude*(np.sin(np.deg2rad(vector_direction))))
        else:
            print("Input is invalid.")
            ans == "Yes"

    resultant_vector_magnitude = np.sqrt((resultant_vector_x**2) + (resultant_vector_y**2))
    resultant_vector_direction = np.rad2deg(np.arctan(abs(resultant_vector_y/resultant_vector_x)))

    print(resultant_vector_magnitude)

    if resultant_vector_x > 0 and resultant_vector_y == 0:
        print("0° East")
    elif resultant_vector_x > 0 and resultant_vector_y > 0:
        print(str(resultant_vector_direction) + "° North of East")
    elif resultant_vector_x == 0 and resultant_vector_y > 0:
        print("90° East")
    elif resultant_vector_x < 0 and resultant_vector_y > 0:
        print(str(resultant_vector_direction) + "° North of West")
    elif resultant_vector_x < 0 and resultant_vector_y == 0:
        print("180° East")
    elif resultant_vector_x < 0 and resultant_vector_y < 0:
        print(str(resultant_vector_direction) + "° South of West")
    elif resultant_vector_x == 0 and resultant_vector_y < 0:
        print("270° East")
    elif resultant_vector_x > 0 and resultant_vector_y < 0:
        print(str(resultant_vector_direction) + "° South of East")

    with st.expander("Credits", expanded = False):
        st.markdown("""wahaha credits""")
