FROM alpine

COPY . /app

RUN apk --update --no-cache add git python3 py3-pip && \
  pip3 install --upgrade pip && \
  pip3 install gunicorn flask

WORKDIR /app
EXPOSE 262

CMD ["/bin/sh","-c","gunicorn -w 5 -b 0.0.0.0:262 app:app"]

