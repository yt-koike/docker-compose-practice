# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt update
RUN apt install -y build-essential curl software-properties-common git
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY streamlit_app.py .

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]