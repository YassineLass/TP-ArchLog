FROM python:3-alpine
WORKDIR /usr/app
ADD . /usr/app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python","app.py"]
