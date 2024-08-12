FROM python:3.10-slim-buster
RUN apt-get update
RUN apt-get install gcc libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "batterychecker.py"]