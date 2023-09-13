# Python Image extract from image
extract text from an image using Python and Tesseract

## Why do we need this repo as public
I observed that many individuals working in data entry jobs often have to manually type text from images, which can be quite time-consuming.
As a result, I made the decision to create a repository that simplifies the process, allowing them to easily extract text from images and arrange it in documents.

I have also included comprehensive documentation to guide users through running the code on their local machines, even if they don't have a background in coding. This resource is designed to be highly beneficial.

## required environment
- Python 3.x.x
  Download in [here](https://www.python.org/downloads/)
- Install tesseract
  You can install tesseract in [here](https://tesseract-ocr.github.io/tessdoc/) on your OS
    

## set virtual env with python
### Linux OS

```sh    
python3 -m venv venv
source ./venv/bin/activate
```

### Windows OS

```sh
python3 -m venv venv
cd venv/Scripts && activate && cd .. && cd ..
```

## run command
- confirm tesseract exe path on your OS
```sh
python3 main.py
```