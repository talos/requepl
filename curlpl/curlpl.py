#/usr/bin/env/python

# curlpl -- http repl with sessions
# Copyright (C) 2011  John Krauss
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
    import requests # currently depends on requests library.  eventually curl?
    from requests.exceptions import RequestException
except ImportError:
    print "You must install the requests library to use curlpl."
    print "http://docs.python-requests.org/en/latest/user/install/#install"
    exit(0)
import cmd

'''This is the name of the session the user begins with.'''
DEFAULT_SESSION_NAME = 'default'


def safe_request(func):
    """Prevent request error from killing the repl.
    """
    def wrapped(*args):
        try:
            return func(*args)
        except RequestException as e:
            print "Error requesting: %s" % e
        except ValueError as e:
            print "Error requesting: %s" %e

    return wrapped


class Curlpl(cmd.Cmd):
    """Curlpl provides an HTTP repl with switchable sessions.
    """

    def __init__(self):
        """Initialize Curlpl
        """
        #super(Curlpl, self).__init__('\t') # use tab for readline
        cmd.Cmd.__init__(self, '\t')
        self.prompt = "curlpl$ "
        self.sessions = {}
        self.do_session(DEFAULT_SESSION_NAME)

    def _print_response(self, response, status_code, headers, content):
        """Print responses from http requests consistently.
        """
        if status_code:
            print response.status_code

        if headers:
            print response.headers

        if content:
            print response.content

    def do_session(self, session_name):
        """Enter a session called `session_name`.  Reenters a session
        if such a session already exists.  Without arguments, tells
        you which session you're currently in.
        """
        if session_name:
            # Use the existing session if possible.
            if self.sessions.has_key(session_name):
                self.session = self.sessions[session_name]
            else:
                self.session = requests.session()
                self.sessions[session_name] = self.session

            self.session_name = session_name

        print "In session %s" % self.session_name

    def do_sessions(self, line):
        """List the available sessions.
        """
        print self.sessions

    def do_clear(self, line):
        """Clear the current session's state.
        """
        self.session = requests.session()  # should this be an
                                           # @property instead?
        self.sessions[self.session_name] = self.session

        print "Cleared session %s" % self.session_name

    def do_cookies(self, line):
        """Show the cookies for the current session's cookie jar.
        """
        print self.session.cookies

    @safe_request
    def do_head(self, url):
        """Synchronously get the specified [url]
        """
        self._print_response(self.session.head(url), True, True, False)

    @safe_request
    def do_get(self, url):
        """Synchronously get the specified [url]
        """
        self._print_response(self.session.get(url), True, False, True)

    @safe_request
    def do_post(self, url):
        """Synchronously post to the specified [url].
        """
        self._print_response(self.session.post(url), True, False, True)

    @safe_request
    def do_put(self, url):
        """Synchronously put to the specified [url].
        """
        self._print_response(self.session.put(url), True, False, True)

    @safe_request
    def do_delete(self, url):
        """Synchronously delete the specified [url].
        """
        self._print_response(self.session.delete(url), True, False, True)

    def do_exit(self, line):
        """Exit the repl.
        """
        return self.do_EOF(line)

    def do_quit(self, line):
        """Exit the repl.
        """
        return self.do_EOF(line)

    def do_EOF(self, line):
        """Exit the repl.
        """
        return True

if __name__ == '__main__':
    Curlpl().cmdloop()
