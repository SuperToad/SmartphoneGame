from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty
from kivy.lang import Builder 

Builder.load_file('inside_castle.kv')

class Inside_castle(Widget):
	# List of the castles in the map
	building_list = ListProperty([])
	level = NumericProperty(1)
	castle = ObjectProperty()
	
	def __init__(self, castle):
		super(Inside_castle, self).__init__()
		print ("Inside castle lvl", castle.level)
		self.castle = castle