---
created:
  - 2024-06-24T23:28
modified: 2024-06-24 23:29
tags:
  - auth
  - security
  - oauth20
  - authentication
  - identity
  - web
type:
  - note
status:
  - completed
---
Open ID Connect (OIDC):

- is a protocol for user authentication and identity management (i.e. validating the identity of an entity, such as a user, and accessing their attributes)

- is an identity layer built on top of [OAuth2.0](#oauth-20)

- allows 3rd-party applications to verify the identity of the end-user and to obtain basic user profile information

- is secure, centralised, and standardised

- uses [JWTs](https://github.com/J-sephB-lt-n/jwt-checkout/tree/main)

- defines how applications (e.g. a web-based platform) and identity providers (authentication servers) interact in order to establish secure end-user authentication

- is just OAuth2.0 with an additional token (ID token), and extra process for dealing with it (i.e. dictates the required structure of the ID token, how the ID token should be validated by the client etc.)

In the step in an OAuth2.0 flow where an access token is returned, OIDC returns an additional token (an ID token, in the form of a JWT).

Here is the official spec: <https://openid.net/specs/openid-connect-core-1_0.html>

I also enjoyed this: [The OIDC Handbook](https://auth0.com/resources/ebooks/the-openid-connect-handbook)

## Related
* [[OAuth 2.0]]