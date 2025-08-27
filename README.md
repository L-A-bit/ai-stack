# ai-stack (OSAID compliant)

Este proyecto es una estructura mínima para experimentar y aprender a utilizar IA de manera independiente, siguiendo principios de Open Source AI Development (OSAID).

## Estructura
- `fastapi-app/`: API principal para interactuar con modelos y embeddings.
- `config/`: Variables de entorno y configuración.
- `docker-compose.yml`: Orquestación de servicios (API, LLM, Qdrant).
- `README.md`: Documentación y guía de uso.

## Servicios
- **FastAPI**: API REST para pruebas y desarrollo.
- **Qdrant**: Motor de vectores para embeddings y búsquedas semánticas.
- **LLM**: Modelo de lenguaje grande (ejemplo: Mistral-7B).

## Uso
1. Clona el repositorio y coloca tu modelo en la carpeta `models/`.
2. Ejecuta `docker-compose up` para iniciar todos los servicios.
3. Accede a la API en `http://localhost:8000`.

## Ejemplo de endpoints
- `/`: Estado del stack.
- `/chat`: (por implementar) Interacción con el LLM.
- `/embed`: (por implementar) Generación y consulta de embeddings.

## Recursos
- [OSAID Principles](https://osaid.org)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Qdrant](https://qdrant.tech/)
- [vLLM](https://vllm.ai/)

---
¡Listo para experimentar con IA de forma abierta y local!
