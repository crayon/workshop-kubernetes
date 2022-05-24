FROM python:3.9.11-slim

WORKDIR /

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD server.py .
RUN chmod +x server.py

CMD [ "python", "-u", "/server.py" ]
