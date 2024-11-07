"""The CLI entry script for the query engine"""

import argparse

available_embedding_methods: tuple[str, ...] = (
    "bm25",
    "semantic_embedding",
)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-e",
    "--embedding_method",
    help=f"The algorithm used to convert text documents into dense embedding vectors. Current options are: {{{', '.join(available_embedding_methods)}}}",
    required=True,
)
arg_parser.add_argument(
    "-q",
    "--query",
    help="The search query",
    required=True,
)
arg_parser.add_argument(
    "-w",
    "--rewrite_query",
    help="if included, LLM will reword the user query before performing the retrieval step",
    action="store_true",
)
args = arg_parser.parse_args()

if args.embedding_method not in available_embedding_methods:
    raise ValueError(
        f"'{args.embedding_method}' is not a supported embedding_method. Current options are: {{{', '.join(available_embedding_methods)}}}"
    )
