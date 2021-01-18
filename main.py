"""
https://fastapi.tiangolo.com/advanced/custom-response/#html-response
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Simple HTML app</title>
        </head>
        <body>
            <h1>Hello world HTML!</h1>
        </body>
    </html>
    """
