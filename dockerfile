FROM python:3

WORKDIR /usr/src/app
COPY . .
CMD ["main.py"]
ENTRYPOINT ["python3"]

RUN pip install -r requirements.txt