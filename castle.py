from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import _hash
from kivy.animation import Animation
from kivy.graphics.vertex_instructions import *
from kivy.uix.boxlayout import BoxLayout

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
			# Create a CastleInfo popup with this castle as parameter
			castleInfo = CastleInfo(self)
			castleInfo.open()

class CastleInfo(Popup):
	castle = ObjectProperty()
	close_button = ObjectProperty()
	def __init__(self, _castle):
		self.castle = _castle
		self.close_button = Button()
		super(CastleInfo, self).__init__()
		self.close_button.bind(on_press = self.dismiss)
		self.pos = (Window.width/2 - self.width/2, Window.height/2 - self.height/2)
		self.box_layout.pos = self.pos
		self.box_layout.size = self.size
		
