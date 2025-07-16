# Weaviate CLIP models example

🎯 Overview
-----------

This is a simple demo of how one can run Weaviate CLIP vectorizers to index images.

📦 Requirements
----------------

In order to be able to create Weaviate one needs at least:

1. Docker
2. Python3

💡 Running
----------

In order to run the setup one needs to issue:

```sh
docker compose up -d
```

In order to run notebooks, it's advised to setup a venv for a project.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

or using uv:

```sh
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt
```

📖 How to use notebooks
----------

Prior running the examples please run import notebook:

1. Import data: ([0-prepare_data.ipynb](./notebooks/0-prepare_data.ipynb))

Examples:

1. Books CLIP: ([1-books-clip.ipynb](./notebooks/1-books-clip.ipynb))
2. Amazon CLIP: ([2-amazon-clip.ipynb](./notebooks/2-amazon-clip.ipynb))

🔗 Useful links
----------

- [Dataset used in notebooks](https://huggingface.co/datasets/ada-datadruids/books)
- [Vector similarity search](https://weaviate.io/developers/weaviate/search/similarity)
- [Keyword search](https://weaviate.io/developers/weaviate/search/bm25)
- [Hybrid search](https://weaviate.io/developers/weaviate/search/hybrid)
