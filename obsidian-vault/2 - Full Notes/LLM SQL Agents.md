---
created:
  - 2024-12-09T19:55
modified: 2024-12-09 21:40
tags:
  - llm
  - large-language-model
  - llm-agents
  - sql
  - query
type:
  - note
status:
  - ongoing
---
These are my notes on the use of LLMs to allow people to query SQL databases in natural language 

- Access to Confidential Data
	- If the data in the tables themselves is confidential/sensitive but the user query is not confidential and the database schema (i.e. table names, columns names etc.) is not confidential, then can use a proprietary LLM (e.g. OpenAI API) to generate the SQL queries. 
	- If the user query or the database schema is confidential/sensitive, then will have to use a self-hosted LLM (so as not to share this information with LLM vendors).
	- If the end user is not allowed to see their own data (but only aggregations of it), then a LLM is a bad idea. It is too easy to jail-break an LLM. 
* End users seeing each others' data
	* This should be enforced in the SQL database itself, where each end user is assigned a specific SQL database user (with specific viewing permissions):
		* Some databases (e.g. PostGres) support row-level security (users can only see certain table rows). Alternatively, this can be achieved using views.
- Safety of the data (data corruption/deletion) 
	- LLM must be assigned a restricted database user (with painfully limited access to do damage to the database).
	- Definitely the LLM should have read-only access, and possibly schema-limited, table-limited (possibly even row-limited) access.
	- The SQL user account which runs the LLM-generated SQL queries must not have any database admin privileges (access to read data ONLY), as user-facing SQL services are very vulnerable to SQL injection.
- Health of the database service
	- Measures must be put in place to stop the LLM from crashing the database (or making it slow for real users) 
		- Set short query timeouts for LLM SQL users (no long-running queries)
		* Set the database to limit the CPU and memory usage for individual queries for LLM SQL users
		* Query sanitisation
			- Disallow dangerous SQL keywords which can easily use up all of the database resources e.g. CROSS JOIN, FULL JOIN, WITH RECURSIVE etc.
			- Automatically add LIMIT clauses onto the end of the query (to ensure not too many results are returned)
			- Have a different LLM review the generated SQL, looking to identify SQL injection attacks or resource-heavy queries
- Accuracy of results
	- The LLM must be provided with adequate context
		- A good LLM can easily write valid SQL queries, but it needs help in choosing the right tables and columns to use. The SQL query generation is the job of the LLM. The job of explaining to the model precisely where the appropriate business data lives is primarily the task of the application creator.   
				- (option) Narrow down the relevant parts of the database using the contents of the user query before prompting the LLM to write the SQL query. Other cleaning up of the user query might also be beneficial (e.g. [Swiggy extracts the metrics the user is interested in from their query, and generates a separate SQL query for each](https://bytes.swiggy.com/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e)) .  
			- (option) Give the LLM access (in it's prompt) to examples of previous successful SQL queries from similar user queries (e.g. via RAG). Grow the database of historic successful queries by creating a feedback mechanism for end users to provide feedback on the quality of the results they get from the system (even just "good" or "bad")
			- (option) Give the model relevant database/business context directly within it's prompt (e.g. give it explicit documentation on what tables and columns are available, and exactly what they mean/are for)
				- [Swiggy went so far as to create a curated knowledge base of past SQL queries, business metric definitions, table and column metadata](https://bytes.swiggy.com/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e), which is queried and then used to provide context to the model.
			- (option) Give the model an interface via which it can query/explore database schema documentation (e.g. via tool calling) 
			- (option) If the database is sprawling and complex, then a lot of structuring and documentation work on the database side will enable the LLM to work (make the LLM's task clear, simple and unambiguous) i.e. don't throw in the kitchen sink and expect the LLM to magically guess the correct answer.
	- (option) Give the end user the generated SQL query for them to vett directly
	- (option) Address LLM hallucination using agentic LLM methods such as self-evaluation, voting, chain-of-though, self-consistency etc. e.g. encourage the LLM to specify it's plan/assumptions and do multi-step interaction with the database in order to verify it's own output.
	- (option) A shadow deployment: Deploy the LLM solution alongside actual analysts writing SQL queries (not showing the LLM result to the end user), and compare the LLM output to the the real analyst output
	- (option) A query explanation layer - improve end user trust in the system by explaining to them how their SQL query was arrived at (how their query was sanitised, which database metadata was fetched, which similar historic user queries were used as a reference etc.)
## References
* [Hermes: A Text-to-SQL solution at Swiggy](https://bytes.swiggy.com/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e)
## Related
* Links to other notes which are directly related go here