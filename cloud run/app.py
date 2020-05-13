import os
import datetime



from flask import Flask, render_template, request, Response
from google.cloud import logging
import sqlalchemy
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

app = Flask(__name__)



# [START cloud_sql_mysql_sqlalchemy_create]
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=db_user,
        password=db_pass,
        database=db_name,
        query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
    ),
    # ... Specify additional properties here.
    # [START_EXCLUDE]
    # [START cloud_sql_mysql_sqlalchemy_limit]
    # Pool size is the maximum number of permanent connections to keep.
    pool_size=5,
    # Temporarily exceeds the set pool_size if no connections are available.
    max_overflow=2,
    # The total number of concurrent connections for your application will be
    # a total of pool_size and max_overflow.
    # [END cloud_sql_mysql_sqlalchemy_limit]
    # [START cloud_sql_mysql_sqlalchemy_backoff]
    # SQLAlchemy automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.
    # [END cloud_sql_mysql_sqlalchemy_backoff]
    # [START cloud_sql_mysql_sqlalchemy_timeout]
    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds
    # [END cloud_sql_mysql_sqlalchemy_timeout]
    # [START cloud_sql_mysql_sqlalchemy_lifetime]
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # reestablished
    pool_recycle=1800,  # 30 minutes
    # [END cloud_sql_mysql_sqlalchemy_lifetime]
    # [END_EXCLUDE]
)
# [END cloud_sql_mysql_sqlalchemy_create]


@app.route('/')
def hello_world():
    log_client = logging.Client()
    logger = log_client.logger("cloudfunctions.googleapis.com%2Fcloud-functions")
    target = os.environ.get('TARGET', 'World')
    logger.log_text("i come from cloud run")
    return 'Hello vvvv{}!\n'.format(target)


@app.route('/nlp',methods=["POST"])
def hello_nlp():
    #request = request.form["TODO"]   #Anything you want get from request
    response_auth_list=[]
    response_para_list=[]
    auth_dict={}
    para_dict={}
#For example:

    gender="male"
    age="40"
    industry="Internet"
    astro_sign="Cancer"


    log_client = logging.Client()
    logger = log_client.logger("cloudfunctions.googleapis.com%2Fcloud-functions")
    #target = os.environ.get('TARGET', 'World')
    logger.log_text("i come from NLP")
    stmt = sqlalchemy.text(
        "SELECT * FROM Author where gender='"+gender+"' and age="+age+" and industry='"+industry+"' and astro_sign='"+astro_sign+"';"
    )
    with db.connect() as conn:
        result=conn.execute(stmt)

        for row in result:
            id=row[0]
            auth_dict["id"] = row[0]
            auth_dict["gender"] = row[1]
            auth_dict["age"] = row[2]
            auth_dict["industry"] = row[3]
            auth_dict["astro_sign"]=row[4]
            response_auth_list.append[auth_dict]
            stmt2 = sqlalchemy.text(
                "SELECT * FROM Post where author_id='"+str(id)+"';"
                #"SELECT avg(sentiment_score),avg(sentiment_magnitude) FROM Post where author_id='"+str(id)+"';"
            )
            result2=conn.execute(stmt2)
            for row2 in result2:
                para_dict["id"]= row2[0]
                para_dict["author_id"] = row2[1]
                para_dict["publish_date"] = row2[2]
                para_dict["bucket_path"] = row2[3]
                para_dict["sentiment_score"] = row2[4]
                para_dict["sentiment_magnitude"] = row2[5]
                response_para_list.append[para_dict]
                logger.log_text("SUCCESS of inner")


    return Response(
        status=200,
        response="two list_dicts",
        #TO DO anything you want to send
        )



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
