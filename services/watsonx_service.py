from ibm_watsonx_ai.foundation_models import Model
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("4SP6wd9s3g9X8xTCmLFeS4wAK3B7IkGSdnHAVUv-zZBV")
PROJECT_ID = os.getenv("dd0677da-e94c-4810-b931-686e82428b16")
URL = os.getenv("https://us-south.ml.cloud.ibm.com")

model = Model(
    model_id="granite-13b-chat-v2",
    credentials={"apikey": API_KEY, "url": URL},
    project_id=PROJECT_ID,
)

def get_watsonx_response(prompt: str) -> str:
    response = model.generate(prompt=prompt)
    return response.get("results", [{}])[0].get("generated_text", "No response")

def generate_code(prompt: str) -> str:
    return get_watsonx_response(f"Write Python code to do the following:\n{prompt}")

def fix_bug(code: str) -> str:
    return get_watsonx_response(f"Fix bugs in the following code:\n{code}")

def generate_test_case(code: str) -> str:
    return get_watsonx_response(f"Write unit test cases for the following code:\n{code}")

def summarize_code(code: str) -> str:
    return get_watsonx_response(f"Summarize what this code does:\n{code}")

def classify_requirements(text: str) -> dict:
    response = get_watsonx_response(
        f"Classify the following requirements into SDLC phases like Requirements, Testing, Deployment:\n{text}"
    )
    # You can improve this parsing logic later
    return {"Raw Output": response}
