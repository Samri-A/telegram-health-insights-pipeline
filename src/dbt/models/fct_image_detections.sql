{{ config(materialized='table') }}

select
    message_id, 
    detected_object_class,
    confidence_score
from {{ source('Raw', 'raw_image_detection') }}
