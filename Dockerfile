FROM python:3.9.1-buster

WORKDIR /usr/src/app

RUN chmod 777 /usr/src/app

RUN apt update -y && \
    apt install -y --no-install-recommends \
    git curl wget

COPY . .

RUN pip install -U -r requirements.txt

CMD [ "bash", "start.sh" ]
