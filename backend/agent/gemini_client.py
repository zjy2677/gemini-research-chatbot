from google import genai

from backend.config import get_gemini_api_key


def generate_chat_response(message: str, model: str) -> str:
    clean_message = message.strip()
    clean_model = model.strip()

    if not clean_message:
        raise ValueError("Message is required.")

    if not clean_model:
        raise ValueError("Model is required.")

    client = genai.Client(api_key=get_gemini_api_key())
    response = client.models.generate_content(
        model=clean_model,
        contents=clean_message,
    )

    if not response.text:
        return "Gemini returned an empty response."

    return response.text
