from fastapi import FastAPI
import requests
import json

app = FastAPI()

# URLs para Ollama (más simple) y Qdrant
OLLAMA_URL = "http://ollama:11434"
QDRANT_URL = "http://qdrant:6333"

@app.get("/")
def root():
    return {"status": "ok", "message": "AI stack OSAID corriendo 🚀", "services": ["ollama", "qdrant"]}

@app.post("/chat")
async def chat(message: dict):
    """
    Endpoint para chat con modelo OSAID via Ollama
    Ejemplo: {"prompt": "¿Qué es OSAID?"}
    """
    try:
        payload = {
            "model": "llama2",  # Modelo OSAID
            "prompt": message.get("prompt", "Hola"),
            "stream": False
        }
        
        response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)
        if response.status_code == 200:
            return {"response": response.json().get("response", "Sin respuesta")}
        else:
            return {"error": "Modelo no disponible. Ejecuta: docker exec -it ai-stack-ollama-1 ollama pull llama2"}
            
    except Exception as e:
        return {"error": f"Error conectando con Ollama: {str(e)}"}

@app.get("/models")
async def list_models():
    """Listar modelos disponibles en Ollama"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        if response.status_code == 200:
            return response.json()
        else:
            return {"models": [], "note": "Ejecuta: docker exec -it ai-stack-ollama-1 ollama pull llama2"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

# Endpoint para embeddings (por implementar con Qdrant)
@app.post("/embed")
async def embed(text: dict):
    return {"message": "Embeddings por implementar", "text": text.get("text", "")}
