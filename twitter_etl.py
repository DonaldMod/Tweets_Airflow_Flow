import pandas as pd
from datetime import datetime

def run_twitter_etl():
    df = pd.read_csv('s3://don-airflow-youtube-bucket/tweets.csv', delimiter=',', na_values='?', on_bad_lines='skip')

    df = df.drop(columns=['longitude', 'latitude', 'country'])

    savedData = df[df['author'] == 'katyperry']

    savedData.to_csv('s3://don-airflow-youtube-bucket/katyperry_twitter_data.csv')