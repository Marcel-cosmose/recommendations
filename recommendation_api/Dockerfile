FROM python:3.10.5-bullseye

RUN apt-get update && apt-get install -y \
    tinyproxy postgresql-13-postgis-3 redis-server\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app

# add a jenkins user
ARG JENKINS_UID=1001
RUN useradd -u ${JENKINS_UID} -m jenkins

# port for prometheus
EXPOSE 9000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
