FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
RUN apt-get update && apt-get install -y \
    firefox-esr \
    xvfb \
    wget \
    unzip \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    libxt6 \
    libx11-xcb1 
RUN pip3 install selenium
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
