"""
https://fastapi.tiangolo.com/advanced/custom-response/#html-response
"""

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Simple HTML app</title>
        </head>
        <body>
            <h1>Navigate to <a href="http://localhost:8000/form">/form</a></h1>
        </body>
    </html>
    """


@app.get("/form")
def form_post(request: Request):
    result = "Enter your name"
    return templates.TemplateResponse(
        "form.html", context={"request": request, "result": result}
    )


@app.post("/form")
def form_post(request: Request, name: str = Form(...)):
    result = name.capitalize()
    return templates.TemplateResponse(
        "form.html", context={"request": request, "result": result, "name": name}
    )

