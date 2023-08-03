from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ChatVectorDBChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


class CVGPT:
    """
    CVGPT class is responsible for querying a GPT model with a given PDF document.

    Attributes:
        pdf_path (str): Path to the PDF document.
        model_name (str): Name of the GPT model to use.
        temperature (float): Temperature parameter for the GPT model.
        chat_history (list): List to keep track of the chat history.
        documents (list): Split and loaded PDF documents.
        vectordb (Chroma): Vector database created from the documents.
        qa (ChatVectorDBChain): Query chain for interacting with the GPT model.
    """

    def __init__(self, pdf_path, model_name, temperature):
        """
        Initializes the CVGPT object with the given PDF path, model name, and temperature.

        Args:
            pdf_path (str): Path to the PDF document.
            model_name (str): Name of the GPT model to use.
            temperature (float): Temperature parameter for the GPT model.
        """
        self.pdf_path = pdf_path
        self.model_name = model_name
        self.temperature = temperature
        self.chat_history = []

        # create emebddings and DB
        self.documents = PyPDFLoader(pdf_path).load_and_split()
        self.vectordb = Chroma.from_documents(documents = self.documents, embedding = OpenAIEmbeddings(), persist_directory='.vectordb/.')
        self.vectordb.persist()
    
        # create the query chain
        self.qa = ChatVectorDBChain.from_llm(OpenAI(temperature=self.temperature, model_name=self.model_name),
            self.vectordb,
            return_source_documents=True)
        
    def query_cvgpt(self, question):
        """
        Queries the GPT model with a given question and appends the result to the chat history.

        Args:
            question (str): The question to query.

        Returns:
            str: The answer to the question.
        """
        result= self.qa({"question":question, "chat_history":self.chat_history})
        self.chat_history.append( (question, result["answer"]) )
        return result['answer']