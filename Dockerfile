FROM python:alpine3.16

WORKDIR /app

COPY . .

RUN pip install --trusted-host pypi.python.org flask

ENV "NAME" "Исайчев Данила"

EXPOSE 80

CMD ["python",  "simple_app.py"]