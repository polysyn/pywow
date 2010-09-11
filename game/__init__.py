# -*- coding: utf-8 -*-
"""
Game module
Contains model logic for the game
"""

# Colors
GREY   = 0x9d9d9d
WHITE  = 0xffffff
GREEN  = 0x1eff00
BLUE   = 0x0080ff
PURPLE = 0xb048f8
ORANGE = 0xff8000
GOLD   = 0xe5cc80

class Model(object):
	"""
	Base Model class for all the game models:
	Items, Spells, Quests, Talents, ...
	"""
	proxy = None
	
	@classmethod
	def initProxy(cls, proxy):
		cls.proxy = proxy(cls)
	
	def __init__(self, id):
		if not self.proxy:
			raise RuntimeError("%s.proxy needs to be initialized with initProxy(proxy)" % (self.__class__.__name__))
		self.id = id
		self.obj = self.proxy.get(id)
	
	def __getattr__(self, attr):
		if attr != "obj" and hasattr(self.obj, attr):
			return getattr(self.obj, attr)
		
		if attr != "proxy" and hasattr(self.proxy, attr):
			func = getattr(self.proxy, attr)
			return lambda: func(self.obj)
		
		return super(Model, self).__getattribute__(attr)
	
	def __repr__(self):
		if hasattr(self, "name"):
			return "<%s #%i: %s>" % (self.__class__.__name__, self.id, self.name)
		return "<%s #%i>" % (self.__class__.__name__, self.id)

class Tooltip(object):
	def __init__(self, obj, renderer):
		self.obj = obj
		self.renderer = renderer
		self.render()
	
	def append(self, name, text, color=WHITE):
		if text:
			self.keys.append(name)
			self.values.append(TooltipNode(name, text, color))

class TooltipNode(object):
	def __init__(self, name, text, color):
		self.name = name
		self.text = text
		self.color = color
	
	def __repr__(self):
		return repr(self.text)
	
	def __str__(self):
		return self.text
