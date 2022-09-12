from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello sexy"}

#  uvicorn main_api:app --reload