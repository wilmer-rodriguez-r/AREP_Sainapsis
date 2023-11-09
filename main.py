# This is a sample Python script.
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
@tool("SayHello", return_direct=True)
def say_hello(name:str) -> str:
    """Answer when someone says hello"""
    # Use a breakpoint in the code line below to debug your script.
    return f'Hello {name}'  # Press Ctrl+F8 to toggle the breakpoint.

@tool("SayPuto", return_direct=True)
def say_puto(name:str) -> str:
    """Answer when someone says bye"""
    # Use a breakpoint in the code line below to debug your script.
    return f'Puto {name}'  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello,
        say_puto
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True)

    print(agent.run("Hello my name is Wilmer"))

if __name__ == "__main__":
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
