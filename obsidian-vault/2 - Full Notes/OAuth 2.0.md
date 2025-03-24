---
created:
  - 2024-06-24T23:25
modified: 2024-06-24 23:30
tags:
  - auth
  - oauth20
  - security
  - authorisation
type:
  - note
status:
  - completed
---

OAuth2.0 is an industry-standard protocol for authorization (i.e. managing access to protected HTTP resources).

OAuth2.0 can be used also for authentication (identifying who a user is) by extending it with [OIDC](#oidc)

I never properly understood OAuth2.0 until I read the RFC (6749), which is surprisingly readable.

Abstract from the RFC (6749):

```bash
The OAuth 2.0 authorization framework enables a third-party
application to obtain limited access to an HTTP service, either on
behalf of a resource owner by orchestrating an approval interaction
between the resource owner and the HTTP service, or by allowing the
third-party application to obtain access on its own behalf. This
specification replaces and obsoletes the OAuth 1.0 protocol described
in RFC 5849.
```

At a high-level:

- Oauth2.0 manages 3rd party client (e.g. Zoom) access to a subset of a resource owner's (e.g. end user's) protected resources (e.g. calendar only) which are stored on a resource server (e.g. gmail), without the 3rd party client (Zoom) having any access to the resource owner's (e.g. end user's) credentials (e.g. username and password).

- This is achieved through the use of an authorisation server. This authorisation server issues the client with temporary access to some of the resource owner's protected resources on the resource server by issuing the client with a temporary access token (this access token is accepted and trusted by the resource server).

Here are the roles defined in the RFC (RFC 6749):

```bash
1.1.  Roles

   OAuth defines four roles:

   resource owner
      An entity capable of granting access to a protected resource.
      When the resource owner is a person, it is referred to as an
      end-user.

   resource server
      The server hosting the protected resources, capable of accepting
      and responding to protected resource requests using access tokens.

   client
      An application making protected resource requests on behalf of the
      resource owner and with its authorization.  The term "client" does
      not imply any particular implementation characteristics (e.g.,
      whether the application executes on a server, a desktop, or other
      devices).

   authorization server
      The server issuing access tokens to the client after successfully
      authenticating the resource owner and obtaining authorization.
```

Here is the oauth2.0 flow at a slightly deeper level:

I will use the example of a social media website (client) logging in an end-user (resource owner) using their google account (resource server).

1. Client (social media website) requests access to user's name, Google ID and gmail address (protected resource) from the resource owner (end-user)

2. Client (social media website) receives an authorisation grant, which is a credential representing the resource owner's (end-user's) authorisation

3. Client (social media website) presents their authorisation grant to the authorisation server in return for an access token

4. Client (social media website) requests the protected resource (user's name, Google ID and gmail address) from the resource server (google), presenting the access token

5. The resource server (google) validates the client (social media website) request and, if valid, serves the request

There are 4 different types of authorisation grants defined in RFC 6749:
(I will give an example usage of each immediately after)

| Grant Type                                      | Description                                                                                                                                                                                                                                                         | Example use case                                                             |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Authorization code                              | A convoluted flow in which the authorisation server acts as intermediary (middleman) between client and resource owner.<br>This is a very secure choice, and the one you always encounter online<br>(OAuth2.0 recommends to extend this grant type to include PKCE) | A web-based platform allows users to authenticate using their Google account |
| Client credentials                              | The client itself has credentials which can be used to directly obtain an access token from the authorisation server.                                                                                                                                               | A microservice fetching data from a database                                 |
| DEPRECATED: Implicit                            | A simplified version of the Authorisation Code flow, which sacrifies security to achieve less calls to the authorisation server                                                                                                                                     |
| DEPRECATED: Resource owner password credentials | The client uses resource owner password credentials directly in order to directly obtain an access token.                                                                                                                                                           |

Explanation of the OAuth2.0 Authorisation Code flow, using the example of a web platform allowing a user to log in to the platfom using their Google account:

0. The client (website) must first register itself with the authorisation server (it will be given a unique client ID and client secret).

1. The client (website) makes a request to the authorisation server to access some of the resource owner's resources (end-user name and google ID). It does this by constructing a URL for the resource owner (end-user) to navigate to in their browser. This request contains required information such as the client ID, client secret, authorisation scope etc.

2. On navigating to the URL, the end-user is prompted by the authorisation server to approve the client (website) request. If they do, they are redirected back to the client (website). The URI to redirect them back to is specified by the client in their initial request to the authorisation server (step 1. above).

3. The authorisation server adds additional query parameters to the client (website) URI which the resource owner (end-user) is redirected back to (in step 2. above):

   - "code": An authorisation code which the client (website) can now use to get access tokens from the authorisation server

   - "state": This is a random string which was included in the original client (website) request to the authorisation server. The authorisation server must ensure that this matches the string which they sent in the original request (step 1. above).

4. The client (website) can now exchange the authorisation code (received in step 3. above) on the authorisation server for a short-lived access token, which it can use to access the resource owner's (end-user's) protected resources without having to ask them for permission again.

5. (optional) Optionally, the request in step 3. above can return an access token **and** a refresh token. A refresh token is a token which the client (website) can use to generate a new access token when the current one has expired. This helps to provide a better user experience (the resource owner doesn't have to re-authorise in all the time).

For a precise description on this process, refer to <https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type>

## Related
* [[OIDC]]