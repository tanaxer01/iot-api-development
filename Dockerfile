from python:3-alpine

WORKDIR /apiot

COPY . .

RUN python -m venv env && source ./env/bin/activate

RUN pip install -r requirements.txt

CMD ["flask", "--app", "apiot", "run"]

