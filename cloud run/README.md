
gcloud builds submit --tag gcr.io/<Project ID>/helloworld                   

gcloud run deploy --image gcr.io/<Project ID>/helloworld --platform managed  



#Pleae modify your SQL connection
gcloud run services update helloworld1 \
    --add-cloudsql-instances woven-patrol-276308:australia-southeast1:s3734247\
    --set-env-vars CLOUD_SQL_CONNECTION_NAME=woven-patrol-276308:australia-southeast1:s3734247,\
DB_USER=root,DB_PASS=1234abcd,DB_NAME=lib1
