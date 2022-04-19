FROM python:3-alpine
WORKDIR /usr/app
ADD . /usr/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
