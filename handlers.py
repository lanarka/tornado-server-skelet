"""
	Handlers
"""
from views.view1 import Handler1
from views.view2 import Handler2

handlers = (
	(r"/handler1", Handler1),
	(r"/handler2", Handler2)
)
