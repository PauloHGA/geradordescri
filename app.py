from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Coloque aqui a chave da OpenAI que você copiou no Passo 1
OPENAI_API_KEY = os.getenv('sk-proj-mKQZW4i7GhfpxCqA2ZrZbwDkXfnUQOSwWEDjlZpAMwX6fLIDOjuCW6q0pKU85STsnIhaEXs9IeT3BlbkFJKniga6DotQk8vLqAWf4eqdkyJlxXmDRAnEFyFQH54bZFYijwsc7-N_sIxrmdj6Zzm5KmmpBi0A_OPENAI')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = f"Crie uma descrição magnética para o Instagram sobre o produto {data['name']}, com as características {data['features']}. Os benefícios são {data['benefits']}. O público-alvo é {data['target']}. Inclua emojis, hashtags relevantes e termine com o CTA 'comente quero'."
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json',
    }
    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': prompt}],
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
    description = response.json()['choices'][0]['message']['content']
    
    return jsonify({'description': description})

    

if __name__ == '__main__':
    app.run(port=5000)
    
print("Requisição recebida!")