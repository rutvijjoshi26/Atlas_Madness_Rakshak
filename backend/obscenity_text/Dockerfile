FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /FASTAPI
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN pip uninstall typing_extensions -y && \
    pip uninstall fastapi -y && \
    pip install --no-cache fastapi

RUN python -m nltk.downloader punkt wordnet averaged_perceptron_tagger

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
