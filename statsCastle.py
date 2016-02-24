from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty

class StatsCastle():
	def __init__(self):
		self.bois=0
		self.fer=0
		self.nourriture=0
		self.gain_bois=1
		self.gain_fer=1
		self.gain_nourriture=1

		