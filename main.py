from kivy.app import App
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

from castle import Castle

# Widget class
class WorldMap(Widget):
	# List of the castles in the map
	castle_list = ListProperty([])
	
	def on_touch_up(self, touch):
		coord = (touch.x -25, touch.y -25)
		# Determine if the place is already taken
		place = True
		for castle in self.castle_list:
			if  castle.x - 25 < touch.x < castle.x + 75 and castle.y - 25 < touch.y < castle.y + 75:
				place = False
		if place:
			# Creation of a new castle
			newCastle = Castle(coord)
			self.castle_list.append(newCastle)
			# Make the new castle show up on the map
			self.add_widget(newCastle)
			newCastle.active = True
			# Add a ressource point every second to the castle
			Clock.schedule_interval(newCastle.increment_ressources, 1.0)
		else:
			print ("Place taken")
	
	# Failed attempt to "move" the screen
	# Maybe we need to create a canvas or something and then move it
	def on_touch_move(self, move):
		self.pos = move.pos
		print (move.pos)
		

# App class
class GameApp(App):
	
	def build(self):
		map = WorldMap()
		return map


if __name__ == '__main__':
	GameApp().run()