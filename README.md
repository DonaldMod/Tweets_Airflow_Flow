# Tweets_Airflow_Flow

I am using AWS EC2 instance to run Airflow in an Ubuntu environment and S3 bucket to stored my existing and new files.

## Ubuntu
I installed the following packages in the environment:
- sudo apt-get update
- sudo apt install python3-pip
- sudo pip install apache-airflow
- sudo pip install pandas
- sudo pip install s3fs

Test if apache-airflow works:
- airflow standalone        // Save the Username and Password 

Add the following info to the "~/airflow/airflow.cfg" file, then save:
- dags_folder = /home/ubuntu/airflow/twitter_dag

Create the directory "~/airflow/twitter_dag"
- mkdir ~/airflow/twitter_dag

Create the following files in the "~/airflow/twitter_dag" direcrtory on Ubuntu environment
- twitter_etl.py    | <a href="https://github.com/DonaldMod/Tweets_Airflow_Flow/blob/main/twitter_etl.py" target="_blank">Twitter ETL File</a>
- twitter_dag.py    | <a href="https://github.com/DonaldMod/Tweets_Airflow_Flow/blob/main/twitter_dag.py" target="_blank">Twitter Dag File</a>

Update those files accordingly with the files provided in this repo

## Airflow
To start the webserver you need to run the
- airflow standalone 
- [AWS public IP]:8080
- Username and Password

Search for your dag
- twitter_dag

Then run the dag to confirm that works