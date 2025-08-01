FROM python:3.12-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN python manage.py migrate

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
