---
created:
  - 2024-12-17T09:01
modified: 2024-12-17 09:16
tags:
  - sql
  - documentation
  - docs
  - postgres
  - rdbms
  - relational
  - database
  - data
  - comment
  - postgresql
type: 
status: 
---
Basically anything in PostgreSQL can be documented using a _COMMENT_, which is a piece of string metadata which attaches to the object itself. 
# Writing Comments 

```sql
-- add a description for a database
COMMENT ON DATABASE mydatabase IS 'Production database'

-- add a description for a table
COMMENT ON TABLE myschema.mytable IS 'Customer information'

-- add a description for a column
COMMENT ON COLUMN mytable.mycolumn IS 'Unique customer identifier'
```

Note that you can COMMENT on basically anything (COMMENT ON ROLE, COMMENT ON CONSTRAINT, COMMENT ON INDEX etc.)
# Accessing Comments

```sql
-- read table comments


-- read columns comments
SELECT		col.table_schema
		,	pgs.relname AS table_name
		,	col.column_name
		,	pgd.description AS column_description
FROM		pg_catalog.pg_statio_all_tables pgs
INNER JOIN	information_schema.columns col
		ON 	col.table_schema = pgs.schemaname
		AND col.table_name = pgs.relname
LEFT JOIN	pg_catalog.pg_description pgd
		ON 	pgd.objoid=pgs.relid
		AND pgd.objsubid=col.ordinal_position
WHERE 		pgs.relname = 'sqlbot_employee_attribute'
;
```

## References
* https://www.postgresql.org/docs/current/sql-comment.html
* https://stackoverflow.com/questions/343138/retrieving-comments-from-a-postgresql-db
## Related

* Links to other notes which are directly related go here