# curlpl

An HTTP repl with multiple sessions.

Wraps the Python [requests](http://pypi.python.org/pypi/requests) library.

---

## Installation

    $ git clone https://talos@github.com/talos/curlpl.git
    $ cd curlpl
    $ python setup.py install

---

## Usage

    $ curlpl

#### Help:

    curlpl(default)> help

    Documented commands (type help <topic>):
    ========================================
    clear    delete  head  put              response_headers  set   
    content  exit    help  quit             session           status
    cookies  get     post  request_headers  sessions          unset 

#### HTTP Requests:

    curlpl(default)> get http://www.google.com/
    curlpl(default)> post http://www.google.com/ [data]
    curlpl(default)> put http://www.google.com/ [data]
    curlpl(default)> delete http://www.google.com/ [data]

#### Show cookies:

    curlpl(default)> cookies
    { 'NID': '53=pkOV_ZXWlXa_qUM6pf4QeRsUrPdAXQW8Wbgk8KO3iNKTkvUb7M5DAOMsIB0k4Eqeya2Q_vM2hfjFOiAisa8yVpQptw_GAI_mxM7QHe3UeBVgaAsoL3cU3PUH979wRyTC',
      'PREF': 'ID=ca5f1679b1acda32:FF=0:TM=1323388356:LM=1323388356:S=EUiHGMVX1R5dshxv'}

#### New session:

    curlpl(default)> session other
    curlpl(other)> cookies
    { }

#### Show available sessions:

     curlpl(default)> sessions
     default
     other

#### Exit:

     curlpl(default)> exit

---

## Versions

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

---

## License

The GPLv3.  See LICENSE.txt.