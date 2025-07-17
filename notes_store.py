import chromadb
from embedder import get_embedding

client = chromadb.Client()
collection = client.get_or_create_collection("notes")

def store_note(summary, full_text):
    embedding = get_embedding(summary)
    collection.add(documents=[full_text], embeddings=[embedding], metadatas=[{"summary": summary}])

def query_notes(query, top_k=3):
    embedding = get_embedding(query)
    results = collection.query(query_embeddings=[embedding], n_results=top_k)
    return list(zip(results["documents"][0], results["distances"][0]))
