import streamlit as st

# Function to convert units
def convert_units(value, unit_from, unit_to):
    # Dictionary to store conversion factors
    conversions = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000,     # 1 kilogram = 1000 grams
    }

    # Create a key based on the units to convert from and to
    key = f"{unit_from}_{unit_to}"

    # Check if the conversion key exists in the dictionary
    if key in conversions:
        conversion = conversions[key]
        return value * conversion  # Perform the conversion
    else:
        return "Conversion not available"  # Return a message if conversion is not available

# Streamlit app title
st.title("Unit Converter")

# Input field to enter the value to convert
value = st.number_input("Enter the value to convert")

# Dropdown to select the unit to convert from
unit_from = st.selectbox("Convert From: ", ["meter", "kilometer", "gram", "kilogram"])

# Dropdown to select the unit to convert to
unit_to = st.selectbox("Convert To:", ["meter", "kilometer", "gram", "kilogram"])

# Button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    # Display the result
    st.markdown(f"{value} {unit_from} is equal to {result} {unit_to}")