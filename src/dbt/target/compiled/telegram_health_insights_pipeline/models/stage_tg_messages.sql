with source as (
    select * from "Tg_med"."Raw"."raw_telegram_message_data"
),

cleaned as (
    select
        cast(message_id AS BIGINT) AS message_id,
        channel_name,
        cast(date as timestamp) as message_timestamp,
        text,
        cast(views as integer) as views,
        cast(forwards as integer) as forwards,
        media
    

    from source
)

select * from cleaned