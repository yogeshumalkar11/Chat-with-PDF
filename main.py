import streamlit as st
import os
import pickle
from pypdf import PdfReader
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from secret import openapi_key
os.environ["OPENAI_API_KEY"] = openapi_key


def main():
    st.set_page_config(page_title='Chat with PDF', page_icon=None,
                       layout="wide", initial_sidebar_state="auto", menu_items=None)
    st.title("Chat with PDF")
    st.sidebar.title('PDF:')
    pdf = st.sidebar.file_uploader("Upload your PDF", type=['pdf'])
    if pdf:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, length_function=len
        )

        chunks = text_splitter.split_text(text=text)

        if os.path.exists(f"{pdf.name[:-4]}.pkl"):
            with open(f"{pdf.name[:-4]}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
            st.write("Embeddings loaded from disk")
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            store_name = pdf.name[:-4]
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            st.write("Embeddings saved to disk")

        query = st.text_input("Enter your query")
        if query:
            docs = VectorStore.similarity_search(query=query)
            # st.write(docs)
            llm = OpenAI(temperature=0)
            chain = load_qa_chain(llm=llm, chain_type='stuff')
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)


if __name__ == '__main__':
    main()
