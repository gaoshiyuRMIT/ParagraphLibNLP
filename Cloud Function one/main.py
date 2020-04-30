from google.cloud import storage
import json
import os
import re
from google.cloud import pubsub_v1
# TODO  Bucketname is your Bucket name
# TODO  projectID is your project id
# TODO  triggerFunction2 is your second trigger topic
# TODO  Bucketname2 is your second Bucketname

def hello_gcs_generic(data, context):
    CS = storage.Client()
    bucket = CS.bucket(data['bucket'])
    xmlblob = bucket.blob(data['name'])
    inputxml = xmlblob.download_as_string()
    inputxml=str(inputxml)

    inputxml=inputxml.replace("\\r", "")
    inputxml=inputxml.replace("\\n", "")
    inputxml=inputxml.replace("\\", "")
    inputxml=inputxml.replace("         ", "")
    ssd =re.findall(r"<post>(.+?)</post>",inputxml)
    for i in ssd:
        filename=data['name']+str(ssd.index(i))+".txt"
        Bucketname1 = Bucketname
        data1=filename+" Bucketname is "+Bucketname1
        publish_messages_with_custom_attributes(projectID,triggerFunction2,data1)
        gcs = storage.Client()
        bucket = gcs.get_bucket(Bucketname2)
        blob = bucket.blob(filename)
        blob.upload_from_string(
        str(i)
        )



def publish_messages_with_custom_attributes(project_id, topic_name,filename):
    batch_settings = pubsub_v1.types.BatchSettings(
        max_messages=10,  # default 100
        max_bytes=1024,  # default 1 MB
        max_latency=1,  # default 10 ms
    )

    publisher = pubsub_v1.PublisherClient(batch_settings)
    topic_path = publisher.topic_path(project_id, topic_name)
    data = filename
    #metadata1=metadata2
    # Data must be a bytestring
    data = data.encode("utf-8")
    #metadata1 = metadata1.encode("utf-8")
    # Add two attributes, origin and username, to the message
    future = publisher.publish(
        topic_path, data
    )
    print(future.result())

    print("Published messages with custom attributes.")
    # [END pubsub_publish_custom_attributes]
