FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install selenium==4.6.1
RUN pip install webdriver-manager
RUN pip3 install webdriver_manager
RUN apt-get update && apt-get install chromium=114.0.5735.90
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
