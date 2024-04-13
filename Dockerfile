FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
RUN sudo npm install -g phantomjs
RUN pip3 install selenium==2.48.0
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
