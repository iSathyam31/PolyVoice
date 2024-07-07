from setuptools import find_packages, setup

setup(
    name="MULTILINGUAL ASSISTANT",
    version="0.0.1",
    author="Sattu",
    author_email="sathyam.a31@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)