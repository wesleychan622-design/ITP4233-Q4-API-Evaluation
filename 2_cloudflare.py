import requests

account_id = "YOUR_CLOUDFLARE_ACCOUNT_ID"
api_token = "YOUR_CLOUDFLARE_API_TOKEN"

url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/meta/llama-3.1-8b-instruct"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {"role": "user", "content": "Explain what god is in two short sentences."}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["result"]["response"])
