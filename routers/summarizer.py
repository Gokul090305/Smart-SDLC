from services.watsonx_service import summarize_code # Import the specific function

def summarize_code(code: str) -> str:
    # Directly use the summarize_code function
    summary = summarize_code(code)
    return summary