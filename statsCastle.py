from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty

class StatsCastle(Widget):
	bois = NumericProperty(0)
	fer = NumericProperty(0)
	nourriture = NumericProperty(0)
	gain_bois = NumericProperty(1)
	gain_fer = NumericProperty(1)
	gain_nourriture = NumericProperty(1)
	def __init__(self):
		pass

		