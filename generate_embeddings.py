import os
import chromadb
import ollama
from pathlib import Path
from os.path import isfile, join
from unstructured.partition.pdf import partition_pdf

client = chromadb.PersistentClient(path="./embeddings.sql")
collection = client.create_collection(name="docs")

dir_path = os.path.dirname(os.path.realpath(__file__))

# Output directory just used so you can inspect what text snippets have been entered into the db
ouput_dir = os.path.join(dir_path, 'output')
if not os.path.exists(ouput_dir):
    os.mkdir(ouput_dir)

# Loop through each document inside /docs
docs_dir = os.path.join(dir_path, 'docs')
pdf_files = [f for f in os.listdir(docs_dir) if isfile(join(docs_dir, f))]
for file in pdf_files:
    print(f'Processing: {file}')
    elements = partition_pdf(filename=join(docs_dir, file))

    # Think there'll be a better way of doing this
    extracted_text = [t.text for t in elements if t.__class__.__name__ == 'NarrativeText']
    print(f'{len(extracted_text)} to add...')

    text_file = f'{Path(file).stem}'
    with open(join(ouput_dir, text_file), 'w') as f:
        f.writelines([f'{l.strip()}\n\n' for l in extracted_text])

    # Add all the text snippets into the embedding db
    for i, d in enumerate(extracted_text):
        response = ollama.embeddings(model="all-minilm", prompt=d)
        embedding = response["embedding"]
        collection.add(
            ids=[f'{file}{i}'],
            embeddings=[embedding],
            documents=[d]
        )
        print(f'Added {i}/{len(extracted_text)}')

    

