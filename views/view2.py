import time
import tornado
from concurrent.futures import ThreadPoolExecutor
import logging
logger = logging.getLogger(__name__)


#Multithreading using tornado thread pool
class Handler2(tornado.web.RequestHandler):
  executor = ThreadPoolExecutor(4)

  @tornado.gen.coroutine
  def get(self):
    result = yield self.doing()
    self.write(result)

  @tornado.concurrent.run_on_executor
  def doing(self):
    time.sleep(.5)
    logger.warning("View2")
    return 'Hello from View2'
