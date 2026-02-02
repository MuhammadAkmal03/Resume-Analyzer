"""
Analysis Prompts
Contains all LLM prompts for resume analysis
"""

SYSTEM_PROMPT = """You are an expert HR consultant and career coach with 15+ years of experience 
in resume writing, talent acquisition, and career development. You provide detailed, actionable 
feedback to help candidates improve their resumes and increase their chances of getting hired."""


RESUME_ANALYSIS_PROMPT = """Analyze the following resume and provide a comprehensive evaluation.

RESUME:
{resume_text}

Please provide your analysis in the following format:

## 📊 Overall Score: [X/100]

## 📋 Summary
[Brief 2-3 sentence summary of the resume's strengths and weaknesses]

## ✅ Strengths
- [List 3-5 key strengths]

## ⚠️ Areas for Improvement
- [List 3-5 areas that need work]

## 💡 Specific Recommendations
1. [Actionable recommendation 1]
2. [Actionable recommendation 2]
3. [Actionable recommendation 3]
4. [Actionable recommendation 4]
5. [Actionable recommendation 5]

## 📝 Section-by-Section Feedback

### Contact Information
[Feedback on contact details]

### Professional Summary/Objective
[Feedback on summary section]

### Work Experience
[Feedback on experience section]

### Education
[Feedback on education section]

### Skills
[Feedback on skills section]

Be specific, constructive, and provide examples where possible."""


JOB_MATCH_PROMPT = """Compare the following resume against the job description and provide a detailed matching analysis.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Please provide your analysis in the following format:

## 🎯 Match Score: [X/100]

## 📋 Match Summary
[2-3 sentences summarizing how well the candidate fits the role]

## ✅ Matching Qualifications
- [List skills/experience that match the job requirements]

## ❌ Missing Qualifications
- [List required skills/experience that are missing from the resume]

## 🔑 Keywords Analysis

### Keywords Found in Resume:
- [List matching keywords]

### Keywords to Add:
- [List important keywords from job description missing in resume]

## 💡 Recommendations to Improve Match
1. [Specific action to improve match]
2. [Specific action to improve match]
3. [Specific action to improve match]

## 📝 Suggested Resume Modifications
[Specific suggestions on how to tailor the resume for this job]"""


ATS_SCORE_PROMPT = """Evaluate the following resume for ATS (Applicant Tracking System) compatibility.

RESUME:
{resume_text}

Please analyze and provide:

## 🤖 ATS Compatibility Score: [X/100]

## 📋 ATS Summary
[Brief explanation of how well this resume will perform with ATS systems]

## ✅ ATS-Friendly Elements
- [List elements that work well with ATS]

## ⚠️ Potential ATS Issues
- [List elements that might cause problems with ATS]

## 📝 Format Recommendations
1. [Formatting suggestion for better ATS compatibility]
2. [Formatting suggestion for better ATS compatibility]
3. [Formatting suggestion for better ATS compatibility]

## 🔑 Keyword Optimization
- [Suggestions for keyword optimization]

## 💡 Quick Fixes
- [Immediate changes to improve ATS score]

Note: ATS systems scan resumes for keywords, proper formatting, and standard section headers. 
Avoid tables, graphics, headers/footers, and unusual fonts."""
