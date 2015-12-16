from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label

from castle import Castle

class WorldMap(Widget):
	ressources = NumericProperty(0)
	
	def increment_ressources(self, dt):
		self.ressources = self.ressources + 1
	def on_touch_up(self, touch):
		test = (touch.x, touch.y)
		print ("Touched", test)
		newShip = Castle(test)


class GameApp(App):
	
	texture = ObjectProperty()
	
	def build(self):
		map = WorldMap()
		Clock.schedule_interval(map.increment_ressources, 1.0)
		return map


if __name__ == '__main__':
	GameApp().run()