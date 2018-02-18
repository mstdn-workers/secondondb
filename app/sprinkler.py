import pika
import requests
import json

def hook(event, id, URL, secret):
    post_data = {
        'event': event,
        'id': id,
        'secret': secret,
    }
    print(post_data)
    with requests.session() as client:
        try:
            r = client.post(URL, data=post_data)
            print(r.text)
        except Exception as e:
            print("Exception")
            print(e)
            pass

def callback(ch, method, properties, body):
    # 通知受け時処理
    sprinkl( json.loads(body.decode()) )
    pass

def getURL4Hook():
    # いいかんじにリストURLとsecretのKVリスト作る
    URLlist = [{}, ]
    return URLlist

def sprinkl(status):
    try:
        for url in getURL4Hook():
            hook(status['event'], status['id'], url['url'], url['secret'])
    except:
        pass

def recv(host, queue):
    with  pika.BlockingConnection(pika.ConnectionParameters(host)) as conn:
        channel = conn.channel()
        channel.queue_declare(queue=queue)
        channel.basic_consume(callback,queue=queue,no_ack=True)
        channel.start_consuming()

if __name__ == '__main__':
    recv('rabbitmq', 'event_notify')