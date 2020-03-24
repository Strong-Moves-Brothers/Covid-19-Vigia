FROM python:latest
RUN pip3 install --upgrade pip
RUN pip3 install django==3.0.4
RUN pip3 install psycopg2==2.8.4
COPY . /app
WORKDIR /app
EXPOSE 8000