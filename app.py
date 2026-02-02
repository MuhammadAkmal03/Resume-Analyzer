"""
Resume Analyzer - Streamlit Application
AI-powered resume analysis using Groq LLM
"""

import streamlit as st
from services.resume_parser import parse_resume
from services.analyzer import analyze_resume, match_with_job, calculate_ats_score

# Page configuration
st.set_page_config(
    page_title="Resume Analyzer | AI-Powered",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .upload-section {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #e7f3ff;
        border: 1px solid #b3d7ff;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def main():
    # Header
    st.markdown('<h1 class="main-header">📊 Resume Analyzer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-powered resume analysis to help you land your dream job</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/clouds/200/resume.png", width=150)
        st.markdown("### 📋 How to Use")
        st.markdown("""
        1. **Upload** your resume (PDF or DOCX)
        2. **Optionally** paste a job description
        3. **Click** Analyze to get insights
        4. **Review** the detailed feedback
        """)
        st.markdown("---")
        st.markdown("### 🎯 Features")
        st.markdown("""
        -  Resume Quality Analysis
        -  ATS Compatibility Score
        -  Job Match Analysis
        -  Improvement Suggestions
        """)
        st.markdown("---")
        st.markdown("Made with ❤️ using Groq AI")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📄 Upload Your Resume")
        uploaded_file = st.file_uploader(
            "Choose a PDF or DOCX file",
            type=["pdf", "docx"],
            help="Upload your resume in PDF or DOCX format"
        )
        
        if uploaded_file:
            st.success(f" Uploaded: {uploaded_file.name}")
    
    with col2:
        st.markdown("### 💼 Job Description (Optional)")
        job_description = st.text_area(
            "Paste the job description here",
            height=150,
            placeholder="Paste the job description to get a match analysis...",
            help="Adding a job description enables job matching analysis"
        )
    
    # Analysis section
    st.markdown("---")
    
    if uploaded_file:
        # Analyze button
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            analyze_button = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)
        
        if analyze_button:
            try:
                # Extract text from resume
                with st.spinner("📖 Reading your resume..."):
                    resume_text = parse_resume(uploaded_file)
                
                if not resume_text.strip():
                    st.error("❌ Could not extract text from the resume. Please try a different file.")
                    return
                
                # Show extracted text in expander
                with st.expander("📝 Extracted Resume Text", expanded=False):
                    st.text_area("Resume Content", resume_text, height=200, disabled=True)
                
                # Create tabs for different analyses
                if job_description.strip():
                    tab1, tab2, tab3 = st.tabs(["📊 Resume Analysis", "🤖 ATS Score", "🎯 Job Match"])
                else:
                    tab1, tab2 = st.tabs(["📊 Resume Analysis", "🤖 ATS Score"])
                
                # Tab 1: Resume Analysis
                with tab1:
                    with st.spinner("🔍 Analyzing your resume..."):
                        analysis = analyze_resume(resume_text)
                    st.markdown(analysis)
                
                # Tab 2: ATS Score
                with tab2:
                    with st.spinner("🤖 Checking ATS compatibility..."):
                        ats_analysis = calculate_ats_score(resume_text)
                    st.markdown(ats_analysis)
                
                # Tab 3: Job Match (if job description provided)
                if job_description.strip():
                    with tab3:
                        with st.spinner("🎯 Matching with job description..."):
                            match_analysis = match_with_job(resume_text, job_description)
                        st.markdown(match_analysis)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Make sure your GROQ_API_KEY is set in the .env file")
    else:
        # Placeholder when no file is uploaded
        st.info("👆 Upload your resume to get started!")
        
        # Feature cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
                <h3>📊 Resume Analysis</h3>
                <p>Get detailed feedback on your resume's strengths and weaknesses</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
                <h3>🤖 ATS Score</h3>
                <p>Check how well your resume works with Applicant Tracking Systems</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
                <h3>🎯 Job Match</h3>
                <p>Compare your resume against specific job descriptions</p>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
