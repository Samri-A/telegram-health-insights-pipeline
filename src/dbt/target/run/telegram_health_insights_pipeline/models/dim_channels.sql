
  
    

  create  table "Tg_med"."Raw"."dim_channels__dbt_tmp"
  
  
    as
  
  (
    

SELECT DISTINCT
    channel_name AS channel_display_name
FROM "Tg_med"."Raw"."stage_tg_messages"
WHERE channel_name IS NOT NULL
  );
  