---
created:
  - 2024-08-04T20:18
modified: 2024-08-04 21:23
tags:
  - api
  - rest
  - http
type:
  - note
status:
  - in-progress
---
- Follow the standards
	- https://www.openapis.org/
	- https://restfulapi.net/
	- OAuth
- Be consistent (across all endpoints)
	- e.g. date formats, ranges, query parameters
	- Pagination works the same way everywhere
	- Error handling
	- Naming conventions
	- Versioning
- Simple to use for the end user
	- Sensible default arguments
	- Don't force the user to deal with complicated things like timezones (unless necessary, obviously)
- Write clear documentation
	- Explain what every argument/query parameter means
	- Give useful examples
- API must be easy to navigate
	- e.g. a GET /transaction endpoint should contain a customer ID in the response
	- i.e. include IDs which allow the user to link to different parts of the system
	- IDs must be primary keys (i.e. no duplicated or missing IDs etc.)
- Make it easy for users to integrate your API into their other systems and APIs
	- e.g. allow users to store their own custom metadata in your objects (for example, stripe allows you to store your own arbitrary json in a customer object)
- Add support for webhooks
- Provide an SDK
## References
* https://www.youtube.com/watch?v=SjUQLryotAk (ArjanCodes youtube video)