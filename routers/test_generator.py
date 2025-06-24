from services.watsonx_service import generate_test_case # Import the specific function

def generate_test_cases(code: str) -> str:
    # Directly use the generate_test_case function
    test_code = generate_test_case(code)
    return test_code