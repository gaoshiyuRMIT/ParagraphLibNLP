from google.cloud import storage    
import sys
import io

def read_storage(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """
    # print('Event type: {}'.format(context.event_type))
    # print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    bucketName, fileName = map(data.get, ('bucket', 'name'))
    xmlStr = read_blob(bucketName, fileName)
    print(xmlStr)


def read_blob(bucketName, fileName) -> bytes:
    client = storage.Client()
    bucket = client.bucket(bucketName)
    blob = bucket.blob(fileName)
    s = blob.download_as_string()
    return s
