from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.scraper import VerizonScraper
from src.chat_handler import ClaudeChatHandler
from src.utils import setup_logging
import logging

app = FastAPI()
setup_logging()

class Query(BaseModel):
    text: str

@app.post("/chat")
async def chat_endpoint(query: Query):
    try:
        # Initialize components
        scraper = VerizonScraper()
        chat_handler = ClaudeChatHandler()
        
        # Search Verizon community
        search_results = scraper.search_community(query.text)
        
        if not search_results:
            return {
                "response": "I couldn't find any relevant information in the Verizon Community. Please try rephrasing your question or contact Verizon support directly."
            }
        
        # Generate response using Claude
        response = chat_handler.generate_response(query.text, search_results)
        
        return {"response": response}
        
    except Exception as e:
        logging.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)