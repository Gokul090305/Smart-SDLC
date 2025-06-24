import fitz  # from PyMuPDF


async def extract_text_from_pdf(file):
    pdf = fitz.open(stream=await file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in pdf)
    return text
