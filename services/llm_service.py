"""
Groq LLM Service
Handles all interactions with the Groq API using requests library
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GroqLLM:
    """Groq LLM client for resume analysis."""
    
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in .env file.")
        
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.3-70b-versatile"  # Fast and capable model
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
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
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2048
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error calling Groq API: {str(e)}")
        except (KeyError, IndexError) as e:
            raise Exception(f"Error parsing Groq response: {str(e)}")


# Singleton instance for reuse
_llm_instance = None


def get_llm() -> GroqLLM:
    """Get or create the LLM instance."""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = GroqLLM()
    return _llm_instance
