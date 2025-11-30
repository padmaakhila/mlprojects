import streamlit as st
import pandas as pd
import numpy as np

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# -------------------------
# Streamlit UI
# -------------------------

st.set_page_config(page_title="Student Score Prediction App", layout="centered")
st.title(" Student Performance Prediction")

st.write("Fill the below details to predict the student's test score.")

# -------------------------
# Input Fields (Same as Flask)
# -------------------------

gender = st.selectbox("Gender", ["male", "female"])

race_ethnicity = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["standard", "free/reduced"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)
writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=70)

# -------------------------
# Prediction Button
# -------------------------

if st.button("Predict Score"):
    try:
        # Create data same as Flask
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        st.write("# Input Data")
        st.dataframe(pred_df)

        # Prediction
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        st.success(f" **Predicted Score: {result[0]}**")

    except Exception as e:
        st.error(f"Error during prediction: {e}")
