## curlpl

http repl with multiple sessions

### usage

    $ curlpl
    In session `default`.

Help:

    curlpl$ help

    Documented commands (type help <topic>):
    ========================================
    clear  cookies  delete  exit  get  head  post  put  quit  session  sessions

Requests:

    curlpl$ get http://www.google.com/
    curlpl$ post http://www.google.com/
    curlpl$ put http://www.google.com/
    curlpl$ delete http://www.google.com/

Show cookies:

    curlpl$ cookies
    {'PREF': 'ID=a68f101929627f83:FF=0:TM=1323379784:LM=1323379784:S=6WQ0dct7sXgma5Vk', 'NID': '53=NebZVGGxTc0UUNrDn5DcDtXS4IjBD8pbyFVwRBqqxCsi924sLbLcSg72w7i-1gh8fllM13k6lG4OpK7y2BJbka8bUUQ1W--ynYda46HfR1Qy4vfQ91jF4ej_674eP-Fm'}

New session:

    curlpl$ session other
    In session `other`.
    curlpl$ cookies
    {}

Show available sessions:

     curlpl$ sessions
     default
     other

Exit:

     curlpl$ exit

---

### known issues

* no request data

---

### versions

0.0.2 : proper executable, docs are there.

0.0.1 : does put, post, get, delete, and head.
