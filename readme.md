## prerequisites
- choose a project; fill in set_project_id.sh accordingly and run it
- create a bucket
- link this function to object finalization on bucket: `gcloud functions deploy FUNCTION_NAME --trigger-resource YOUR_TRIGGER_BUCKET_NAME --trigger-event google.storage.object.finalize --runtime python37`

## references
- [Google Cloud Storage Triggers | Cloud Functions](https://cloud.google.com/functions/docs/calling/storage)
- [google-cloud-storage Blobs](https://googleapis.dev/python/storage/latest/blobs.html)