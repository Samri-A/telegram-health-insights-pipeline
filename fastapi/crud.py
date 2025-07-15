from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List

def get_top_products(db: Session, limit: int = 10) -> List[dict]:
    sql = text("""
        SELECT product_name, COUNT(*) as mention_count
        FROM fct_messages
        GROUP BY product_name
        ORDER BY mention_count DESC
        LIMIT :limit
    """)
    return db.execute(sql, {"limit": limit}).fetchall()

def get_channel_activity(db: Session, channel_name: str) -> List[dict]:
    sql = text("""
        SELECT d.date, COUNT(*) AS message_count
        FROM fct_messages f
        JOIN dim_dates d ON f.date_id = d.date_id
        JOIN dim_channels c ON f.channel_id = c.channel_id
        WHERE c.channel_name = :channel_name
        GROUP BY d.date
        ORDER BY d.date
    """)
    return db.execute(sql, {"channel_name": channel_name}).fetchall()

def search_messages(db: Session, query: str) -> List[dict]:
    sql = text("""
        SELECT f.message_id, f.message_text, c.channel_name
        FROM fct_messages f
        JOIN dim_channels c ON f.channel_id = c.channel_id
        WHERE f.message_text ILIKE :q
        LIMIT 100
    """)
    return db.execute(sql, {"q": f"%{query}%"}).fetchall()
