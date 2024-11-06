# 1. Prerequisites

* Install [Ollama](https://github.com/ollama/ollama/blob/main/README.md#quickstart)
* In your terminal ```ollama pull llama3.2```
* In your terminal ```ollama pull all-minilm```
  * There are other models mentioned [here](https://ollama.com/blog/embedding-models) we could try
* In your terminal ```./createenv.sh``` to grab all the Python deps and initialise the virtual env

# 2. Instructions

## 2.1. Only need to run once

* Create a folder under the project root ```docs```
* Drop your PDFs in there
  * Parsing and embedding takes quite a while so you could always just start with 1 or 2
* Run ```python generate_embeddings.py```
* This should leave you with:
  * An output folder where you see plaintext of what's been inserted in the db (found it useful when debugging)
  * The embedded db; _embeddings.sql_

## 2.2. Prompt

* Run ```python chatbot.py```