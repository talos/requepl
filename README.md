# requepl

An HTTP repl with multiple sessions.

Wraps the Python [Requests](http://pypi.python.org/pypi/requests) library.

## Installation

From source:

```bash
    $ git clone https://talos@github.com/talos/requepl.git
    $ cd requepl
    $ python setup.py install
```

From pypi:

```bash
    $ pip install requepl
```

## Usage

#### start with default host (localhost)

```bash
    $ requepl
    ***An HTTP repl with multiple sessions. Type `help` for a list of commands.
    (localhost)http://localhost/> 
```

#### start with a specific host

```bash
    $ requepl www.htttools.com:8080
    ***An HTTP repl with multiple sessions. Type `help` for a list of commands.
    (www.htttools.com:8080)http://www.htttools.com:8080/> 
```

#### make a request

resolved relative to the specified path

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> head /
    http://www.htttools.com:8080/ responded with `status` 200, 3 `headers`, and `content` of length 0
```

head, get, post, put, and delete verbs all supported

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> get /
    http://www.htttools.com:8080/ responded with `status` 200, 3 `headers`, and `content` of length 1260
```

request data is parsed as a Python object if possible.  if the object is a dict, it is form-encoded.

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> post / {"form":"encoded", "data":"in", "a": "python dictionary"}
    http://www.htttools.com:8080/ responded with `status` 200, 3 `headers`, and `content` of length 1377
```

json data can be serialized and sent in a string.  it will be properly encoded.

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> put / '{"json":"data", "inside":"a", "python": "string"}'
    http://www.htttools.com:8080/ responded with `status` 200, 3 `headers`, and `content` of length 1389
```

ditto with an arbitrary string, which doesn't even have to be surrounded in quotes.

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> delete data chillin' &etc. is still encoded!
    Request data is not a python object, sending as 'chillin' &etc. is still encoded!'
    http://www.htttools.com:8080/data responded with `status` 200, 3 `headers`, and `content` of length 1323
```

#### observe the last response

see the status code

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> status
    200
```

see the response headers

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> headers
    { 'connection': 'close', 'content-length': '1323', 'content-type': 'text/html'}
```

see the response content

```bash
    (www.htttools.com:8080)http://www.htttools.com:8080/> content
    <P
    >HTTP/1.1 request from 72.14.228.138:17081</P
    ><HR
    ><PRE
    >DELETE /data HTTP/1.1
      Host: www.htttools.com:8080
      Content-Length: 32
      Accept-Encoding: identity, deflate, compress, gzip
      Accept: */*
      User-Agent: python-requests/0.8.3

      chillin' &amp;etc. is still encoded!</PRE>
```

#### modify session state

set an arbitrary request header.  tab is your friend!

```bash
    (google.com)http://google.com/> set_header User-Agent Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011-10-16 20:23:00
    { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011-10-16 20:23:00'}
    (google.com)http://google.com/> Referer http://www.google.com/
    { 'Referer': 'http://www.google.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011-10-16 20:23:00'}
```

delete an existing request header.  tab is still your friend!

```bash
    (google.com)http://google.com/> unset_header User-Agent
    { 'Referer': 'http://www.google.com/'}
```

get a readout of the request headers in place for this session.

```bash
    (google.com)http://google.com/> request_headers
    { 'Referer': 'http://www.google.com/'}
```

#### switch to other sessions

```bash
    (caustic)summer-air:requepl talos$ requepl
    (localhost)http://localhost/> session en.wikipedia.org
    ***An HTTP repl with multiple sessions. Type `help` for a list of commands.
    (en.wikipedia.org)http://en.wikipedia.org/> 
```

Requests are resolved against the host for your current session.

```bash
    (en.wikipedia.org)http://en.wikipedia.org/> get /
    http://en.wikipedia.org/ responded with `status` 200, 14 `headers`, and `content` of length 54885
```

You can have as many sessions as you want.

```bash
    (wikipedia)http://en.wikipedia.org> session nytimes nytimes.com
    (nytimes.com)http://nytimes.com/> get /
    http://nytimes.com/ responded with `status` 200, 9 `headers`, and `content` of length 128667
```

Each session has its own cookie jar.

```bash
    (nytimes)http://nytimes.com> cookies
    { 'RMID': '389d0d8135844ee3c5c18476', 'adxcs': 's*2ace1=0:1|s*2554d=0:1'}
    (nytimes.com)http://nytimes.com/> session en.wikipedia.org
    (wikipedia)http://en.wikipedia.org> cookies
    { }
```

You can see which sessions you've used.

```bash
    (nytimes)http://nytimes.com> sessions
    nytimes.com
    en.wikipedia.org
    localhost
```

Drop into other sessions automatically when you destroy one.

```bash
    (nytimes)http://nytimes.com> destroy
    (localhost)http://localhost/> sessions
    en.wikipedia.org
    localhost
```

#### exit

```bash
    (wikipedia)http://en.wikipedia.org> exit
```

## Versions

0.0.9 :

      - simpler, better session handling
      - request data is assumed to be a python object.  passed as string otherwise.

0.0.8 :

      - better host handling
      - switched content/head/status from booleans to showing results of last response

0.0.7 :

      - renamed to 'requepl'

0.0.6 :

      - added host prefix on session-by-session basis

0.0.5 :

      - readline working on macosx
      - added a bunch of completions, including http://[www.] and common request headers
      - fixed reverse-argument bug
      - added setup.py install support

0.0.4 :

      - can set request headers on session-by-session basis

0.0.3 :

      - can request data

0.0.2 :

      - proper executable, docs are there.

0.0.1 :

      - does put, post, get, delete, and head.

## License

The GPLv3.  See LICENSE.txt.