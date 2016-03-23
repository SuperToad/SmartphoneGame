from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty
from kivy.lang import Builder 
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.storage.jsonstore import JsonStore
from kivy.uix.dropdown import DropDown
import random

import castle 
import placementBatiment

Builder.load_file('worldmap.kv')
store = JsonStore('users.json')

#Cette classe est la classe principale permettant l'affichage de l'interieur d'un chateau

class InCastle(Widget) :
	boisLabel = ObjectProperty() #Un affichage pour le bois
	ferLabel = ObjectProperty() #Un affichage pour le fer
	nourritureLabel = ObjectProperty() #Un affichage pour la nourriture
	fenetre = Popup(title="Construction") #Une fenetre popup pour le menu de construction
	fenetreAttaque = Popup(title="Attaque")
	fenetreResultat = Popup(title="Resultat")
	nbFermes = NumericProperty()
	nbMines = NumericProperty()
	nbScieries = NumericProperty()
	nbCasernes = NumericProperty()
	nbSoldats = NumericProperty()
	nbSoldatsMax = NumericProperty()
	bois = NumericProperty()
	fer = NumericProperty()
	nourriture = NumericProperty()
	gain_bois = NumericProperty()
	gain_fer = NumericProperty()
	gain_nourriture = NumericProperty()
	utilisateur = StringProperty()
	mdp = StringProperty()

	def __init__(self, username, password):
		super(InCastle, self).__init__()
		#On initialise les clocks 
		Clock.schedule_interval(self.increment_bois, 1.0)
		Clock.schedule_interval(self.increment_fer, 1.0)
		Clock.schedule_interval(self.increment_nourriture, 1.0)
		Clock.schedule_interval(self.synchro, 1.0)
		self.nbFermes = store.get(username)['nbFermes']
		self.nbMines = store.get(username)['nbMines']
		self.nbScieries = store.get(username)['nbScieries']
		self.nbCasernes = store.get(username)['nbCasernes']
		self.nbSoldats = store.get(username)['nbSoldats']
		self.nbSoldatsMax = store.get(username)['nbSoldatsMax']
		self.bois = store.get(username)['bois']
		self.fer = store.get(username)['fer']
		self.nourriture = store.get(username)['nourriture']
		self.gain_bois = store.get(username)['gainBois']
		self.gain_fer = store.get(username)['gainFer']
		self.gain_nourriture = store.get(username)['gainNourriture']
		self.utilisateur = username
		self.mdp = password

	def ouvrirMenuConstruction(self):
		#Placement des differents widget dans la Popup grace a des layouts
		print("fonction OuvrirMenuConstruction")
		box = BoxLayout(orientation='vertical')
		stack = StackLayout()
		fermer = Button(text="Fermer", font_size=20)
		scierie = Button(text="Scierie :\n 50 Bois, 20 Fer", size_hint=(0.2, 0.2), background_normal = 'images/scierie.png')
		mine = Button(text="Mine :\n 20 Bois, 50 Fer", size_hint=(0.2, 0.2), background_normal = 'images/mine.png')
		ferme = Button(text="Ferme :\n 50 Bois, 50 Fer", size_hint=(0.2, 0.2), background_normal = 'images/ferme.png')
		caserne = Button(text="Caserne:\n 100 Bois, 100 Fer", size_hint=(0.2, 0.2), background_normal = 'images/caserne.png')
		scierie.disabled = True
		mine.disabled = True
		ferme.disabled = True
		caserne.disabled = True
		self.fenetre = Popup(title="Construction")
		
		if(self.bois >= 50 and self.fer >= 20):
			scierie.disabled = False
			
		if(self.bois >= 20 and self.fer >= 50):
			mine.disabled = False
			
		if(self.bois >= 50 and self.fer >= 50):
			ferme.disabled = False
			
		if(self.bois >= 100 and self.fer >= 100):
			caserne.disabled = False
			
		stack.add_widget(scierie)
		stack.add_widget(mine)
		stack.add_widget(ferme)
		stack.add_widget(caserne)
		box.add_widget(stack)
		box.add_widget(fermer)
		self.fenetre.add_widget(box)
		fermer.size_hint=(1,.1)
		fermer.bind(on_press= self.fenetre.dismiss)
		
		#Lorsqu'on appuie sur une des constructions possibles, on appelle la fonction construire
		# et on y passe le type de batiment en parametre
		scierie.bind(on_press=lambda x:self.construire("scierie"))
		mine.bind(on_press=lambda x:self.construire("mine"))
		ferme.bind(on_press=lambda a:self.construire("ferme"))
		caserne.bind(on_press=lambda a:self.construire("caserne"))
		self.fenetre.open()
	
	def ouvrirMenuAttaque(self):
		box = BoxLayout(orientation='vertical')
		self.fenetreAttaque = Popup(title="Attaque")
		dropdown = DropDown()
		stats = Label(text='Veuillez selectionner une cible')
		confirm = Button(text="Voir")
		attaquer = Button(text="Attaquer")
		
		for key in store:
			btn = Button(text=store.get(key)['nom'], size_hint_y=None, height=44)
			btn.bind(on_release=lambda btn: dropdown.select(btn.text))  
			dropdown.add_widget(btn)
		mainbutton = Button(text='Cible :', size_hint=(None, None))
		mainbutton.bind(on_release=dropdown.open)
		dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
		box2 = BoxLayout(orientation='horizontal')
		
		fermer = Button(text="Fermer", font_size=20)
		box.add_widget(mainbutton)
		box.add_widget(stats)
		box2.add_widget(confirm)
		box2.add_widget(attaquer)
		box.add_widget(box2)
		box.add_widget(fermer)
		self.fenetreAttaque.add_widget(box)
		mainbutton.size_hint=(1,.1)
		confirm.size_hint=(.1,.1)
		fermer.size_hint=(1,.1)
		attaquer.size_hint=(.1,.1)
		confirm.bind(on_press=lambda x: self.actualise(stats, mainbutton.text))
		attaquer.bind(on_press=lambda x: self.attaque(mainbutton.text))
		fermer.bind(on_press=self.fenetreAttaque.dismiss)
		self.fenetreAttaque.open()
		
	def actualise(self, stats, actuel):
		if (actuel == "Cible :"):
			stats.text="Veuillez selectionner une cible"
		else:
			stats.text="Bois : " + str(store.get(actuel)['bois']) + "\nFer : " + str(store.get(actuel)['fer']) + "\nNourriture : " + str(store.get(actuel)['nourriture']) + "\nSoldats :" + str(store.get(actuel)['nbSoldats'])
		
	def attaque(self, actuel):
		combatAttaquant = (store.get(self.utilisateur)['nbSoldats']*2)+store.get(self.utilisateur)['nourriture']
		combatDefenseur = (store.get(actuel)['nbSoldats']*2)+store.get(actuel)['nourriture']
		proba = combatAttaquant/combatDefenseur
		rand = random.randint(0, 10)
		if(rand > proba):
			fermer = Button(text="Fermer")
			self.fenetreResultat = Popup(title="Resultat")
			box = BoxLayout(orientation='vertical')
			gainBois = random.randint(0, rand)*10
			gainFer = random.randint(0, rand)*10
			gainNourriture = random.randint(0, rand)*10
			store[self.utilisateur] = {'nom': self.utilisateur, 'mdp': self.mdp, 'bois': self.bois-gainBois, 'fer': self.fer-gainFer, 'nourriture':self.nourriture+gainNourriture, 'gainBois': self.gain_bois, 'gainFer': self.gain_fer, 'gainNourriture': self.gain_nourriture, 'nbFermes': self.nbFermes, 'nbMines': self.nbMines, 'nbScieries': self.nbScieries, 'nbCasernes': self.nbCasernes, 'nbSoldats': self.nbSoldats, 'nbSoldatsMax': self.nbSoldatsMax}
			store[actuel] = {'nom': actuel, 'mdp': self.mdp, 'bois': store.get(actuel)['bois']- gainBois, 'fer': store.get(actuel)['fer']- gainFer, 'nourriture': store.get(actuel)['nourriture']- gainNourriture, 'gainBois': self.gain_bois, 'gainFer': self.gain_fer, 'gainNourriture': self.gain_nourriture, 'nbFermes': self.nbFermes, 'nbMines': self.nbMines, 'nbScieries': self.nbScieries, 'nbCasernes': self.nbCasernes, 'nbSoldats': self.nbSoldats, 'nbSoldatsMax': self.nbSoldatsMax}
			self.bois += gainBois
			self.fer += gainFer
			self.nourriture += gainNourriture 
			label = Label(text =  "Vous avez gagne! \n+" + str(gainBois) + " Bois\n+" + str(gainFer) + "Fer\n+" + str(gainNourriture) + "Nourriture")
			box.add_widget(label)
			fermer = Button(text="Fermer")
			fermer.size_hint=(1,.1)
			box.add_widget(fermer)
			self.fenetreResultat.add_widget(box)
			fermer.bind(on_press=self.fenetreResultat.dismiss)
			self.fenetreResultat.open()
		else:
			self.fenetreResultat = Popup(title="Resultat")
			box = BoxLayout(orientation='vertical')
			perteBois = random.randint(0, rand)*10
			perteFer = random.randint(0, rand)*10
			perteNourriture = random.randint(0, rand)*10
			store[self.utilisateur] = {'nom': self.utilisateur, 'mdp': self.mdp, 'bois': self.bois-perteBois, 'fer': self.fer-perteFer, 'nourriture':self.nourriture-perteNourriture, 'gainBois': self.gain_bois, 'gainFer': self.gain_fer, 'gainNourriture': self.gain_nourriture, 'nbFermes': self.nbFermes, 'nbMines': self.nbMines, 'nbScieries': self.nbScieries, 'nbCasernes': self.nbCasernes, 'nbSoldats': self.nbSoldats, 'nbSoldatsMax': self.nbSoldatsMax}
			self.bois -= perteBois
			self.fer -= perteFer
			self.nourriture -= perteNourriture 
			label = Label(text =  "Vous avez perdu! \n-" + str(perteBois) + " Bois\n-" + str(perteFer) + "Fer\n-" + str(perteNourriture) + "Nourriture")
			box.add_widget(label)
			fermer = Button(text="Fermer")
			fermer.size_hint=(1,.1)
			box.add_widget(fermer)
			self.fenetreResultat.add_widget(box)
			fermer.bind(on_press=self.fenetreResultat.dismiss)
			self.fenetreResultat.open()
		
	
	#Les fonctions d'incrementation de sressources
	def increment_bois(self, dt):
		self.bois = self.bois + self.gain_bois
		#self.boisLabel.text = self.cc.bois

	def increment_fer(self, dt):
		self.fer = self.fer + self.gain_fer
		#self.ferLabel.text = self.cc.fer

	def increment_nourriture(self, dt):
		self.nourriture = self.nourriture + self.gain_nourriture
		#self.nourritureLabel = self.cc.nourriture


	#La fonction de construction
	def construire(self, typeBatiment):
		print("fonction construire")
		self.placementBatiment = placementBatiment.PlacementBatiment(self)
		placementBatiment.active = True
		if typeBatiment == "scierie":
			self.gain_bois = self.gain_bois + 1
			self.nbScieries+=1
			self.bois-=50
			self.fer-=20
		elif typeBatiment == "mine":
			self.gain_fer = self.gain_fer + 1
			self.nbMines+=1
			self.bois-=20
			self.fer-=50
		elif typeBatiment == "ferme":
			self.gain_nourriture = self.gain_nourriture + 1
			self.nbFermes+=1
			self.bois-=50
			self.fer-=50
		elif typeBatiment == "caserne":
			self.nbSoldatsMax += 10
			self.nbCasernes += 1
			self.bois -= 100
			self.fer -= 100
		self.fenetre.dismiss()
		
	def formerSoldat(self):
		print 'formerSoldat' 
		if(self.nbSoldats+1 <= self.nbSoldatsMax and self.nbCasernes > 0):
			self.nbSoldats += 1
			self.nourriture -= 10
			
	def synchro(self, dt):
		store[self.utilisateur] = {'nom': self.utilisateur, 'mdp': self.mdp, 'bois': self.bois, 'fer': self.fer, 'nourriture':self.nourriture, 'gainBois': self.gain_bois, 'gainFer': self.gain_fer, 'gainNourriture': self.gain_nourriture, 'nbFermes': self.nbFermes, 'nbMines': self.nbMines, 'nbScieries': self.nbScieries, 'nbCasernes': self.nbCasernes, 'nbSoldats': self.nbSoldats, 'nbSoldatsMax': self.nbSoldatsMax}
