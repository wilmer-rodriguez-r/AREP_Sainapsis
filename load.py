import os
import pinecone
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pinecone import Pinecone

def main():
    pinecone.init(api_key="27d6859f-2671-4044-97c9-e428d612c5dc",
                  environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_existing_index("sainapsis", embeddings)
    files = ["economia.txt",
             "ingenieria-civil.txt",
             "ingenieria-electrica.txt",
             "ingenieria-electronica.txt",
             "ingenieria-industrial.txt",
             "ingenieria-sistemas.txt"]
    for fileName in files:
        load_index(fileName, embeddings)

def load_index(fileName, embeddings):
    loader = TextLoader(fileName, encoding="utf8")
    documents = loader.load()
    text_splitter = CharacterTextSplitter()
    docs = text_splitter.split_documents(documents)
    docsearch = Pinecone.from_texts([docs[0].page_content], embeddings, index_name='sainapsis')