FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-chace-dir -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]
