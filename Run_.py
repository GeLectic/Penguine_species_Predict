import streamlit as st
import pickle
import numpy as np


with open("Logistic.pkl", "rb") as file:
    model = pickle.load(file)


st.title("Penguin Species Prediction")
st.write("Predict the species of a penguin based on its features!")


st.sidebar.header("Input Features")
def user_input():
    island = st.sidebar.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
    bill_length_mm = st.sidebar.slider("Bill Length (mm)", 30.0, 60.0, 45.0)
    bill_depth_mm = st.sidebar.slider("Bill Depth (mm)", 13.0, 21.0, 17.0)
    flipper_length_mm = st.sidebar.slider("Flipper Length (mm)", 170, 230, 200)
    body_mass_g = st.sidebar.slider("Body Mass (g)", 2500, 6500, 4000)
    sex = st.sidebar.selectbox("Sex", ["male", "female"])


    island_mapping = {"Biscoe": 0, "Dream": 1, "Torgersen": 2}
    sex_mapping = {"male": 1, "female": 0}
    island_encoded = island_mapping[island]
    sex_encoded = sex_mapping[sex]

    features = np.array([island_encoded, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex_encoded])
    return features


features = user_input()


if st.button("Predict"):
    prediction = model.predict([features])[0]
    species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
    species = species_mapping[prediction]


    st.subheader("Prediction")
    st.success(f"The predicted species is: **{species}**")


    st.subheader("Facts about the Predicted Species")
    if species == "Adelie":
        st.write("""
        - The Adelie Penguin is one of the most widespread penguin species in Antarctica.
        - They are excellent swimmers and can reach speeds of up to 15 km/h.
        - Adelie Penguins primarily feed on krill and fish.
        """)
    elif species == "Chinstrap":
        st.write("""
        - Chinstrap Penguins are named for the distinctive black band under their head.
        - They are found in the Southern Ocean and breed on Antarctic islands.
        - Chinstrap Penguins are known for their loud, braying calls.
        """)
    elif species == "Gentoo":
        st.write("""
        - Gentoo Penguins are the fastest swimming penguin species, reaching speeds of 36 km/h.
        - They are recognizable by their bright orange beak and white stripe across the top of their head.
        - Gentoo Penguins build nests out of stones and are known to be very territorial.
        """)

