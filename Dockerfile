FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install selenium
RUN apt-get update && apt-get install firefox-esr -y
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
RUN pkill firefox
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
