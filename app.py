from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

#test commit
text:str = "What is Text Summarization?"

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    


@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    



if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

    
