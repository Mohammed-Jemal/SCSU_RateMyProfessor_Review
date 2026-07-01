import chromadb
from chromadb.utils import embedding_functions
from load_and_chunk import chunk_txt, load_and_clean_docs
import os

def vector_db(chunks, db_path= "./chroma_db"):
    client= chromadb.PersistentClient(path=db_path)
    
    embedding_func= embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    
    #create collections
    collection= client.get_or_create_collection(
        name='ratemyprof_review',
        embedding_function=embedding_func
    )
    ids= []
    documents= []
    metadata= []
    
    for i, chunk in enumerate(chunks):
        ids.append(f"chunk_{i}")
        documents.append(chunk['text'])
        metadata.append(chunk['metadata'])
        
        #Add the elements to the vector store
        print(f"Adding {len(documents)} chunks to db")
        
        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadata
        )
        print("Successfully indexed all the chunks into chromadb")
    return collection
def retrive_context(query,collection, k=5):
    #quiring the top k semantically relivant chunks
    result= collection.query(
        query_text=[query],
        n_results=k
    )
    return result
if __name__=="__main__":
    #load data
    data= "raw_data"
    docs= load_and_clean_docs(data_dir=data)
    chunks= chunk_txt(docs, chunk_size=300, overlap=50)   
    
    #Load the vector stor
    collection= vector_db(chunks=chunks)
    #Test the retrival with the target query
    test_query= "what does students say about professor Hossain exam or assignment?"
    print(f"This is the retrieval testing query:\n {test_query}")    
    print("*"*50) 
    
    hits= retrive_context(test_query, collection=collection, k=5)
    
    #print the retrivied chunk and similarity score
    for idx in range(len(hits['documents'][0])):
        doc_txt = hits['documents'][0][idx]
        metadata = hits['metadatas'][0][idx]
        distance = hits['distances'][0][idx]

        print(f"match #{idx} | distance: {distance:.4f} | source: {metadata.get('source','unknown')}")
        print(f"Context: \"{doc_txt}\"")
        print("♪"*50)
        
        
    
