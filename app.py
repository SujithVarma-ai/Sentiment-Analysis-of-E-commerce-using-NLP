import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.set_page_config(
    page_title="Sentiment Analysis - E-commerce",
    layout="wide"
)
st.markdown("""
<style>
.big-title {
    text-align: center;
    color: green;
    font-size: 30px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: green;
    font-size: 16px;
    margin-bottom: 40px;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    border: 2px solid #2e8b57;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="big-title">Understand the emotions behind the words 😊</div>', unsafe_allow_html=True)
st.markdown("""
<div class="subtitle">
Text sentiment prediction is a powerful tool that helps analyze emotions and opinions 
expressed in customer reviews. This can help e-commerce businesses improve products and services.
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
def predict_sentiment(text):
    text = text.lower()
    if "good" in text or "excellent" in text or "love" in text:
        return "Positive", [0.75, 0.20, 0.05]
    elif "bad" in text or "worst" in text or "hate" in text:
        return "Negative", [0.10, 0.15, 0.75]
    else:
        return "Neutral", [0.25, 0.50, 0.25]
with col1:
    st.subheader("Text Sentiment Prediction")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    text_input = st.text_area("Text for Prediction")

    if st.button("Predict"):
        if text_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            sentiment, probs = predict_sentiment(text_input)
            st.session_state.sentiment = sentiment
            st.session_state.probs = probs
with col2:
    st.subheader("Prediction Result")

    if "sentiment" in st.session_state:
        sentiment = st.session_state.sentiment
        probs = st.session_state.probs

        st.markdown(
            f'<div class="result-box">Sentiment: {sentiment}</div>',
            unsafe_allow_html=True
        )

        st.subheader("Probability Distribution")

        labels = ["Positive", "Neutral", "Negative"]
        colors = ["#4e79a7", "#9e9e9e", "#f28e2b"]

        for label, prob, color in zip(labels, probs, colors):
            st.markdown(
                f"""
                <div style="background-color:{color};
                            padding:8px;
                            border-radius:6px;
                            color:white;
                            margin-bottom:5px;
                            width:{int(prob*100)}%;">
                    {label} {int(prob*100)}%
                </div>
                """,
                unsafe_allow_html=True
            )
with col3:
    st.subheader("Sentiment Distribution")

    if "probs" in st.session_state:
        probs = st.session_state.probs

        fig, ax = plt.subplots()
        labels = ["Positive", "Neutral", "Negative"]
        ax.bar(labels, probs, color=["#4e79a7", "#9e9e9e", "#f28e2b"])
        ax.set_ylim(0, 1)
        ax.set_ylabel("Probability")
        ax.set_title("Sentiment Distribution")

        st.pyplot(fig)

