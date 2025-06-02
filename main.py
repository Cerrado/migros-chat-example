from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface.llms.huggingface_endpoint import HuggingFaceEndpoint
from pinecone import Pinecone, ServerlessSpec
import pinecone
from dotenv import load_dotenv
import os

class ChatBot():
  load_dotenv()
  loader = TextLoader('./eistee.json')
  documents = loader.load()
  text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=4)
  docs = text_splitter.split_documents(documents)

  embeddings = HuggingFaceEmbeddings()

  pc = Pinecone(
      api_key= os.getenv('PINECONE_API_KEY'),
  )

  index_name = "migros-demo"

  if not pc.has_index(index_name):
    pc.create_index(name=index_name, metric="cosine", dimension=768, spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ))
    docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)
  else:
    docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)

  repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
  llm = HuggingFaceEndpoint(
      repo_id=repo_id,
      temperature=0.8,
      top_k= 50,
      top_p=0.8,
      huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY')
  )

  from langchain import PromptTemplate

  template = """
  You are a hilarious Migros Sales Assistant with a flair for comedy! Your job is to enthusiastically promote Migros products 
  while making customers laugh. Use the following product information to answer questions in a funny, engaging way.
  
  Always include a humorous pitch or joke about the product, and end with a ridiculous reason why they should buy it immediately.
  Keep your response short.
  Add the product information in the response. Print it in a list format.

  Product Information: {context}
  Customer Question: {question}
  """

  prompt = PromptTemplate(template=template, input_variables=["context", "question"])

  from langchain.schema.runnable import RunnablePassthrough
  from langchain.schema.output_parser import StrOutputParser

  rag_chain = (
    {"context": docsearch.as_retriever(),  "question": RunnablePassthrough()} 
    | prompt 
    | llm
    | StrOutputParser() 
  )