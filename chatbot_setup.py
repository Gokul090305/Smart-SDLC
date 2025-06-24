from services.watsonx_service import get_watsonx_response

def get_chatbot_response(prompt: str) -> str:
    response = get_watsonx_response(prompt)
    return response