from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button

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