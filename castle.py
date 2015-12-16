from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label

class Castle(Image):
	x = NumericProperty(0)
	y = NumericProperty(0)
	ressources = NumericProperty(0)
	
	def __init__(self, pos = (0, 0), image = "images/castle.png", **kwargs):
		self.source = image
		super(Castle, self).__init__(**kwargs)
		self.size = (50, 50)
		self.x = pos[0]
		self.y = pos[1]
		print ("New Castle", pos)
	
	def increment_ressources(self, dt):
		self.ressources = self.ressources + 1
		#print ("Ressources : ", self.ressources)

	def on_touch_down(self, touch):
		# For some reason, each time we touch the screen, ALL of the castles get this called
		# For now, we'll verify each time if each castle is touched
		if  self.x < touch.x < self.x + 50 and self.y < touch.y < self.y + 50:
			print ("Current ressources : ", self.ressources)
