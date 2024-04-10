"""
	Server
"""
import tornado.web
from handlers import handlers

import logging
logger = logging.getLogger(__name__)

def start_server(port, proc):
	app = tornado.web.Application(handlers=handlers)
	http_server = tornado.httpserver.HTTPServer(app)
	logger.info("server listen... (port %s)" % port)
	http_server.listen(port)
	http_server.start(proc)
	try:
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		logger.critical("terminated by user")


if __name__ == '__main__':
	start_server(8080, 5)