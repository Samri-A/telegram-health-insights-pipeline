

SELECT DISTINCT
    channel_name AS channel_display_name
FROM "Tg_med"."Raw"."stage_tg_messages"
WHERE channel_name IS NOT NULL