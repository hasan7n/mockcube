FROM tensorflow/tensorflow:2.3.0-gpu
LABEL org.opencontainers.image.authors="Hasan"

COPY ./requirements.txt project/requirements.txt 

RUN pip3 install --no-cache-dir -r project/requirements.txt

ENV LANG C.UTF-8

COPY . /project

WORKDIR /project

ENTRYPOINT ["python3", "/project/mlcube.py"]
