import streamlit as st
import pandas as pd
import random

st.sidebar.title("About")
st.sidebar.write(
    "This application generates random social media captions based on selected categories."
)

st.caption("Developed by Touseef Khan")

# App Title
st.title("📱 Social Media Post & Caption Generator")

st.write("Generate random social media captions based on category.")

# Load Dataset
df = pd.read_json("instagram-posts.json")

# Category Selection
category = st.selectbox(
    "Choose a Category",
    [
    "💄 Beauty",
    "💪 Fitness",
    "🍔 Food",
    "💻 Technology"
]
)

# Category Mapping
category_map = {
    "💄 Beauty": 0,
    "💪 Fitness": 1,
    "🍔 Food": 2,
    "💻 Technology": 3
}

# Generate Button
if st.button("Generate Caption"):

    all_captions = []

    for inf in df.iloc[category_map[category]]["influencer"]:
        all_captions.extend(inf["posts"])

    st.subheader("✨ Generated Caption")
    st.info(random.choice(all_captions))
    