from kivy.app import App

import worldmap 

class GameApp(App):
	def build(self):
		map = worldmap.WorldMap()
		return map