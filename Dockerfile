FROM python:3.8-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN python -m pip install pip==22.2.2
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

# install dependencies
RUN apk update && apk add g++ gcc libxml2 libxslt-dev
COPY ./req.txt .

#COPY ./entrypoint.sh .
#RUN chmod +x entrypoint.sh

RUN pip install -r req.txt
RUN chown -R 101:101 /usr/src/app/model_onnx/
RUN chown -R 101:101 /usr/src/app/robot.txt





# copy project
COPY . .

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]