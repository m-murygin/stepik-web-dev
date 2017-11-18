FROM python:2.7.14

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

RUN mkdir -p /home/box
WORKDIR /home/box

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "gunicorn", "-c", "/home/box/etc/ask.py", "--chdir", "/home/box/ask", "ask.wsgi" ]

