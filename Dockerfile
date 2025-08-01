FROM python:3.12-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN apt-get update && apt-get install -y bash && apt-get upgrade -y && apt-get clean

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python3 manage.py migrate && exec python3 manage.py runserver 0.0.0.0:8000"]
