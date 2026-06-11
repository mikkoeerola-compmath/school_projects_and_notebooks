-- Tietokantojen perusteet - Database basics
-- H3 T3
-- mikko.eerola@tuni.fi


SELECT book.title, pre.title as sequel_title
from book left outer join book as pre on book.id = pre.predecessor_id
order by book.id;