# requepl

An HTTP repl with multiple sessions.

Wraps the Python [requests](http://pypi.python.org/pypi/requests) library.

## Installation

    $ git clone https://talos@github.com/talos/requepl.git
    $ cd requepl
    $ python setup.py install

## Usage

    $ requepl

#### Help:

    requepl(default)> help

    Documented commands (type help <topic>):
    ========================================
    clear    delete  head  put              response_headers  set   
    content  exit    help  quit             session           status
    cookies  get     post  request_headers  sessions          unset 

#### HTTP Requests:

    requepl(default)> get http://www.google.com/
    requepl(default)> post http://www.google.com/ [data]
    requepl(default)> put http://www.google.com/ [data]
    requepl(default)> delete http://www.google.com/ [data]

#### Show cookies:

    requepl(default)> cookies
    { 'NID': '53=pkOV_ZXWlXa_qUM6pf4QeRsUrPdAXQW8Wbgk8KO3iNKTkvUb7M5DAOMsIB0k4Eqeya2Q_vM2hfjFOiAisa8yVpQptw_GAI_mxM7QHe3UeBVgaAsoL3cU3PUH979wRyTC',
      'PREF': 'ID=ca5f1679b1acda32:FF=0:TM=1323388356:LM=1323388356:S=EUiHGMVX1R5dshxv'}

#### New session:

    requepl(default)> session other
    requepl(other)> cookies
    { }

#### Show available sessions:

     requepl(default)> sessions
     default
     other

#### Exit:

     requepl(default)> exit

## Versions

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