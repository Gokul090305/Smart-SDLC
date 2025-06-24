from fastapi import FastAPI
from routers import classify, generate_code, bug_fixer, test_generator, summarizer, chatbot

app = FastAPI(title="SmartSDLC Backend")

# Routers
app.include_router(classify.router)
app.include_router(generate_code.router)
app.include_router(bug_fixer.router)
app.include_router(test_generator.router)
app.include_router(summarizer.router)
app.include_router(chatbot.router)

@app.get("/")
async def root():
    return {"message": "SmartSDLC API running"}
