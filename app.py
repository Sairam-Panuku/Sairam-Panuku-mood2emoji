import streamlit as st
from textblob import TextBlob
import re

# ------------------------------
# 🎯 CONFIGURATION & FILTERS
# ------------------------------
BAD_WORDS = [
    "damn", "hell", "shit", "bitch", "crap", "stupid",
    "idiot", "fool", "dumb", "kill", "suicide"
]

def contains_bad_words(text):
    """Check if text contains inappropriate words."""
    text_lower = text.lower()
    return any(word in text_lower for word in BAD_WORDS)

# ------------------------------
# 💬 MOOD DETECTION FUNCTION
# ------------------------------
def detect_mood(text):
    """Analyze text mood and return (emoji, explanation, polarity)."""
    if not text.strip():
        return "😐", "Please enter a sentence!", 0.0
    
    if contains_bad_words(text):
        return "😐", "Let's keep our words kind and friendly!", 0.0
    
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 2)

    # Expanded mood mapping for better expression
    if polarity >= 0.6:
        return "🤩", "That's super cheerful and excited!", polarity
    elif 0.3 <= polarity < 0.6:
        return "😃", "That sounds really happy!", polarity
    elif 0.1 <= polarity < 0.3:
        return "😊", "That feels positive and pleasant.", polarity
    elif -0.1 < polarity < 0.1:
        return "😐", "That sounds neutral or balanced.", polarity
    elif -0.3 <= polarity <= -0.1:
        return "😟", "That feels a bit unhappy or worried.", polarity
    elif -0.6 <= polarity < -0.3:
        return "😢", "That sounds quite sad.", polarity
    else:  # polarity < -0.6
        return "😡", "That sounds really upset or angry.", polarity

# ------------------------------
# 🖥️ STREAMLIT APP UI
# ------------------------------
st.set_page_config(page_title="Kid-safe Mood Detector", page_icon="🎭", layout="centered")

st.title("🎭 Kid-safe Text → Mood Detector")
st.markdown("This fun app analyzes your sentence and shows how it *feels* — using friendly emojis. Perfect for ages **12–16**!")

user_input = st.text_area("✏️ Type a short sentence:", placeholder="Example: I love sunny days!", height=100)

if st.button("🔍 Analyze Mood"):
    emoji, explanation, polarity = detect_mood(user_input)
    
    # Output section
    st.markdown(f"## {emoji}")
    st.success(explanation)
    
    if not contains_bad_words(user_input) and user_input.strip():
        st.info(f"**Sentiment Score:** {polarity}  (Range: -1 to +1)")

# ------------------------------
# 🎓 TEACHER MODE
# ------------------------------
st.markdown("---")
teacher_mode = st.checkbox("🎓 Teacher Mode — Show How It Works")

if teacher_mode:
    st.subheader("🧩 How the App Works")
    st.markdown("""
    1. **Input** — Student types a sentence.  
    2. **Safety Filter** — Checks for bad or unsafe words.  
    3. **Sentiment Analysis** — Using **TextBlob**, the app calculates a *polarity score* from -1 (negative) to +1 (positive).  
    4. **Mood Mapping:**  
       | Polarity Range | Emoji | Mood |
       |----------------|-------|------|
       | > +0.6 | 🤩 | Excited / Joyful |
       | +0.3 to +0.6 | 😃 | Happy |
       | +0.1 to +0.3 | 😊 | Pleasant |
       | -0.1 to +0.1 | 😐 | Neutral |
       | -0.3 to -0.1 | 😟 | Slightly Unhappy |
       | -0.6 to -0.3 | 😢 | Sad |
       | < -0.6 | 😡 | Angry / Frustrated |
    5. **Output** — Shows emoji + one-line feedback.
    """)
    
    st.markdown("**Try these examples:**")
    st.code("I won a prize today! → 🤩")
    st.code("I feel great about my project. → 😃")
    st.code("The sky is blue. → 😐")
    st.code("I'm worried about my test. → 😟")
    st.code("I lost my toy. → 😢")
    st.code("This is the worst day ever! → 😡")

# ------------------------------
# 👣 FOOTER
# ------------------------------
st.markdown("---")
st.caption("Made for students (12–16) | Safe | Fun | Educational — by Sairam Panuku 🌱")
