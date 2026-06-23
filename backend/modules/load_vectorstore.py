import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "medical-chatbot-index")
UPLOAD_DIR = "uploaded_docs"

EMBED_DIM = 3072

pc = Pinecone(api_key=PINECONE_API_KEY)

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


def _ensure_index_exists():
    existing_indexes = [idx["name"] for idx in pc.list_indexes()]
    if INDEX_NAME not in existing_indexes:
        pc.create_index(
            name=INDEX_NAME,
            dimension=EMBED_DIM,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )


def load_vectorstore(upload_dir: str = UPLOAD_DIR):
    """
    Loads every PDF in `upload_dir` in a single call. LangChain's
    DirectoryLoader handles walking the folder and tagging each
    resulting chunk's `source` metadata internally, so there's no
    manual file-by-file loop here. Then it splits into chunks, embeds
    them with Google's Gemini embedding model, and upserts everything
    into Pinecone.
    """
    _ensure_index_exists()

    loader = DirectoryLoader(
        upload_dir,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
    )
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(documents)

    vectorstore = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
    return vectorstore


def get_vectorstore():
    """Returns a handle to the existing Pinecone index, for querying."""
    _ensure_index_exists()
    return PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)