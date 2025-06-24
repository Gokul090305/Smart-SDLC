from services.watsonx_service import get_watsonx_response # Import from services folder

def get_chat_response(prompt: str):
    return get_watsonx_response(prompt)