import chromadb
from chromadb.utils import embedding_functions

def index_treaty_for_rag(treaty_id, text_content):
    """
    Indexes legal text into ChromaDB for the AI Insight Layer.
    This allows the 'Compass' to provide conversational legal citations.
    """
    client = chromadb.HttpClient(host='localhost', port=8000)
    
    # Using OpenAI or HuggingFace for embeddings
    emb_fn = embedding_functions.DefaultEmbeddingFunction()
    collection = client.get_or_create_collection(
        name="global_tax_laws", 
        embedding_function=emb_fn
    )

    collection.add(
        documents=[text_content],
        metadatas=[{"treaty_id": treaty_id}],
        ids=[f"id_{treaty_id}"]
    )
    print(f"Vectorized treaty {treaty_id} for AI retrieval.")

if __name__ == "__main__":
    # index_treaty_for_rag(101, "The term 'resident' of a Contracting State means...")
    pass