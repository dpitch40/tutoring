# A very brief introduction to the Internet

## Internet protocol stack

| Layer | Examples | Description |
| --- | --- | --- |
| Application | HTTP, HTTPS, SMTP, FTP, Websocket, DNS | The highest and most multifeatured layer, that websites and applications are built on |
| Transport | TCP, UDP | Builds additional features onto network later; used by the application layer for data transmission |
| Network | IP | Provides IP address routing; "the glue that binds the Internet together" |
| Link | Ethernet | Passes datagrams from node to node |
| Physical | IEEE 802.3ab | The lowest layer; transmits individual bits down a wire/fiber optic cable |

## The most commonly used protocol: HTTP

### An example http URL

`http://subdomain.awebsite.com/place/subpage?arg1=foo&arg2=bar`

* `http://` Protocol specifier
* `.com` Top-level domain
* `subdomain.awebsite` Lower-level domains in the DNS hierarchy
* `/place/subpage` Resource to access
* `?arg1=foo&arg2=bar` URL arguments

### The HTTP Request

Consists of four main parts: the HTTP method to use, the target (resource), request headers, and an optional request body.

#### Common HTTP methods

* **GET**: Retrieves information
* **POST**: Creates a new resource
* **PUT**: Updates or creates a resource
* **DELETE**: Deletes a resource

#### Common HTTP request headers

* *Host* (mandatory): The domain name of the server the request is being sent to
* *Accept*: The type of content the client is expecting in the response
* *User-Agent*: Information about the client, e.g. the type and version of the web browser sending the request.
* *Cookie*: Key-value data previously set by the server (see below)

### The HTTP Response

Consists of three main parts: a status code, response headers, and an optional response body.

#### HTTP status codes

* 1xx: Informational (not used much)
* 2xx: Success
* 3xx: Redirect--client must take some additional action to complete the request
* 4xx: Client-side error
  * e.g. 404 not found error
* 5xx: Server-side error

#### Common HTTP response headers

* *Content-Type*: The type of content the server is returning
* *Content-Length*: The length in bytes of the data being returned
* *Set-Cookie*: Instructs the user agent to store some key-value data and include it in the headers of future requests to this host

## HTTP request and response diagram

![HTTP diagram](HTTPDiagram.png)
