## PolyVoice - MultiLingual Voice Assistant
PolyVoice is a multilingual voice assistant leveraging Google gTTS and Google API to provide seamless voice interaction across multiple languages.

## Features
- Supports multiple languages for voice output.
- Simple and intuitive interface using Streamlit.
- Efficient and responsive performance.

## Project Structure
```bash
PolyVoice/
├── src/
│   ├── __init__.py
│   └── helper.py
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
├── setup.py
└── template.py
```

## Setting Up the Environment
1. Create and activate a new conda environment:
```
conda create -n polyvoice python=3.10
conda activate polyvoice
```
2. Install the required packages:
```
pip install -r requirements.txt
```

## Project Setup
1. Create a setup script `setup.py`:
```
from setuptools import find_packages, setup

setup(
    name= PROJECT_NAME,
    version= VERSION,
    author= AUTHOR_NAME,
    author_email= EMAIL_ID,
    packages=find_packages(),
    install_requires= REQUIREMENTS
)
```

2. Create a `requirements.txt` file with the required packages:
* Following are the requirements of this Project
```
SpeechRecognition
pipwin
pyaudio
gTTS
google-generativeai
python-dotenv
streamlit
requests
google-api-python-client
```

3. Create a project template `template.py`

4. Create a Streamlit app `app.py`

5. Run the application:
```
streamlit run app.py
```

## License
This project is licensed under the [Apache 2.0 License](LICENSE).

## Acknowledgements
* Google gTTS
* Streamlit

