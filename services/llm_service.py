"""
Groq LLM Service
Handles all interactions with the Groq API
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GroqLLM:
    """Groq LLM client for resume analysis."""
    
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in .env file.")
        
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.1-70b-versatile"  # Fast and capable model
    
    def generate_response(self, prompt: str, system_prompt: str = None) -> str:
        """
        Generate a response from the Groq LLM.
        
        Args:
            prompt: The user prompt/question
            system_prompt: Optional system prompt to set context
            
        Returns:
            The LLM's response text
        """
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=0.7,
                max_tokens=2048
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error calling Groq API: {str(e)}")


# Singleton instance for reuse
_llm_instance = None


def get_llm() -> GroqLLM:
    """Get or create the LLM instance."""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = GroqLLM()
    return _llm_instance
