import os

def load_and_clean_docs(data_dir):
    
    document=[]
    
    if not os.path.exists(data_dir):
        print("File is not found")
        return document
    
    for file_name in os.listdir(data_dir):
        if file_name.endswith(".txt"):
            file_path= os.path.join(data_dir, file_name)
            
            #clean the file
            with open(file_path,'r', encoding='utf-8') as f:
                raw_txt= f.read()
                
                #remove space
                clean_txt= " ".join(raw_txt.split())
                document.append({
                    'source':file_name,
                    'text':clean_txt}
                )               
        
        
    return document
def chunk_txt(document, chunk_size= 300, overlap= 50):
    chunks=[]
    
    for doc in document:
        text= doc['text']
        source= doc['source']
        
        start=0
        if len(text)==chunk_size:
            chunks.append({
                'text':text,
                'metadata':{'source': source, 'chunk_index':0}
            })
            continue
        chunk_index=0
        while start < len(text):
            end= start + chunk_size
            chunk_text= text[start:end]
            
            chunks.append({
                'text':chunk_text,
                'metadata':{'source':source, 'chunk_index':chunk_index}
            })
            start+=(chunk_size-overlap)
            chunk_index+=1
        
            if start>=len(text)-overlap:  #check indentation
                break
            
    return chunks        
    

if __name__=="__main__":
    #loading data
    data_dir= 'raw_data'
    docs=load_and_clean_docs(data_dir)
    print(f"Successfully loaded {len(docs)} files")
    print("="*50)
    All_chunks= chunk_txt(docs, chunk_size=300,overlap=50)
    print(f"The total number of chunks are {len(All_chunks)}")
    
    #lets see some chunks
    print("_"*50)
    for i,chunk in enumerate(All_chunks[:3]):
        print(f"chunk#{i+1}|source:{chunk['metadata']['source']}|index:{chunk['metadata']['chunk_index']}")
        print(f"contents: {chunk['text']}")
        print("."*50)
        
    

