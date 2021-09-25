import datetime
import subprocess
import pika
import socket

def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()


printout = str(system_call("vcgencmd measure_temp"))[7:].split("'")[0]

result = []
result.append(printout)
print(result)
temps = []
spots = ["CPU"]
for i in range(len(spots)):
    entry = {}
    entry["Temperature"] = float(result[i])
    entry["PartName"] = spots[i]
    temps.append(entry)
outbound = {}
outbound["HostName"] = socket.gethostname()
outbound["Timestamp"] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
outbound["Temperatures"] = temps
print(outbound)
credentials = pika.PlainCredentials('tempy','celsius')
connection = pika.BlockingConnection(pika.ConnectionParameters('centurionx.net',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='InterTopic',exchange_type='topic',durable=True)
channel.queue_bind(exchange='InterTopic',queue='Temperature',routing_key='temperature.*')
channel.basic_publish(exchange='InterTopic',
                      routing_key='temperature.node',
                      body=str(outbound))
connection.close()

