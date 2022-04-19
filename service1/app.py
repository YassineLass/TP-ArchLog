from flask import Flask
import pika
import json

app = Flask("__main__")

HOST = "0.0.0.0"
PORT = 5000


def send_msg(msg):
    connection = pika.BlockingConnection(pika.URLParameters('amqps://hegzpijz:wP6xyaCkVI8M-ETfBYcYEY5Se9eqvTAE@rat.rmq2.cloudamqp.com/hegzpijz'))
    channel =connection.channel()
    channel.queue_declare(queue="queue1")
    data = { "pattern" : "test",
        "data": msg}

    channel.basic_publish(exchange="",routing_key='queue1',body=json.dumps(data))
    print('[x] message send')
    connection.close()

    # message="HELLO *********"
    # routing_key="test"
    # channel.exchange_declare(exchange='topic', exchange_type='topic')
    # channel.basic_publish(
    # exchange='topic', routing_key=routing_key, body=message)
    # print(" [x] Sent %r:%r" % (routing_key, message))
    # connection.close()

@app.route('/')
def methode():
    for i in range(10):
        send_msg(i)
    return "<h1>Service 1 is working! </h1>"

if (__name__ == "__main__") :
    app.run(debug=True,host=HOST,port=PORT)
