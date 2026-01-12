FROM python:3.10-slim

WORKDIR /food

COPY . .


CMD ["python", "food.py"]
