# 📊 Resume Analyzer

An AI-powered Resume/CV Analyzer that helps job seekers improve their resumes using **Groq LLM** (Llama 3.1 70B) and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![Groq](https://img.shields.io/badge/Groq-LLM-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **📄 Resume Upload** - Support for PDF and DOCX formats
- **📊 Resume Analysis** - Comprehensive feedback on strengths and weaknesses
- **🤖 ATS Score** - Check compatibility with Applicant Tracking Systems
- **🎯 Job Match** - Compare resume against specific job descriptions
- **💡 Improvement Suggestions** - Actionable recommendations to enhance your resume

## 🖥️ Demo

Upload your resume and get instant AI-powered feedback!

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A free [Groq API Key](https://console.groq.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MuhammadAkmal03/Resume-Analyzer.git
   cd Resume-Analyzer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your Groq API key
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   - The app will open automatically at `http://localhost:8501`

## 📁 Project Structure

```
resume-analyzer/
├── app.py                    # Main Streamlit application
├── services/
│   ├── __init__.py
│   ├── resume_parser.py      # PDF/DOCX text extraction
│   ├── llm_service.py        # Groq API integration
│   └── analyzer.py           # Analysis orchestration
├── prompts/
│   ├── __init__.py
│   └── analysis_prompts.py   # LLM prompts
├── utils/
│   └── __init__.py
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore
└── README.md
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com/) | ✅ Yes |

### Getting a Groq API Key

1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

## 📖 How to Use

1. **Upload Resume** - Click "Browse files" and select your PDF or DOCX resume
2. **Add Job Description** (Optional) - Paste the job description for targeted feedback
3. **Click Analyze** - Get instant AI-powered analysis
4. **Review Results** - Check the tabs for different types of analysis:
   - 📊 **Resume Analysis** - Overall quality and suggestions
   - 🤖 **ATS Score** - Applicant Tracking System compatibility
   - 🎯 **Job Match** - How well you match the job requirements

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **Groq** | LLM API (Llama 3.1 70B) |
| **PyPDF2** | PDF text extraction |
| **python-docx** | DOCX text extraction |
| **python-dotenv** | Environment variable management |

## 🚢 Deployment

### Deploy to Streamlit Community Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Add `GROQ_API_KEY` in the Secrets section:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
5. Deploy!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Muhammad Akmal**

- GitHub: [@MuhammadAkmal03](https://github.com/MuhammadAkmal03)

---

⭐ Star this repo if you found it helpful!
