from qdrant_client import QdrantClient, models

qd_client = QdrantClient(url="http://loalhost:6333")

qd_client.create_collection(
    collection_name="note_embeddings",
    vectors_config={
        "jinaai/jina-embeddings-v3": models.VectorParams(
            size=4, distance=models.Distance.COSINE
        ),
    },
    sparse_vectors_config={"bm25": models.SparseVectorParams()},
)
