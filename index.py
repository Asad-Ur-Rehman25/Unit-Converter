import streamlit as st

 # st.title()


def convert_unit(value: float,unit_from: str,unit_to: str):
    if unit_from == "kilometer" and unit_to == "meter":
        return value * 1000
    elif unit_from == "meter" and unit_to == "kilometer":
        return value * 0.001
    elif unit_from == "kilogram" and unit_to == "gram":
        return value * 1000
    elif unit_from == "gram" and unit_to == "kilogram":
        return value * 0.001

    elif unit_from == "foot" and unit_to == "inch":
        return value * 12 
    elif unit_from == "inch" and unit_to == "foot":
        return value * 0.0833333333333333 
    
    elif unit_from == "inch" and unit_to == "centimetre":
        return value * 2.54 
    elif unit_from == "centimetre" and unit_to == "inch":
        return value * 0.393701
    else:
        return "please enter matching unit name"
def unitconvert():  
    st.title("UNIT CONVERTER")
    st.write("welcome to unit converter")
    value= st.number_input("Enter your number")
    unit_from = st.text_input("Enter your text")
    unit_to = st.text_input("Enter to your text")
# result = convertunit(value , unit_from, unit_to )
# # print(result)
# st.write(result) 
    if st.button("Convert"):
        result = convert_unit(value, unit_from, unit_to)
        st.write(result)
unitconvert()