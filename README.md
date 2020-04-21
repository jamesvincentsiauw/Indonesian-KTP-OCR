# Indonesian Citizen ID Card - Optical Character Recognition
### How to run

```bash
# install tesseract 
for Windows: https://github.com/UB-Mannheim/tesseract/wiki

# clone the repository
$ git clone https://github.com/jamesvincentsiauw/Indonesian-KTP-OCR.git

# make image folder
$ mkdir image

# move photos to image folder

# create virtual environment
$ python -m venv venv

# activate virtual environment
$ venv\scripts\activate

# install dependencies
(venv) $ pip install -r requirements.txt

# run project
(venv) $ python main.py

# deactivate virtual environment
(venv) $ deactivate
```