from fastapi import APIRouter, Form, HTTPException
from modules.query_handler import query_chain
from logger import logger

router = APIRouter()


@router.post("/ask/")
async def ask_question(question: str = Form(...)):
    """
    Accepts a question (as a form field) and returns an answer generated
    from the most relevant chunks stored in Pinecone.
    """
    try:
        result = query_chain(question)
        logger.info(f"Answered question: {question}")
        return result
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to answer question")