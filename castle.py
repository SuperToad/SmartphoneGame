from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from functools import partial


import castleinfo

class Castle(Image):
	x = NumericProperty(0)
	y = NumericProperty(0)
	
	level = NumericProperty(1)
	ressources = NumericProperty(0)
	on_upgrade = BooleanProperty(False)
	
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
	
	# Level up
	# param is useless but for some reason we need two parameters
	# (param = the button who called the function)
	def level_up(self, param):
		if self.ressources >= 5*self.level and self.on_upgrade == False:
			param.disabled = True
			self.on_upgrade = True
			self.ressources = self.ressources - 5*self.level
			Clock.schedule_once(partial(self.do_up, param), 3.0 * self.level)
			
	def do_up(self, control, dt):
		self.level = self.level + 1
		self.on_upgrade = False
		control.disabled = False

	def on_touch_down(self, touch):
		# For some reason, each time we touch the screen, ALL of the castles get this called
		# For now, we'll verify each time if each castle is touched
		if  self.x < touch.x < self.x + 50 and self.y < touch.y < self.y + 50:
			print ("Current ressources : ", self.ressources)
			# Create a CastleInfo popup with this castle as parameter
			castleInfo = castleinfo.CastleInfo(self)
			castleInfo.open()
		
