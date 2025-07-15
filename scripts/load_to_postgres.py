import os
import json
from pathlib import Path
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

load_dotenv()


conn_params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# Data lake path
DATA_LAKE_PATH = Path("../data/raw/telegram_messages")

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()
cursor.execute("""
    CREATE SCHEMA IF NOT EXISTS raw;
    CREATE TABLE IF NOT EXISTS raw.telegram_messages (
        channel_name VARCHAR(255),
        message_date DATE,
        message_id BIGINT,
        date TIMESTAMP,
        text TEXT,
        sender_id BIGINT,
        media BOOLEAN,
        views INTEGER,
        forwards INTEGER
    );
""")
conn.commit()


for json_file in DATA_LAKE_PATH.glob("*.json"):
    channel_name = json_file.stem  
    with open(json_file, 'r', encoding='utf-8') as f:
        messages = [json.loads(line) for line in f]
    records = [
        (
            channel_name,
            msg["message_id"],
            msg["date"],
            msg["text"],
            msg["sender_id"],
            msg["media"],
            msg["views"],
            msg["forwards"]
        )
        for msg in messages
    ]
    
    query = """
        INSERT INTO raw.telegram_messages (
            channel_name, message_date, message_id, date, text, 
            sender_id, media, views, forwards
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    execute_batch(cursor, query, records)
    conn.commit()

cursor.close()
conn.close()