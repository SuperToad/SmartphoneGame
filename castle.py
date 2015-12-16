from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label

class Castle(Image):
	x = NumericProperty(0)
	y = NumericProperty(0)
	
	def __init__(self, test = (0, 0), image = "images/castle.png", **kwargs):
		self.source = image
		super(Castle, self).__init__(**kwargs)
		self.size = (60, 50)
		self.x = test[0]
		self.y = test[1]
		print ("New Castle", test)
	