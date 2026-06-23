from typing import List
import shutil
from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("uploaded_docs")
UPLOAD_DIR.mkdir(exist_ok=True)


def save_uploaded_pdfs(files: List[UploadFile]) -> List[str]:
    """
    Validates and saves uploaded PDF files to the uploaded_docs/ folder.
    Returns the list of saved file paths.
    """
    saved_paths = []

    for file in files:
        if not file.filename.lower().endswith(".pdf"):
            raise ValueError(f"{file.filename} is not a PDF file")

        destination = UPLOAD_DIR / file.filename
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved_paths.append(str(destination))

    return saved_paths