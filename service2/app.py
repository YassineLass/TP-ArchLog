from flask import Flask
import json
import pika
app = Flask("__main__")

HOST = "0.0.0.0"
PORT = 5001

URL="amqps://hegzpijz:wP6xyaCkVI8M-ETfBYcYEY5Se9eqvTAE@rat.rmq2.cloudamqp.com/hegzpijz"
def send_msg(msg):
    connection2 = pika.BlockingConnection(pika.URLParameters(URL))
    channel2 =connection2.channel()
    channel2.queue_declare(queue="queue2")
    data = { "pattern" : "service3",
        "data": msg}
    data['data']=data['data']+"sent from service 2"

    channel2.basic_publish(exchange="",routing_key='queue2',body=json.dumps(data))
    print('[x] message send')
    connection2.close()

def callback(ch,method, properties, body):

    print(" [x] Recieved %r" % body)
    send_msg(body.decode("utf-8") )


def consume():
    connection = pika.BlockingConnection(pika.URLParameters(URL))
    channel =connection.channel()
    channel.queue_declare(queue="queue1")
    channel.basic_consume(queue="queue1",auto_ack=True,on_message_callback=callback)

    channel.start_consuming()


    # channel.exchange_declare(exchange='topic', exchange_type='topic')
    #
    # result = channel.queue_declare('', exclusive=True)
    # queue_name = result.method.queue
    # channel.queue_bind(exchange='topic', queue=queue_name, routing_key="kern.*")
    # channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    # channel.start_consuming()

@app.route('/')
def method():

    return "<h1>Service 2 is working </h1>"


if __name__ == "__main__" :
    print("started")
    consume()
    app.run(debug=True,host=HOST,port=PORT)
