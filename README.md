# DCpy
SELECT asset_tag.id, set_value, items.id, lob
FROM table1
inner join table2
on asset_tag.id = items.id
order by lob desc