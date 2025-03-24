---
created:
  - 2024-12-15T22:04
modified: 2024-12-16 19:48
tags:
  - 1nf
  - 2nf
  - 3nf
  - dbt
  - data-engineering
  - data-model
  - sql
  - rdms
type:
  - note
status:
  - completed
---
_Database normalisation_ is a set of criteria/restrictions on table structure that protect against certain data integrity errors (e.g. the same person incorrectly having 2 different dates of birth can be prevented by the design of the database itself). 

_Normalisation_ prevents:

- Insertion anomalies
- Update anomalies
- Deletion anomalies

[This YouTube video](https://www.youtube.com/watch?v=GFQaEYEc8_8) I found extremely helpful. The examples I use in this note are from this video (a bit edited by me).

## Terminology

| Term          | Meaning                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------- |
| Primary Key   | A table column (or combination of columns) which uniquely identifies a row in the table. |
| Foreign Key   | A column in a table which maps to a _primary key_ in another table                       |
| Composite Key | A _primary key_ which is made up of multiple columns rather than just one                |
## First Normal Form (1NF)

- Row order in a table must not be used to convey information
- No mixing of data types within the same column
- Every table must have a primary key
- No rows or columns are duplicated
- No repeating groups of data items (e.g. storing player inventory in a wide table format e.g. columns "item1_name", "item1_quantity", "item2_name", "item2_quantity", ...
## Second Normal Form (2NF)

- 1NF is met
- 2NF involves the relationships between non-key columns and the _primary key_ column(s).
- All non-key columns are functionally dependent on the whole _primary key_ (no partial dependencies). 
	- This means that each non-key column in a function of the entire _primary key_ (it's value cannot be perfectly determined from only a subset of the _primary key_).  
- 2NF only applies to tables with composite primary keys (i.e. primary key consists of multiple columns). If there is a single primary key column, then 1NF automatically implies 2NF.

Example:

| player_id | item       | item_quantity | player_rating |
| --------- | ---------- | ------------- | ------------- |
| 1         | broadsword | 1             | advanced      |
| 1         | gold coin  | 999           | advanced      |
| 1         | dagger     | 3             | advanced      |
The (composite) primary key of this table is `(player_id, item)`. Item quantity depends on both primary key columns, since it is fairly meaningless if one of them is omitted. `player_rating`, however, depends only on `player_id`, which violates [2NF](#Second%20Normal%20Form%20(2NF)).

Problems with this table design (all solved by [2NF](#Second%20Normal%20Form%20(2NF))):

| Name              | Problem example                                                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deletion anomaly  | We can't find the `player_rating` for an existing player with no items in their inventory.                                                                                                                                   |
| Update anomaly    | A player's `player_rating` is modified in the database, and an error during writing results in only some of their rows being updated (and not the others). The database structure has no issue with this data inconsistency. |
| Insertion anomaly | We cannot add the `player_rating` for a new player before they have items in their inventory.                                                                                                                                |
[2NF](#Second%20Normal%20Form%20(2NF)) would be achieved by creating a `players` table with columns `player_id` and `player_rating`.
## Third Normal Form (3NF)

- 1NF is met
- 2NF is met
- There are no transitive partial dependencies
	- i.e. non-key attributes (columns) cannot functionally depend on other non-key attributes (columns)
- A good way to achieve [3NF](#Third%20Normal%20Form%20(3NF)) is almost all situations is to remember "_Every non-key attribute in a table should depend on the key, the whole key and nothing but the key_."

Example:

Suppose that `player_rating` is a function of `player_skill_level`:

$$\begin{array}{lcl}
\text{player skill level}\in \{1,2,3\}  &\rightarrow{}& \text{beginner} \\
\text{player skill level}\in \{4,5,6\}  &\rightarrow{}& \text{intermediate} \\
\end{array}$$

| player_id | player_skill_level | player_rating |
| --------- | ------------------ | ------------- |
| 2         | 3                  | beginner      |
| 9         | 4                  | intermediate  |
This table design violates [3NF](#Third%20Normal%20Form%20(3NF)) because `player_rating` is a function of `player_skill_level`. 
This database design structurally allows `player_skill_level` to advance from $3\rightarrow{}4$ without `player_rating` being updated (which is a data inconsistency).  

## References
* [Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF (YouTube video)](https://www.youtube.com/watch?v=GFQaEYEc8_8)
## Related

* Links to other notes which are directly related go here