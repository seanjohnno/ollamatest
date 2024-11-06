import ollama
import chromadb


client = chromadb.PersistentClient(path="./embeddings.sql")
collection = client.get_collection(name="docs")

print('Type "quit" to exit the application.\n')

while True:
  prompt = input("\n\nHow can I help?\n\n").strip()
  if prompt == 'quit':
    print('Chatbot awaaaaay!')
    exit(0)
  else:
    # generate an embedding for the prompt and retrieve the most relevant doc
    response = ollama.embeddings(
      prompt=prompt,
      model="all-minilm"
    )

    # Result count be adjusted here but this will just grab the most releveant snippet supplied during generate_embeddings
    results = collection.query(
      query_embeddings=[response["embedding"]],
      n_results=1
    )
    data = results['documents'][0][0]

    # Pass the snippet to the larger model to use in it's answer
    stream = ollama.generate(
      model="llama3.2",
      prompt=f"Using this data: {data}. Respond to this prompt: {prompt}",
      stream=True
    )

    # Output response
    for chunk in stream:
      print(chunk['response'], end='', sep=' ')

