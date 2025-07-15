
  
    

  create  table "Tg_med"."Raw"."fct_image_detections__dbt_tmp"
  
  
    as
  
  (
    

select
    message_id, 
    detected_object_class,
    confidence_score
from "Tg_med"."Raw"."raw_image_detection"
  );
  