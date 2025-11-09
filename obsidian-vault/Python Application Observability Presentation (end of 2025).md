---
created:
  - 2025-11-07T16:12
modified: 2025-11-09 13:41
tags:
  - logging
  - python
  - observability
  - telemetry
  - otel
  - opentelemetry
  - open-telemetry
type:
  - note
status:
  - in-progress
---
## Observability vs Monitoring

 *Observability* is a term [borrowed from control theory, where the "observability" of a system measures how well its state can be determined from its outputs](https://en.wikipedia.org/wiki/Observability_(software)#Etymology,_terminology_and_definition).

## Telemetry


## The 3 Pillars of Observability

Software observability relies on 3 main types of telemetry data: 

| Type    | Description                                                                                                                                | Example                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Metrics | A scalar value measured over time (i.e. a value in a numeric time series)                                                                  | Number of HTTP requests per second.                               |
| Logs    | Immutable records of discrete events occurring within the system                                                                           | Record of an instance of a specific user logging in to the system |
| Traces  | Tracking the flow of a single request as it travels through different services and components of a (typically distributed) software system |                                                                   |

## Traces (Distributed Tracing)

- 1 trace represents 1 full end-to-end request
- Each span within the trace represents a single operation/unit of work
- Spans are plotted with time on the x axis
- Spans are nested in a tree structure (children were called by their parent). E.g. if the spans are HTTP requests, then the child spans are HTTP requests made by the parent process.
- Traces show you:
	- Overall performance.
	- Optimisation opportunities (where are the bottlenecks, what is running sequentially that might be run in parallel). 

Here is a piece of [an amazing example I found online](https://betterstack.com/community/guides/observability/jaeger-guide/):

1. The `frontend` service receives a `/dispatch` request, initiating the process.
2. The `frontend` then makes a GET request to the `/customer` endpoint of the `customer` service.
3. The `customer` service executes a `SELECT SQL` query on MySQL, returning the results to the `frontend`.
4. Upon receiving the results, the `frontend` makes an RPC call to the `driver` service (`driver.DriverService/FindNearest`), which then makes multiple calls to Redis (some failing).
5. ...there is more in the example, but I'm truncating it here.
   
![source: https://betterstack.com/community/guides/observability/jaeger-guide/](../7%20-%20assets/Python%20Application%20Observability%20Presentation/trace_example.avif)
Individual spans within the trace can be drilled down into to reveal additional information about the span:

![source: https://betterstack.com/community/guides/observability/jaeger-guide/](../7%20-%20assets/Python%20Application%20Observability%20Presentation/span_detail_example.avif)

## Open Telemetry


## Native Python Logging

Python has **WAY** more functionality and flexibility than you will ever need.

A single logger in python works like this:

![source: https://www.youtube.com/watch?v=9L77QExPmI0](../7%20-%20assets/Python%20Application%20Observability%20Presentation/python_logging_architecture.png)

- The logger is an instance of the built-in `logging.Logger` class, which you use in your code to generate log messages e.g.
  ```python
  logger = logging.getLogger(__name__)
  logger.info("Something noteworthy happened.")
  logger.warning("Something a bit worrying happened.")
  logger.exception("The code broke.")
  ```
- A log message created by a logger is an instance of the built-in `logging.logRecord` class. The `logging.logRecord` automatically always has number of useful built-in attributes containing contextual information available at the time that the record was created, such as:
	1. message
	2. levelname (severity e.g. "INFO", "DEBUG", "CRITICAL" etc.)
	3. created (datetime that the logRecord was created)
	4. exc_info (error information)
	5. stack_info
	6. filename
	7. funcName
	8. lineno
	9. process (process ID)
	10. thread (thread ID)
	11. name (name of logger)
	12. ...and many more (https://docs.python.org/3/library/logging.html#logrecord-attributes)
- Every logger has a severity level (e.g. "DEBUG", "WARNING" etc.) set on the logger itself. Each log record also has a severity level. If the logger generates a log record with severity level below the logger's severity level, that message is discarded (lost forever). 
	- If you don't set a severity level on your logger, it will inherit the level of it's parent logger. If you don't set any levels on any of your loggers, then they will end up inheriting the default level of the root logger, which is *"WARNING"*.
- After the level check, a log record is passed through any filters you have added to the logger (there are no filters by default). 
	- A filter is just a python function (a method, technically) which decides (based on the log record's attributes) whether the record should be discarded or not. You can write your own custom filters to do whatever you wish.
	- Any records which are blocked by a filter and discarded (lost forever).
- Finally, if the log record has passed the level check and been accepted by all of the filters, then the log record is passed independently to each of the handlers attached to the logger.
	- Each handler filters the log records passed to it, formats them in a specific way, then writes them to a specific location (e.g. stdout, file, email etc.)
	- Each handler has it's own severity level threshold and (optional) filters (like the logger itself does).
	- If a handler drops a log record (by severity level or a filter), this doesn't cause the log to be automatically dropped by the other handlers.
	- Each handler has a formatter at the end, which is just a function (method, actually) which formats the log message in some way (turns the `logging.logRecord` object into a string for transmission to somewhere). A good choice for output format is a JSON string.
		- The formatter decides which log record attributes appear in your actual logs.
	- Python has built-in functionality for writing to stdout, stderr, file, socket, email, memory, HTTP (and a whole bunch of others). If these don't suite your needs, you can write your own custom `logging.Handler`.
	- Loggers (including the root logger) have no handlers by default, so log records go nowhere by default (the log records are just discarded).

- There is a tree of python loggers. 
	- There is automatically a logger called "root", which you could access directly using 
	  ```python
	  logger = logging.getLogger("root")
	  # or logging.info(...) # don't do this though
	  ```
	- The root logger is the parent of every other created logger in the application.
	- When you name a logger with periods in it, then you define a hierarchy of loggers. For example...
	  ```python
	  # /src/utils/text/chunking.py
	  logging.getLogger(__name__)
	  ```
	  gives you the logger with name `src.utils.text.chunking`
		- This `chunking` logger has parent logger `text`, which itself has parent logger `utils`, which itself has parent logger `src`, which itself has parent logger `root`.
	- You don't have to use `logging.getLogger(__name__)` - you can define your own hierarchy of loggers however you like e.g. `logging.getLogger("app.llm")`
	- Each logger automatically sends it's log records also to it's parent logger, which processes the record itself, then passes it to it's own parent logger etc. (back up to the root logger). This behaviour can be turned off, if desired.
	- Typically, you don't need any of this. Just put all of your handlers and filters on the root logger, and let all logs propagate to the root logger for filtering, formatting and writing (don't use the root logger for generating log messages directly though).

## References
* [A Practical Guide to Distributed Tracing with Jaeger (betterstack.com)](https://betterstack.com/community/guides/observability/jaeger-guide/)
* [Modern Python Logging (YouTube)](https://youtu.be/9L77QExPmI0?si=Ly2xT0v8gFB0YzZL)
## Related
* Links to other notes which are directly related go here