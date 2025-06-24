from fastapi import FastAPI, UploadFile, APIRouter
from pydantic import BaseModel
from services.watsonx_service import generate_code
import io

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

app = FastAPI()

# ----------- Services -----------
def extract_text_from_pdf(file_bytes):
    if fitz is None:
        return "PyMuPDF not available in this environment."
    pdf = fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf")
    text = "\n".join(page.get_text() for page in pdf)
    return text

def classify_requirements(text):
    return {"Requirements": ["Login should be secure"], "Testing": ["Verify login works"]}

def generate_code_from_prompt(prompt):
    return generate_code(prompt)

def fix_code_bugs(code):
    return code.replace("bug", "fix")

def generate_test_cases(code):
    return (
        "import unittest\n\n"
        "class TestGenerated(unittest.TestCase):\n"
        "    def test_case(self):\n"
        "        self.assertTrue(True)"
    )

def summarize_code(code):
    return "This code prints a user-provided message."

def get_chatbot_response(prompt):
    return f"Chatbot response to: {prompt}"

# ----------- API Routes -----------
class PromptRequest(BaseModel):
    prompt: str

class CodeRequest(BaseModel):
    code: str

@app.post("/classify")
async def classify(file: UploadFile):
    file_bytes = await file.read()
    text = extract_text_from_pdf(file_bytes)
    return classify_requirements(text)

@app.post("/generate-code")
def generate_code(req: PromptRequest):
    return {"code": generate_code_from_prompt(req.prompt)}

@app.post("/bug-fix")
def bug_fix(req: CodeRequest):
    return {"fixed_code": fix_code_bugs(req.code)}

@app.post("/generate-test")
def test_gen(req: CodeRequest):
    return {"test_code": generate_test_cases(req.code)}

@app.post("/summarize")
def summarize(req: CodeRequest):
    return {"summary": summarize_code(req.code)}

@app.post("/chat")
def chat(req: PromptRequest):
    return {"response": get_chatbot_response(req.prompt)}

@app.get("/")
def root():
    return {"message": "SmartSDLC backend is live."}
