from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty

import castle

class WorldMap(Widget):
	# List of the castles in the map
	castle_list = ListProperty([])
	
	def on_touch_up(self, touch):
		coord = (touch.x -25, touch.y -25)
		# Determine if the place is already taken
		place = True
		for c in self.castle_list:
			if  c.x - 25 < touch.x < c.x + 75 and c.y - 25 < touch.y < c.y + 75:
				place = False
		if place:
			# Creation of a new castle
			newCastle = castle.Castle(coord)
			self.castle_list.append(newCastle)
			# Make the new castle show up on the map
			self.add_widget(newCastle)
			newCastle.active = True
			# Add a ressource point every second to the castle
			Clock.schedule_interval(newCastle.increment_ressources, 1.0)
		else:
			print ("Place taken")