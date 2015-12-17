from kivy.app import App

import login 

class GameApp(App):
	def build(self):
		l = login.Login()
		return l