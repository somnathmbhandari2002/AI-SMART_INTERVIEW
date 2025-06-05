# AI-SMART_INTERVIEW
AI-Smart Interview is an intelligent hiring system that automates resume screening, conducts real-time voice and technical interviews, tracks candidate behavior via webcam, and delivers accurate evaluations—making the recruitment process faster, smarter, and bias-free.

# 🤖 AI-Smart Interview

AI-Smart Interview is an advanced recruitment system that streamlines the entire hiring process using AI technologies. It intelligently screens resumes, conducts real-time voice and technical interviews, monitors candidate behavior via webcam (face and gaze tracking), and automatically evaluates responses to generate final results.

## 🚀 Features

- 📄 Resume Upload and Job Description Matching
  - Extracts and compares key skills using NLP techniques.
  - Shortlists candidates with >60% match.

- 📧 Smart Email Notification
  - Sends personalized emails to shortlisted candidates.
  - Supports interview scheduling with timezone handling.

- 🎙️ One-to-One Voice Interview
  - Live voice interaction using Speech-to-Text and Text-to-Speech.
  - Saves voice recordings and text transcriptions.

- 💻 Technical Round
  - Includes MCQs, fill-in-the-blanks, and code-writing questions.
  - Auto-evaluation of non-coding questions.

- 👁️ Candidate Behavior Tracking
  - Monitors face direction, head tilt, and eye gaze using OpenCV and MediaPipe.
  - Integrates video feed in interview UI.

- 📊 Final Scoring and Report Generation
  - Evaluates candidate performance and sends results via email.

## 🛠️ Tech Stack

- Backend: FastAPI, Python
- Frontend: HTML, CSS, JavaScript
- AI/NLP: spaCy, TF-IDF, Sentence Transformers
- Voice: SpeechRecognition, pyttsx3 / gTTS
- Camera: OpenCV, cvzone, MediaPipe
- Database: MongoDB
- Email: SMTP, Email Scheduler
- Deployment: Uvicorn, Docker (optional)

## 📂 Project Structure

smart-interview/
├── backend/
│ ├── main.py
│ ├── routers/
│ └── utils/
├── frontend/
│ ├── index.html
│ ├── styles.css
│ └── scripts.js
├── models/
├── database/
├── media/
│ ├── recordings/
│ └── screenshots/
├── README.md
└── requirements.txt

bash
Copy
Edit

## ⚙️ Setup Instructions

1. 🔽 Clone the repository
```bash
git clone https://github.com/yourusername/smart-interview.git
cd smart-interview
🧪 Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
📦 Install dependencies

pip install -r requirements.txt
▶️ Start the FastAPI server

uvicorn backend.main:app --reload
🌐 Open frontend
Navigate to frontend/index.html in your browser.

📬 Contact
For questions or collaboration:

Name: Somnath Jogi

Email: somnathjogi20@gmail.com
