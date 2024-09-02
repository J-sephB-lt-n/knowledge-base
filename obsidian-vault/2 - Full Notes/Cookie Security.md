---
created:
  - 2024-08-14T13:48
modified: 2024-08-16 16:11
tags:
  - flask
  - cookie
  - session
  - session-id
  - session-cookie
  - web
  - browser
  - auth
  - authorisation
  - authentication
type:
  - notes
status: 
---

| Practice                                                                                                                                                                                                                                        | Reason                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Never send anything over HTTP - only HTTPS                                                                                                                                                                                                      | HTTP sends everything (including sensitive cookies) as plain text, making it easy to steal sensitive information                                           |
| Include the `httpOnly` cookie attribute                                                                                                                                                                                                         | This stops frontend scripts being able to access the cookie (via the DOM document.cookie object)                                                           |
| Include the `secure` cookie attribute                                                                                                                                                                                                           | This allows cookie transmission only over HTTPS                                                                                                            |
| Set the `sameSite` cookie attribute to '`Strict`' if possible, otherwise '`Lax`'                                                                                                                                                                | Provides some protection against [Cross-Site Request Forgery](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)                                      |
| Be very restrictive with the scope of the  `Domain` and `Path` cookie attributes (restrict cookie to origin server by not setting `Domain`, and set `Path` to the most restrictive allowable web path)                                          | This stops weak security on one subdomain creating an entry point for attack on another more secure subdomain on the same domain                           |
| Validate the client cookie values before using them as you would any other form of user input                                                                                                                                                   | Using client-provided values directly can lead to code injection (e.g. SQL injection) attacks                                                              |
| If the cookie is used as a Session ID, do not set the `Max-Age` nor `Expires` cookie attributes. This will make the cookie get deleted when the client closes their browser. Limit the lifespan of the session ID using server-side logic.      | Cookies with either of these attributes set will persist even when the client closes their browser. A longer lifespan gives an attacker more time to work. |
| If cookie is used for authorisation (e.g. a session cookie), then invalidate the session cookie it if is is received within a request from a different IP address, browser, user agent etc. and require the user to log in (authenticate) again | It is hard for an attacker to spoof an IP address. This adds an extra layer of defense                                                                     |
| Cookies should have generic names (e.g. "id")                                                                                                                                                                                                   | They should not reveal any information about the framework which generated them, their use etc.                                                            |
| If cookie is used as a session ID, it's length must be at least `128 bits (16 bytes)` and unpredictable (at least `64 bits` of entropy)                                                                                                         | To prevent brute-force attacks                                                                                                                             |
| If cookie is used as a Session ID, it's content should be meaningless (just a key to the information stored server-side)                                                                                                                        | Prevents leaking sensitive information                                                                                                                     |
| If cookie is used as a session ID, create a new session ID and invalidate the old session ID when a user logs in again (reauthenticates)                                                                                                        | This helps to prevent [session fixation attacks](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#session_fixation)                  |

If the cookie is being used as a Session ID, there are many more applicable security best practices - see the [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
## References
* https://blog.miguelgrinberg.com/post/cookie-security-for-flask-applications
* https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie
* https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks

## Related

* 