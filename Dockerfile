FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install selenium==4.6.1
RUN pip install webdriver-manager
RUN pip3 install webdriver_manager
RUN wget https://chromedriver.storage.googleapis.com/103.0.5060.134/chromedriver_linux64.zip
RUN apt-get update
RUN wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb 
RUN apt-get update
RUN apt-get install -f
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN google-chrome -version
RUN unzip chromedriver_linux64.zip 
RUN mv chromedriver /usr/bin
RUN chmod 777 /usr/bin/chromedriver
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
