# simple-fastAPI-webapp
Use fastAPI to generate html web app. The app will serve a local directory or S3 location of images. Docker, python and fastAPI are the core technologies

## Development
_ `python3.7 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
- `uvicorn main:app --reload`

## References
- https://github.com/robmarkcole/text-insights-app/tree/master/tesseract-engine -> fastAPI in docker
- https://fastapi.tiangolo.com/advanced/custom-response/ -> fastAPI HTML docs
- https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/ article and [code](https://github.com/eugeneyan/fastapi-html)
- https://haltakov.net/simple-photo-gallery/ -> flask app for serving image thumbnails as html app
- [File Management with AWS S3, Python, and Flask](https://stackabuse.com/file-management-with-aws-s3-python-and-flask/)
