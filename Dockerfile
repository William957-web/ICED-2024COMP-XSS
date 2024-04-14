FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN apt-get update
RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb 
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
