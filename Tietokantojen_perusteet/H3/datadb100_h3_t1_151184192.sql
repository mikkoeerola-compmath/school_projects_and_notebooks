-- Tietokantojen perusteet - Database basics
-- H3 T1
-- mikko.eerola@tuni.fi


SELECT book.title, pre.title as predecessor_title
from book, book as pre
where book.predecessor_id = pre.id
order by book.id;