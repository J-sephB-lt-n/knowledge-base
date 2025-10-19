---
created:
  - 2025-10-17T20:13
modified: 2025-10-17 21:31
tags:
type:
  - note
status:
  - in-progress
---

# Logging vs Tracing vs Metrics

| Observation | Description                                                                                                  |     | Popular Tools                                  |
| ----------- | ------------------------------------------------------------------------------------------------------------ | --- | ---------------------------------------------- |
| Metrics     | The same tracked over time<br>(i.e. a numeric time series)<br>e.g. CPU utilisation, requests per minute etc. |     | Time series databases.<br>Prometheus + Grafana |
| Logs        | Timestamped record of a single event                                                                         |     | Elastic Search + LogStash + Kibana             |
| Traces      | A record of events in a causal chain<br>(used to understand cause and effect)                                |     | OpenTelemetry<br>Jaeger                        |

- *Logs* are timestamped records of single discrete events
- *Traces* track the progression of a single request/session/transaction across a system (e.g. across different microservices)
- *Metrics* are numbers which are tracked over time, and often aggregated (e.g. CPU utilisation over time).
# Things that can go in a log entry

| Thing                            | Notes                                                                                                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WHAT                             | What action was taken or event occurred, and what was affected?<br>Can include operation (e.g. LOGIN), operator (e.g. user_id), status (e.g. 403), affected resource (e.g. */v1/login*) |
| WHO                              | Who performed the action?<br>e.g. user_id, machine_id, service account name, IP address etc.                                                                                            |
| WHEN (timestamp)                 | Normalise timezone<br>Always use the same format.<br>Can also report duration of event.                                                                                                 |
| WHERE                            | Where did the action/event originate/occur?<br>e.g. hostname, server_id, container_id, app_id, geographic location, IP address, VPC, region etc.                                        |
| WHY                              | Why did the event occur?<br>e.g. "invalid user credentials"<br>"insufficient funds"<br>"email format invalid"<br>"upstream service timeout"<br>"risk score above threshold"             |
| Full error context (stack trace) |                                                                                                                                                                                         |

# Log Levels

| Level   | General Use                                                                                                                                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DEBUG   |                                                                                                                                                                         |
| INFO    | A noteworthy event happened (e.g. a customer completed an order).                                                                                                       |
| WARNING | No actual code crashed but something bad happened. <br>This is your early warning system.<br>e.g. the response time from a crucial 3rd party API was unexpectedly high. |
| ERROR   | There was an actual exception in the code, not necessarily affecting all users.                                                                                         |
| FATAL   | The entire program is screwed.                                                                                                                                          |

# Notes 

- Logs should be structured and have a consistent schema.
	- This enables them to be aggregated, searched, filtered, analysed
- Include a key in the log record which can be used to recreate the sequence of events which occurred across multiple log records (e.g. a *session_id* or *request_id*)
- Logging can slow down app performance - there are ways to make it more efficient.
- 
## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here