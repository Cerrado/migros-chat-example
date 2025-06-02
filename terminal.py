# Outside ChatBot() class
from main import ChatBot


bot = ChatBot()
input = input("Ask me anything: ")
result = bot.rag_chain.invoke(input)
print(result)