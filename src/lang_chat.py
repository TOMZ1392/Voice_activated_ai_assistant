from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=1,
    # other params...
)





prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a person who carefully analyses the inputs  {input} . Based on that generate outputs in a storytellers style. Question the various aspects and write a new sory.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
input_data="Story of a crab and a snail."
while True:
    print(f"human: {input_data} \n\n")
    res=chain.invoke(
    {
       
        "input": input_data,
    }
    )
    print(f"AI: {res.content}\n\n")
    print("----------------------------------------------------------------------\n")
    input_data=res.content