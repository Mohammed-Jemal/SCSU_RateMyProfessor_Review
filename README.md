# SCSU RateMyProfessor Review

A lightweight Python project for ingesting and indexing professor review text files into a semantic vector store using Chroma and Sentence Transformers.

## Project Summary

This repository processes raw professor review documents, cleans and chunks the text, and builds a semantic search index for retrieval. It is designed as a foundation for information retrieval and question-answering applications over review data.

## Key Features

- Loads raw `.txt` review files from `raw_data/`
- Cleans text by normalizing whitespace
- Splits documents into overlapping chunks for semantic indexing
- Builds a vector store using ChromaDB with `all-MiniLM-L6-v2` embeddings
- Performs semantic retrieval of relevant review chunks for a query

## Repository Structure

- `load_and_chunk.py` — loads and cleans review documents, then chunks text for indexing
- `store_and_search.py` — creates a ChromaDB collection, indexes text chunks, and retrieves relevant chunks for a sample query
- `raw_data/` — raw professor review text files used as input
- `chroma_db/` — local persistent Chroma database directory
- `requirement.txt` — Python dependencies list
- `.env` — optional environment variables file (currently empty)

## Setup

1. Clone the repository

```bash
git clone <repo-url>
cd SCSU_RateMyProfessor_Review
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirement.txt
```

## Usage

1. Generate cleaned chunks from raw review files:

```bash
python load_and_chunk.py
```

2. Create the vector index and test semantic retrieval:

```bash
python store_and_search.py
```

3. Update `test_query` in `store_and_search.py` to retrieve relevant review snippets for other questions.

## Dependencies

- `chromadb` — vector database for semantic retrieval
- `sentence-transformers==3.4.1` — embedding model support
- `groq` — optional query utilities
- `python-dotenv` — environment variable support
- `streamlit` — optional UI framework for future interface work
- `openrouter` — optional LLM integration support

## Notes

- The project currently uses local text files and a persistent ChromaDB store.
- The pipeline can be extended to support question answering, Streamlit dashboards, or external LLM-driven summarization.
- `chroma_db/` contains the indexed vector store and can be recreated by rerunning `store_and_search.py`.

* *In the retrieval step, lower distance values indicates a closer semantic match between the query and the retrieved text chunk, while higher values indicates a weak/no match in from the chroma_db chunks.
