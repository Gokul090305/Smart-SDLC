from fastapi import APIRouter, UploadFile
from services import pdf_reader, watsonx_service

router = APIRouter(prefix="/classify", tags=["Requirement Classification"])

@router.post("/")
async def classify_requirements(file: UploadFile):
    content = await pdf_reader.extract_text_from_pdf(file)
    # Now calls the classify_requirements function in watsonx_service
    classification = watsonx_service.classify_requirements(content)
    return {"phases": classification}