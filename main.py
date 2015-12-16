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
	
	def on_touch_up(self, touch):
		coord = (touch.x, touch.y)
		print ("Touched", coord)
		newCastle = Castle(coord)
		Clock.schedule_interval(newCastle.increment_ressources, 1.0)


class GameApp(App):
	
	def build(self):
		map = WorldMap()
		return map


if __name__ == '__main__':
	GameApp().run()