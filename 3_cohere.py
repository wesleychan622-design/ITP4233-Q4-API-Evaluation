import cohere

co = cohere.Client(api_key="YOUR_COHERE_API_KEY")

response = co.chat(
    model="command-r-08-2024",
    message="Explain what god is in two short sentences."
)

print(response.text)
