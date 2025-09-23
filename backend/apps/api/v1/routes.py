from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ...models.inference import generate_text

router = APIRouter()
templates = Jinja2Templates(directory="backend/static")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, prompt: str = Form(...)):
    response_text = generate_text(prompt)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prompt": prompt, "response": response_text}
    )
