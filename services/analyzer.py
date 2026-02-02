"""
Resume Analyzer Service
Orchestrates the resume analysis using LLM
"""

from services.llm_service import get_llm
from prompts.analysis_prompts import (
    SYSTEM_PROMPT,
    RESUME_ANALYSIS_PROMPT,
    JOB_MATCH_PROMPT,
    ATS_SCORE_PROMPT
)


def analyze_resume(resume_text: str) -> str:
    """
    Perform a comprehensive analysis of the resume.
    
    Args:
        resume_text: Extracted text from the resume
        
    Returns:
        Detailed analysis from the LLM
    """
    llm = get_llm()
    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)
    return llm.generate_response(prompt, SYSTEM_PROMPT)


def match_with_job(resume_text: str, job_description: str) -> str:
    """
    Compare resume against a job description.
    
    Args:
        resume_text: Extracted text from the resume
        job_description: The job description to match against
        
    Returns:
        Job matching analysis from the LLM
    """
    llm = get_llm()
    prompt = JOB_MATCH_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )
    return llm.generate_response(prompt, SYSTEM_PROMPT)


def calculate_ats_score(resume_text: str) -> str:
    """
    Evaluate resume for ATS compatibility.
    
    Args:
        resume_text: Extracted text from the resume
        
    Returns:
        ATS compatibility analysis from the LLM
    """
    llm = get_llm()
    prompt = ATS_SCORE_PROMPT.format(resume_text=resume_text)
    return llm.generate_response(prompt, SYSTEM_PROMPT)


def full_analysis(resume_text: str, job_description: str = None) -> dict:
    """
    Perform complete analysis including all aspects.
    
    Args:
        resume_text: Extracted text from the resume
        job_description: Optional job description for matching
        
    Returns:
        Dictionary containing all analysis results
    """
    results = {
        "resume_analysis": analyze_resume(resume_text),
        "ats_analysis": calculate_ats_score(resume_text)
    }
    
    if job_description and job_description.strip():
        results["job_match"] = match_with_job(resume_text, job_description)
    
    return results
