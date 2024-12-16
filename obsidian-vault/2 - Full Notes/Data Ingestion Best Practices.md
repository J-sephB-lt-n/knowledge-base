---
created:
  - 2024-07-03T14:09
modified: 2024-12-16 19:50
tags:
  - data
  - ETL
  - ELT
  - data-ingestion
type:
  - note
status:
  - in-progress
---
* Data quality checks at ingestion:
	* Format
	* Schema
	* Completeness
	* No duplicate entries
	* Consistency
	* Data drift
	* Outliers/anomalies
* Data cleansing (i.e. improve data quality):
	* remove errors
	* remove duplicates
	* fill in missing values
	* correct data types
* Pipeline monitoring
	* Metrics
	* Logs
	* Alerts
		* There must be alerts at source (data first touches the system)
		* Bad quality data
		* Data unavailable when expected
	* Dashboards
* Keep a copy of all raw data (pre-transformation)
* Idempotency: 
	* The same data arriving more than once should not cause duplicate data.
	* Each record should be assigned a unique ID
* Documentation
	* Data dictionary
	* Pipeline diagram
	* Have a Data SLA
* Separate analytical and operational databases
* High performance:
	* Parallelisation
	* Compression
* Data ingestion should be an automated process
* Data in a relational database should be normalised (i.e. in 3rd normal form). 