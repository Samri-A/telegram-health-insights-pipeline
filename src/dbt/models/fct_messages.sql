with source as (
    select 
        message_id,
        text
    from {{ ref('stage_tg_messages') }}
),

product_extraction as (
    select 
        *,
        -- Extract keyword-based product name
        case 
            when text ~* 'paracetamol' then 'paracetamol'
            when text ~* 'panadol' then 'panadol'
            when text ~* 'ibuprofen' then 'ibuprofen'
            when text ~* 'amoxicillin' then 'amoxicillin'
            when text ~* 'vitamin' then 'vitamin'
            when text ~* 'zinc' then 'zinc'
            when text ~* 'antacid' then 'antacid'
            else null
        end as product_name
    from source
)

select * from product_extraction
