# Change the escape character for Windows
# escape=` (backtick)

# Built off of Python3.8-alpine
FROM python:3.8-alpine

# Copy local requirements to docker
COPY ./requirements.txt /requirements.txt

# Install them and then clean up
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

WORKDIR /app/

CMD ["python","manage.py","runserver","0.0.0.0:8000"]