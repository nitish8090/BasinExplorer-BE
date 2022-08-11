import os

wsgi_app = 'BasinExplorerBE.wsgi'
daemon = True
workers = 2
pidfile = "BasinExplorerBE.pid"
bind = '127.0.0.1:50003'

# Other configuration
os.environ['DEBUG'] = 'False'
