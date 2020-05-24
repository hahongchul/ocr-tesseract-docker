# OCR Tesseract Docker
Allows upload of an image for OCR using Tesseract and deployed using Docker.  This uses Flask, a light weight web server framework - but for development purposes only.  

Build and run the Docker image.

```
$ docker build -t ocr-tesseract-docker .
$ docker run -p 5000:5000 ocr-tesseract-docker
```

Now navigate to localhost:5000 and upload an image for processing

## Acknowledgments
This is a fork of https://github.com/ricktorzynski/ocr-tesseract-docker I made a couple of changes, such as dropping openCV and fixing the dockerfile