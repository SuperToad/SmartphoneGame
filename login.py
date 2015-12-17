import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.properties import ObjectProperty, StringProperty 

import worldmap

Builder.load_file('login.kv')

class Login(BoxLayout):
	status = ObjectProperty(None)
	def validate(self, username, password):
		if username == "test" and password == "test":
			self.clear_widgets()
			w = worldmap.WorldMap()
			self.add_widget(w)
		else:
			self.status.text="Nom d'utilisateur ou mot de passe incorrect !"