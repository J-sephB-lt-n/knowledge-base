---
created:
  - 2026-06-27T21:34
modified: 2026-06-28 23:48
tags:
  - db
  - database
  - python
  - duckdb
  - data-engineering
  - sql
  - olap
type:
  - note
status:
  - in-progress
---
```sql
CREATE TABLE sales_long (
	    year INTEGER
	,   quarter INTEGER
	,   retailer VARCHAR
	,   sales INTEGER   
)
;
INSERT INTO sales_long VALUES  
-- 1984  
(1984, 1, 'IBM', 1200),  
(1984, 2, 'IBM', 1350),  
(1984, 3, 'IBM', 1425),  
(1984, 4, 'IBM', 1550),    
(1984, 1, 'Apple', 650),  
(1984, 2, 'Apple', 720),  
(1984, 3, 'Apple', 780),  
(1984, 4, 'Apple', 850),  
-- 1985  
(1985, 1, 'IBM', 1300),  
(1985, 2, 'IBM', 1450),  
(1985, 3, 'IBM', 1525),  
(1985, 4, 'IBM', 1680),    
(1985, 1, 'Apple', 700),  
(1985, 2, 'Apple', 760),  
(1985, 3, 'Apple', 830),  
(1985, 4, 'Apple', 910)
;
```

```sql
SELECT * 
FROM sales_long
;   
```
```markdown
| year | quarter | retailer | sales |  
|-----:|--------:|----------|------:|  
| 1984 | 1 | IBM | 1200 |  
| 1984 | 2 | IBM | 1350 |  
| 1984 | 3 | IBM | 1425 |  
| 1984 | 4 | IBM | 1550 |  
| 1984 | 1 | Apple | 650 |  
| 1984 | 2 | Apple | 720 |  
| 1984 | 3 | Apple | 780 |  
| 1984 | 4 | Apple | 850 |  
| 1985 | 1 | IBM | 1300 |  
| 1985 | 2 | IBM | 1450 |  
| 1985 | 3 | IBM | 1525 |  
| 1985 | 4 | IBM | 1680 |  
| 1985 | 1 | Apple | 700 |  
| 1985 | 2 | Apple | 760 |  
| 1985 | 3 | Apple | 830 |  
| 1985 | 4 | Apple | 910 |
```

```sql
SELECT * FROM (
	PIVOT_WIDER sales_long
	ON retailer -- or ``ON retailer IN ('IBM', 'Apple')`` 
	USING SUM(sales) -- row aggregation function
	GROUP BY year
	ORDER BY year
) pivot_alias
;
```

```markdown
| year | Apple | IBM |  
|-----:|------:|----:|  
| 1984 | 3000 | 5525 |  
| 1985 | 3200 | 5955 |
```

```sql
CREATE TABLE sales_wide (
		year INTEGER  
	,   Apple INTEGER  
	,   IBM INTEGER	
);
INSERT INTO sales_wide VALUES
        (1984, 3000, 5525)
	,   (1985, 3200, 5955)
;
```

```sql
SELECT * FROM (
	PIVOT_LONGER sales_wide 
	ON COLUMNS (* EXCLUDE (year)) -- or ``ON Apple, IBM``
	INTO
		NAME retailer
		VALUE sales
) pivot_alias
;
```

```markdown
| year | retailer | sales |
| ---: | -------- | ----: |
| 1984 | Apple    |  3000 |
| 1984 | IBM      |  5525 |
| 1985 | Apple    |  3200 |
| 1985 | IBM      |  5955 |
```
## References
* https://duckdb.org/docs/lts/sql/statements/pivot
* https://duckdb.org/docs/lts/sql/statements/unpivot
## Related
* Links to other notes which are directly related go here