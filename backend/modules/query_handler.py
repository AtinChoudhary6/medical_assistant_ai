from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from modules.llm import get_llm
from modules.load_vectorstore import get_vectorstore

PROMPT = ChatPromptTemplate.from_template(
    "You are a medical assistant. Use the context below to answer the "
    "question. If the answer isn't in the context, say you don't know.\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}\n"
    "Answer:"
)


def _format_docs(docs) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


def query_chain(question: str):
    """
    Retrieves relevant chunks from Pinecone, then pipes them through the
    prompt and LLM using LCEL (the `|` operator). LCEL lives in
    langchain-core and is the current, stable way to build chains —
    legacy classes like RetrievalQA were moved out of `langchain.chains`
    into the separate `langchain-classic` package in LangChain v1.
    """
    llm = get_llm()
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    docs = retriever.invoke(question)
    context = _format_docs(docs)

    chain = PROMPT | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": question})

    sources = sorted({doc.metadata.get("source", "unknown") for doc in docs})

    return {
        "answer": answer,
        "sources": sources,
    }
