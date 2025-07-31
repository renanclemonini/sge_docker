FROM python:3.12-slim

WORKDIR /sge

RUN apt-get update && apt-get upgrade -y && apt-get clean

COPY . .

RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python3", "manage.py", "runserver" ]