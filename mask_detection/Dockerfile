FROM python:3.6

LABEL maintainer="Mrinalini <mrinalini_m@optum.com>"
RUN apt update

RUN useradd -u 1006 -ms /bin/bash WIT_cfc

COPY . /app
WORKDIR /app

RUN chown -R 1006:1006 /app

RUN chmod 777 -R  /app

RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN pip3 install -r requirements.txt 

EXPOSE 9000

USER 1006

CMD ["python", "app.py"]