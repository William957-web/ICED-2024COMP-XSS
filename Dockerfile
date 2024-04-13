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
RUN wget -q -O /tmp/geckodriver-v0.29.1-linux64.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz && \
    tar -xzf /tmp/geckodriver-v0.29.1-linux64.tar.gz -C /usr/bin && \
    chmod +x /usr/bin/geckodriver && \
    rm /tmp/geckodriver-v0.
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
