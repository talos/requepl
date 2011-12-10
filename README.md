# requepl

An HTTP repl with multiple sessions.

Wraps the Python [requests](http://pypi.python.org/pypi/requests) library.

## Installation

```bash
    $ git clone https://talos@github.com/talos/requepl.git
    $ cd requepl
    $ python setup.py install
```

## Usage

```bash
    $ requepl
    ***An HTTP repl with multiple sessions. Type `help` for a list of commands.
    (default)http://>
```

#### help

```bash
    (default)http://> help

    Documented commands (type help <topic>):
    ========================================
    clear    delete  head     host  quit             sessions    unset_header
    content  exit    headers  post  request_headers  set_header
    cookies  get     help     put   session          status
```

#### make a request

```bash
    (default)http://> get google.com
    http://google.com responded with `status` 200, 10 `headers`, and `content` of length 10344
```

#### observe the last response

```bash
    (default)http://> status
    200
```

```bash
    (default)http://> headers
    { 'cache-control': 'private, max-age=0',
      'content-type': 'text/html; charset=ISO-8859-1',
      'date': 'Sat, 10 Dec 2011 20:41:05 GMT',
      'expires': '-1',
      'p3p': 'CP="This is not a P3P policy! See http://www.google.com/support/accounts/bin/answer.py?hl=en&answer=151657 for more info."',
      'server': 'gws',
      'set-cookie': 'PREF=ID=15cf7e66d12d78c7:FF=0:TM=1323549665:LM=1323549665:S=DvB0IzisaNyEega5; expires=Mon, 09-Dec-2013 20:41:05 GMT; path=/; domain=.google.com, NID=53=TaQ28fcM7zqzvHccGCB2YuQWthS2lL8h2ojtjVuDNOSqpYKrCaUWEAIcHFzBDWx8dLjhhb2j7APh1zItl1fNtyN6I-RVyoW9x9uzRTcLe4OQad1n4sqBELjfcv8qHuCo; expires=Sun, 10-Jun-2012 20:41:05 GMT; path=/; domain=.google.com; HttpOnly',
      'transfer-encoding': 'chunked',
      'x-frame-options': 'SAMEORIGIN',
      'x-xss-protection': '1; mode=block'}
```

```bash
    (default)http://> content
    ...
```

#### observe session state

```bash
    (default)http://> cookies
    { 'NID': '53=TaQ28fcM7zqzvHccGCB2YuQWthS2lL8h2ojtjVuDNOSqpYKrCaUWEAIcHFzBDWx8dLjhhb2j7APh1zItl1fNtyN6I-RVyoW9x9uzRTcLe4OQad1n4sqBELjfcv8qHuCo',
      'PREF': 'ID=15cf7e66d12d78c7:FF=0:TM=1323549665:LM=1323549665:S=DvB0IzisaNyEega5'}
```

```bash
    (default)http://> request_headers
    { }
```

#### modify session state

```bash
    (default)http://> set_header User-Agent Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011-10-16 20:23:00
    { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011-10-16 20:23:00'}
```

```bash
    (default)http://> set_header Referer http://www.google.com/
    { 'Referer': 'http://www.google.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011-10-16 20:23:00'}
```

```bash
    (default)http://> unset_header User-Agent
    { 'Referer': 'http://www.google.com/'}
```

```bash
    (default)http://> request_headers
    { 'Referer': 'http://www.google.com/'}
```

```bash
    (default)http://> host google.com
    (default)http://google.com>
```

```bash
    (default)http://google.com> get /
    http://google.com/ responded with `status` 200, 10 `headers`, and `content` of length 10344
```

```bash
    (default)http://> clear
    Cleared current session.
```

#### switch to other sessions


```bash
    (default)> session wikipedia en.wikipedia.org
```

```bash
    (wikipedia)http://en.wikipedia.org> get /
    http://en.wikipedia.org/ responded with `status` 200, 14 `headers`, and `content` of length 54885
```

```bash
    (wikipedia)http://en.wikipedia.org> cookies
    { }
```

```bash
    (wikipedia)http://en.wikipedia.org> session nytimes nytimes.com
```

```bash
    (nytimes)http://nytimes.com> get /
    http://nytimes.com/ responded with `status` 200, 9 `headers`, and `content` of length 128667
```

```bash
    (nytimes)http://nytimes.com> cookies
    { 'RMID': '389d0d8135844ee3c5c18476', 'adxcs': 's*2ace1=0:1|s*2554d=0:1'}
```

```bash
    (nytimes)http://nytimes.com> sessions
    default
    wikipedia
    nytimes
```

```bash
    (nytimes)http://nytimes.com> session wikipedia
```

```bash
    (wikipedia)http://en.wikipedia.org> cookies
    { }
```

#### exit


```bash
     (default)http://google.com> quit
```

## Versions

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