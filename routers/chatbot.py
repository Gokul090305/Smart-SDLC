from services.watsonx_service import get_watsonx_response

def get_watsonx_response_for_chatbot(prompt: str) -> str:
    return get_watsonx_response(prompt)