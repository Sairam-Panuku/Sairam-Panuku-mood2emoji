# 🎭 Kid-safe Text-Mood Detector  
*A Streamlit + TextBlob app for students (ages 12–16)*  

---

## 🌟 Overview  
This project is a **kid-friendly mood detection app** that takes a short sentence and returns:  
- An emoji (😀 😐 😞)  
- A simple one-line explanation (e.g., “Sounds happy!”)  

It is designed to help students understand **sentiment analysis** in a safe and fun way.

---

## 🚀 Features  
- ✅ Simple input box for typing any sentence  
- 😀 😐 😞 Emoji-based mood output  
- 🧠 Built-in **TextBlob** sentiment analysis  
- 🚫 Filters bad/inappropriate words  
- 👩‍🏫 “Teacher Mode” — shows how the app works step-by-step  

---

## 🧰 Tech Stack  
- **Python 3.9+**  
- **Streamlit** for web interface  
- **TextBlob** for sentiment analysis  

---

## 🧩 Setup & Run Instructions  

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/sairam-panuku-mood2emoji.git
   cd sairam-panuku-mood2emoji
Install dependencies


pip install -r requirements.txt
Run the app

streamlit run app.py
Open in browser (usually auto-opens)


http://localhost:8501


👩‍🏫 How Kids Learn from It
Students learn:

How computers “feel” emotions from text using polarity scores.

Basics of sentiment analysis using TextBlob.

Writing clean and safe user input.

Ethical AI concepts — filtering inappropriate content.

🕐 60-Minute Teaching Plan

Time	Activity
0–10 min	Introduce sentiment analysis and emojis
10–25 min	Explain the app logic and TextBlob polarity
25–45 min	Students run and test sentences
45–55 min	Explore “Teacher Mode” diagram
55–60 min	Reflect and discuss what AI can/can’t detect

⚙️ Known Limitations

TextBlob can misinterpret sarcasm or mixed emotions.

Only basic bad-word filtering (can be improved).

Doesn’t detect complex emotions like anger or fear yet.

✍️ References

Streamlit Documentation

TextBlob Documentation

📚 Educational Value
This mini-project introduces students to Natural Language Processing (NLP) and helps them understand that AI doesn’t “feel” emotions — it calculates them!
It promotes responsible, creative, and ethical use of technology.

👤 Author
Sairam Panuku

📧 sairampanuku123@gmail.com

🌐 LinkedIn Profile

🧠 Project: sairam-panuku-mood2emoji





sairam-panuku-mood2emoji/
├─ app.py
├─ requirements.txt
├─ README.md
└─ lesson_plan.pdf
