from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload_pdfs import router as upload_router
from routes.ask_question import router as ask_router
from middleware.exception_handlers import global_exception_handler
from logger import logger

app = FastAPI(title="Medical Assistant Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(upload_router)
app.include_router(ask_router)


@app.get("/")
def root():
    return {"status": "Medical Assistant API is running"}


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Medical Assistant server")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# uvicorn main:app --reload --host 0.0.0.0 --port 8000