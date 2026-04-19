

# ------------ Old code -----------------------

from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

# Initialize model and ChromaDB client
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()

# client = chromadb.Client(
#     Settings(
#         persist_directory="vectordb"
#     )
# )
                     
collection_name = "healthapp_docs"

# collection = client.get_or_create_collection(
#     name="healthapp_docs"
# )

if collection_name not in [c.name for c in client.list_collections()]:
    collection = client.create_collection(name=collection_name)
else:
    collection = client.get_collection(name=collection_name)

def extract_class_name(text):
    """
    Extract class name from text.
    Assumes class names are UPPERCASE and short.
    """
    for line in text.split("\n"):
        line = line.strip()
        if line.isupper() and 3 < len(line) < 40:
            return line
    return "UNKNOWN"


#     first one 
def embed_and_store_with_page(filename, chunks_with_page):
    """
    chunks_with_page = list of tuples: (chunk_text, page_number)
    """
    for i, (chunk, page_num) in enumerate(chunks_with_page):
        embedding = model.encode(chunk).tolist()
        collection.add(
            ids=[f"{filename}_{i}"],
            metadatas=[{"filename": filename, "chunk_index": i, "page": page_num}],
            documents=[chunk],
            embeddings=[embedding]
        )   

# client.persist()