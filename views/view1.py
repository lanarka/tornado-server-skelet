import time
import tornado
import logging
logger = logging.getLogger(__name__)


#Single threaded
class Handler1(tornado.web.RequestHandler):

  def get(self):
    logger.debug("View1")
    time.sleep(0.5)
    self.write('Hello from View1')
