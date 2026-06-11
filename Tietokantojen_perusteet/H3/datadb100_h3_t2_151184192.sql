-- Tietokantojen perusteet - Database basics
-- H3 T2
-- mikko.eerola@tuni.fi


SELECT book.title, pre.title as predecessor_title
from book left outer join book as pre on pre.id = book.predecessor_id
order by book.id;