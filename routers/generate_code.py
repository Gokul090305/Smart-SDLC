from fastapi import APIRouter
from pydantic import BaseModel
from services import watsonx_service # Import the refactored watsonx_service

router = APIRouter(prefix="/generate-code", tags=["Code Generator"])

class PromptRequest(BaseModel):
    prompt: str

@router.post("/")
async def generate_code_endpoint(request: PromptRequest):
    # Now calls the generate_code function in watsonx_service
    code = watsonx_service.generate_code(request.prompt)
    return {"code": code}