"""
This script runs the application using a development server.
"""

import bottle
import os
import sys

# routes contains the HTTP handlers for our server and must be imported.
import routes

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    @bottle.route('/')
    def main_page():
        return bottle.template('main_page')

    @bottle.route('/sochi')
    def sochi_page():
        return bottle.template('sochi_page')

    @bottle.route('/picunda')
    def picunda_page():
        return bottle.template('picunda_page')

    @bottle.route('/gelendzhik')
    def gelendzhik_page():
        return bottle.template('gelendzhik_page')

    @bottle.route('/reviews')
    def reviews():
        return bottle.template('reviews')


    # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=PORT)
