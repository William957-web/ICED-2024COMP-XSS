FROM python:3.9

RUN sed -i 's/deb.debian.org/mirror.twds.com.tw/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirror.twds.com.tw/g' /etc/apt/sources.list

RUN pip3 install --upgrade pip
RUN pip3 install flask

RUN apt-get update
RUN apt-get install chromium -y

WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
