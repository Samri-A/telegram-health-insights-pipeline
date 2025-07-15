

WITH dates AS (
    SELECT
        date::DATE AS date_id,
        EXTRACT(DAY FROM date) AS day,
        EXTRACT(MONTH FROM date) AS month,
        EXTRACT(YEAR FROM date) AS year,
        TO_CHAR(date, 'Day') AS weekday,
        TO_CHAR(date, 'Month') AS month_name
    FROM generate_series(
        '2024-01-01'::DATE,
        CURRENT_DATE,
        INTERVAL '1 day'
    ) AS date
)

SELECT * FROM dates