from cgitb import handler
from fastapi import FastAPI, HTTPException
from main import generate_branding_snippet, generate_keywords, MAX_INPUT_LENGTH
import os
from mangum import Mangum

app = FastAPI()
handler=Mangum(app)

OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")
# @app.get("/")
# async def root():
#     return {"message": "Hello sexy"}

@app.get("/generate_snippet")
async def generate_snippet_api(prompt:str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt, OPENAI_API_KEY)
    return {"snippet": snippet, "keywords": []}

@app.get("/generate_keywords")
async def generate_keywords_api(prompt:str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt, OPENAI_API_KEY)
    return {"snippet": None, "keywords": keywords}

@app.get("/generate_snippets_and_keywords")
async def generate_keywords_api(prompt:str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt, OPENAI_API_KEY)
    keywords = generate_keywords(prompt, OPENAI_API_KEY)
    return {"snippet": snippet, "keywords": keywords}

def validate_input_length(prompt:str):
    if len(prompt) > MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"Length exceeded and to long. Must be under {prompt}")
    pass

#  uvicorn main_api:app --reload