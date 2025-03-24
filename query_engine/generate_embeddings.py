import datetime
import shutil
import time
from pathlib import Path

import numpy as np
from transformers import AutoModel


def local_time_now() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")


def embed_full_notes_jina_embeddings_v3(
    embed_task: str,  # e.g. "retrieval.query" - refer to https://huggingface.co/jinaai/jina-embeddings-v3
) -> None:
    """
    Embed all notes and export the embeddings to flat files in
    /generated_embeddings/jina_embeddings_v3/
    """
    output_dir: Path = Path(
        f"./generated_embeddings/jina_embeddings_v3/task_{embed_task.replace(".","")}/"
    )
    shutil.rmtree(output_dir, ignore_errors=True)
    # load embedding model #
    model = AutoModel.from_pretrained(
        Path("../../models/language_embedding_models/jina-embeddings-v3-2024-11-06"),
        local_files_only=True,
        trust_remote_code=True,
    )
    # read in all notes into RAM #
    doc_file_paths: list[Path] = []
    doc_texts: list[str] = []
    for doc_filepath in Path("./obsidian-vault").rglob("*.md"):
        doc_file_paths.append(doc_filepath)
        with open(doc_filepath, "r", encoding="utf-8") as file:
            doc_texts.append(file.read())
    print(
        local_time_now(),
        f"loaded {len(doc_texts):,} notes",
    )
    # generate all embeddings #
    embeddings: list[np.ndarray] = []
    print(
        local_time_now(),
        "started generating embeddings",
    )
    start_time: float = time.perf_counter()
    for doc_num, doc_text in enumerate(doc_texts, start=1):
        embeddings.append(model.encode([doc_text], task="retrieval.passage")[0])
        print(
            local_time_now(),
            f"finished {doc_num:,}/{len(doc_texts):,}",
            end="\r",
        )
    end_time: float = time.perf_counter()
    print(
        local_time_now(),
        f"finished generating {len(embeddings):,} embeddings in {(end_time-start_time)/60:,.2f} minutes",
        f"\n({(end_time-start_time)/len(embeddings):,.1f} seconds per document)",
    )
    print(
        local_time_now(),
        f"exporting embeddings to file at {output_dir}",
    )
    for input_filepath, np_array in zip(doc_file_paths, embeddings):
        output_filepath: Path = (
            output_dir / Path(*input_filepath.parts[1:])
        ).with_suffix(".npy")
        output_filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(output_filepath, "wb") as file:
            np.save(file, np_array)


def generate_all_embeddings() -> None:
    """
    Sequentially run all available embedding models
    for all notes
    """
    print(
        local_time_now(),
        "Generating embeddings for all notes (all available embedding methods)",
        "\n(existing embeddings will be deleted)",
    )
    print(
        local_time_now(),
        "Generating jinaai/jina-embeddings-v3 ? task='retrieval.passage'",
    )
    embed_full_notes_jina_embeddings_v3(embed_task="retrieval.passage")
    print(
        local_time_now(),
        "Finished jinaai/jina-embeddings-v3 ? task='retrieval.passage'",
    )


if __name__ == "__main__":
    generate_all_embeddings()
