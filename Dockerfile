from python:3-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["flask", "--app", "apiot", "run", "--port", "3000"]
