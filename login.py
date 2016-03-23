import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.properties import ObjectProperty, StringProperty 
from kivy.storage.jsonstore import JsonStore

import worldmap
import inCastle 

Builder.load_file('login.kv')

store = JsonStore('users.json')

class NewUser(BoxLayout):
	status = ObjectProperty(None)
	def validate(self, username, password, passwordConfirm):
		if (store.exists(username)):
			self.status.text="Nom d'utilisateur deja utilise"
		elif(password == passwordConfirm):
			store.put(username, nom=username, mdp=password, bois=0, fer=0, nourriture=0, gainBois=1, gainFer=1, gainNourriture=1, nbFermes=0, nbMines=0, nbScieries=0, nbCasernes=0, nbSoldats=0, nbSoldatsMax=0)
			self.clear_widgets()
			w = Login()
			self.add_widget(w)
		else:
			self.status.text="Veuillez remplir tous les champs"
	def retour(self):
		self.clear_widgets()
		w = Login()
		self.add_widget(w)

	
class Login(BoxLayout):
	status = ObjectProperty(None)
	def validate(self, username, password):
		if (store.exists(username)):
			if(password != store.get(username)['mdp']):
				self.status.text="Mot de passe incorect !"
			elif(password == store.get(username)['mdp']):
				self.clear_widgets()
				w = inCastle.InCastle(username, password)
				self.add_widget(w)
		else:
			self.status.text="Nom d'utilisateur ou mot de passe incorrect !"
			
	def nouveau(self):
		self.clear_widgets()
		w = NewUser()
		self.add_widget(w)
			

