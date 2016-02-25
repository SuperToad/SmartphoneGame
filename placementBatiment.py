from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty

import inCastle
import batiment
class PlacementBatiment(Widget):
	def __init__(self, _castle):
		self.castle = _castle
		print("hfusg")

	def on_touch_down(self, pos):
		coord = (touch.x -25, touch.y -25)
		# Determine if the place is already taken
		place = True
		for c in castle.batiment_list:
			if  c.x - 25 < touch.x < c.x + 75 and c.y - 25 < touch.y < c.y + 75:
				place = False
		if place:
			batiment = batiment.Batiment(coord, castle.batimentActuel)
			castle.batiment_list.append(batiment)
			castle.add_widget(batiment)
			batiment.active = True
		else:
			print ("Place taken")