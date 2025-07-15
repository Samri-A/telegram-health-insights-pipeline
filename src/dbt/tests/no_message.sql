select *
from {{ ref('fct_messages') }}
where message_text = '' or message_text is null
