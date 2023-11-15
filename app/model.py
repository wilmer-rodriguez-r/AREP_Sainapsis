# This is a sample Python script.
import pinecone
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.vectorstores.pinecone import Pinecone

@tool("SayHello", return_direct=True)
def say_hello(name:str) -> str:
    """Answer when someone says hello"""
    return f'Hello {name}' 

@tool("Search", return_direct=True)
def search(query:str) -> str:
    """Answer when someone makes a query"""
    pinecone.init(api_key="27d6859f-2671-4044-97c9-e428d612c5dc",
                  environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("sainapsis", embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine", retriever=docsearch.as_retriever(search_type="similarity"))
    query = "Cuantos años de acreditación tiene ingeniría industrial?"
    print(qa.run(query))

# Press the green button in the gutter to run the script.
def execute(query:str) -> str:
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello,
        search
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True)

    print(agent.run(query))

