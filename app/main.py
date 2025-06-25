from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse,  JSONResponse
from fastapi.staticfiles import StaticFiles
import redis
from app import LLM
from huggingface_hub import InferenceClient
from io import BytesIO
import base64

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

client = InferenceClient(
    provider="nebius",
    api_key= "hf_token",      # Replace api key instead of hf_token
)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/prompt")
def receive_prompt(prompt: str = Form(...)):
    obj = LLM.Prompt_extract(prompt)
    r.set(prompt, obj)

    image = client.text_to_image(
    obj,
    model="stabilityai/stable-diffusion-xl-base-1.0",
    )

    buffered = BytesIO()
    image.convert("RGB").save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return {
        "received_prompt": prompt,
        "Extracted prompt": obj,
        "image_data": f"data:image/png;base64,{img_str}"
    }


@app.get("/history")
def get_history():
    keys = r.keys()
    conversation = []
    for i in keys:
        temp = {}
        temp['user'] = str(i)
        temp['bot'] = str(str(r.get(i)))
        conversation.append(temp)
    return JSONResponse(content=conversation)
