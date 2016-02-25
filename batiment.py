from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty
from kivy.uix.image import Image


class Batiment(Image):
	x = NumericProperty(0)
	y = NumericProperty(0)
	def __init__(self, pos, typeBatiment, **kwargs):
		if typeBatiment == "scierie":
			self.source =  "images/scierie.png"
		elif typeBatiment == "mine":
			self.source =  "images/mine.png"
		elif typeBatiment == "ferme":
			self.source =  "images/ferme.png"
		super(Batiment, self).__init__(**kwargs)
		self.size = (50, 50)
		self.x = pos[0]
		self.y = pos[1]
