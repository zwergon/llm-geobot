import requests
 
api_url = 'http://gpu.zwergon.fr/chat/generate'
 
input_text = "bonjour"
 
params = {
    'prompt': input_text,
    'temperature': 0.9,
    "max_new_tokens": 1000,
    'chat_history': [
                    ("répond en français: ", "d'accord je donnerai mes réponses en français")]
}
 
response = requests.post(api_url, json=params)
 
if response.status_code == 200:
    output = response.json()['text']  
    print("Réponse générée:", output)
 
else:
    print("Erreur lors de la requête à l'API:", response.status_code)