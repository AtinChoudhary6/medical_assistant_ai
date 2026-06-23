from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException
from modules.pdf_handler import save_uploaded_pdfs
from modules.load_vectorstore import load_vectorstore
from logger import logger

router = APIRouter()


@router.post("/upload_pdfs/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    """
    Accepts one or more PDF files, saves them to disk, then hands the
    whole uploads folder to LangChain's loader/splitter/embedder
    pipeline in load_vectorstore() — no manual per-file processing here.
    """
    try:
        saved_paths = save_uploaded_pdfs(files)
        load_vectorstore()
        logger.info(f"Uploaded and indexed {len(saved_paths)} file(s)")
        return {
            "message": f"{len(saved_paths)} file(s) processed and indexed successfully",
            "files": saved_paths,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to process PDFs")