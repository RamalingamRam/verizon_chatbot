from anthropic import Anthropic
from typing import List, Dict
import logging
from src.config import settings

class ClaudeChatHandler:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        
    def generate_response(self, query: str, search_results: List[Dict]) -> str:
        try:
            # Construct context from search results
            context = "\n\n".join([
                f"Title: {result['title']}\nContent: {result['snippet']}\nURL: {result['url']}"
                for result in search_results
            ])
            
            # Create prompt for Claude
            prompt = f"""Based on the following Verizon Community information, please answer the user's question.
            If you can't find a relevant answer in the provided context, say so and suggest contacting Verizon support directly.

            User Question: {query}

            Verizon Community Information:
            {context}"""
            
            # Get response from Claude
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=124,
                temperature=0,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            return response.content
            
        except Exception as e:
            logging.error(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error while processing your request. Please try again or contact Verizon support directly."
