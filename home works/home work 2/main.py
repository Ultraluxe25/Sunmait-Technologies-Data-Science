from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")


class TextRequest(BaseModel):
    text: str


@app.get("/ping")
async def ping():
    return {"message": "200 OK"}


@app.post("/predict")
async def predict(request: TextRequest):
    try:
        sentiment = sentiment_analyzer(request.text)
        return {"sentiment": sentiment[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the sentiment analysis API!"} 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    