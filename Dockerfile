FROM python:2.7.14

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

RUN mkdir -p /home/box/web
WORKDIR /home/box/web

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "gunicorn", "-c", "/home/box/web/etc/ask.py", "ask.wsgi" ]

