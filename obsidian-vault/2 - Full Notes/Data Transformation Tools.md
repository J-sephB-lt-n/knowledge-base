---
created:
  - 2024-07-05T09:31
modified: 2024-07-05 14:38
tags:
  - data
  - ETL
  - ELT
  - data-ingestion
  - data-engineering
  - python
  - data-transformation
type:
  - note
status:
  - in-progress
---
By "data transformation" I mean:
* Cleaning (correcting or removing inaccurate records)
* Aggregating 
* Combining (form new tables by combining data from multiple input tables)
* Calculating fields (creating new fields by combining existing ones e.g. ratios or windows)

I'm only considering open-source tools.

| Tool   | Description/Use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DBT    | Command-line tool. A centralised (and very opinionated/structured) orchestration layer sitting on top of a Data Warehouse, managing the whole transform step. Includes data modelling, testing, documentation in a very predefined workflow structure. Data manipulation is done via SQL (supports templating using Jinja).                                                                                                                                                                                                                                                                                                            |
| Polars | Performance-focused, multi-threaded, parallelised python data-frame library. Able to process datasets which cannot fit into RAM. Requires strict schema definitions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Pandas | Very established and full-featured python data-frame library with an object-oriented interface. which holds all data in RAM. Does computation using numpy and C. Not thread-safe.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DuckDB | Feature-rich local SQL engine with no external dependencies (although it has APIs for python, java, C, Go etc.). SUPER fast (e.g. faster than polars on some query types). Stores database as a single file on the filesystem (or can operate ephemerally in RAM). Convenient interface for importing from (possibly many) flat files like csv, json, parquet etc. Supports larger-than-memory datasets by spilling temporarily to disk.<br>Very similar to SQLite, although SQLite is optimised for OLTP (fast lookup of individual rows) whereas DuckDB is optimised for OLAP (aggregate calculations across large numbers of rows). |
| SQLite | The most-used database in the world (e.g. it is on every Android and iOS device). A small, fast, self-contained, high-reliability, full-featured, SQL database engine built in C.<br>Stores database as a single flat file on the filesystem (or can operate ephemerally in RAM).<br>The python standard library has an interface for working with it.<br>Very similar to DuckDB (described above), although SQLite is better for OLTP queries whereas DuckDB is better for OLAP queries.                                                                                                                                              |
| Ibis   | A python data-frame interface which can be used on top of almost any backend (BigQuery, MySQL, PostgreSQL, pandas, DuckDB, ClickHouse, pyspark, snowflake, SQLite etc. etc.). In other words, the execution engine can change while the query language stays the same.<br>Uses both it's own OOP interface (similar to pandas) as standard SQL, and the 2 can be used interchangeably within the same script.                                                                                                                                                                                                                          |
| pETL   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
## Related 
* [[Python Data Validation Tools]]