FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN flask_temp create-db
RUN flask_temp populate-db
RUN flask_temp add-user -u admin -p admin
EXPOSE 5000
CMD ["flask_temp", "run"]
