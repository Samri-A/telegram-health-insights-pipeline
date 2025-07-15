{{ config(materialized='table') }}

SELECT DISTINCT
    channel_name AS channel_display_name
FROM {{ ref('stage_tg_messages') }}
WHERE channel_name IS NOT NULL
