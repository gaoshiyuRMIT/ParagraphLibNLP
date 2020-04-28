### prerequisites
- choose a project; set respective params in set_project_id.sh and run it
- in the project, create a bucket (via console or using [gsutil](https://cloud.google.com/storage/docs/quickstart-gsutil))
- in the project, create a topic, and a subscription that subscribes to that topic (vis console or using [gcloud](https://cloud.google.com/pubsub/docs/quickstart-cli))
- create notifications for the bucket `gsutil notification create -t [TOPIC_NAME] -e OBJECT_FINALIZE -f json gs://[BUCKET_NAME]`


### reference
- [Using Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes?authuser=1#gsutil_2)
- [Managing topics and subscriptions](https://cloud.google.com/pubsub/docs/admin?authuser=1#pubsub-create-topic-cli)