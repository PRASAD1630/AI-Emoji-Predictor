import streamlit as st
from predictor import predict_emoji

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Emoji Predictor",
    page_icon="😊",
    layout="centered"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#4F46E5;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:30px;
}

.result-box{
    background-color:#EEF2FF;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown(
    '<div class="main-title">😊 AI Emoji Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Predict suitable emojis from your text using simple NLP.</div>',
    unsafe_allow_html=True
)

# ----------------------------
# Input
# ----------------------------
sentence = st.text_area(
    "✍️ Enter your sentence",
    placeholder="Example: I got an AI internship today!",
    height=120
)

# ----------------------------
# Predict Button
# ----------------------------
if st.button("🚀 Predict Emoji", use_container_width=True):

    if sentence.strip() == "":
        st.warning("⚠️ Please enter a sentence.")
    else:

        emojis, keywords = predict_emoji(sentence)

        # Mood Detection
        positive = [
            "happy", "love", "party", "birthday",
            "success", "pass", "internship", "job", "smile"
        ]

        negative = [
            "sad", "cry", "fail", "angry"
        ]

        mood = "😐 Neutral"

        if any(word in keywords for word in positive):
            mood = "😊 Happy"

        elif any(word in keywords for word in negative):
            mood = "😢 Sad"

        confidence = min(50 + len(keywords) * 10, 100)

        st.success("Prediction Completed Successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("😊 Mood", mood)

        with col2:
            st.metric("📊 Confidence", f"{confidence}%")

        st.progress(confidence)

        st.markdown("---")

        st.subheader("🔍 Detected Keywords")

        if keywords:
            st.write(", ".join(word.title() for word in keywords))
        else:
            st.info("No matching keywords detected.")

        st.markdown("---")

        st.subheader("🎉 Predicted Emojis")

        st.markdown(
            f"<div class='result-box'><h1>{' '.join(emojis)}</h1></div>",
            unsafe_allow_html=True
        )

        st.balloons()

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")

st.markdown(
    "<div class='footer'>Made with ❤️ using Python & Streamlit</div>",
    unsafe_allow_html=True
)