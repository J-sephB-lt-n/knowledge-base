import time
from pathlib import Path

import numpy as np
from transformers import AutoModel


def embed_full_notes_jina_embeddings_v3(output_dir: str | Path) -> None:
    """
    Embed all notes and export the embeddings to flat files in
    `output_dir`
    """
    model = AutoModel.from_pretrained(
        Path("../../models/language_embedding_models/jina-embeddings-v3-2024-11-06"),
        local_files_only=True,
        trust_remote_code=True,
    )
    doc_file_paths: list[Path] = []
    doc_texts: list[str] = []
    for doc_filepath in Path("./obsidian-vault").rglob("*.md"):
        doc_file_paths.append(doc_filepath)
        with open(doc_filepath, "r", encoding="utf-8") as file:
            doc_texts.append(file.read())
    print(f"loaded {len(doc_texts):,} notes")
    embeddings: list[np.ndarray] = []
    print("started generating embeddings")
    start_time: float = time.perf_counter()
    for doc_num, doc_text in enumerate(doc_texts, start=1):
        embeddings.append(model.encode([doc_text], task="retrieval.passage")[0])
        print(f"finished {doc_num:,}/{len(doc_texts):,}")
    end_time: float = time.perf_counter()
    print(
        f"finished generating {len(embeddings):,} embeddings in {(end_time-start_time)/60:,.2f} minutes"
        f"\n({(end_time-start_time)/len(embeddings):,.1f} seconds per document)"
    )
