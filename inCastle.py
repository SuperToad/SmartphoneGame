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

import castle 
import statsCastle
import placementBatiment

Builder.load_file('worldmap.kv')

#Cette classe est la classe principale permettant l'affichage de l'interieur d'un chateau

class InCastle(Widget) :
	boisLabel = ObjectProperty() #Un affichage pour le bois
	ferLabel = ObjectProperty() #Un affichage pour le fer
	nourritureLabel = ObjectProperty() #Un affichage pour la nourriture
	cc = ObjectProperty(statsCastle.StatsCastle()) #Un objet de type statsCastle stockant l'evolution des stats du chateau
	batimentActuel = "nope" #Une variable stockant le type de batiment que l'on est en train de creer
	fenetre = Popup(title="Construction") #Une fenetre popup pour le menu de construction
	nbFermes = NumericProperty()
	nbMines = NumericProperty()
	nbScieries = NumericProperty()

	def __init__(self):
		super(InCastle, self).__init__()
		#On initialise les clocks 
		Clock.schedule_interval(self.increment_bois, 1.0)
		Clock.schedule_interval(self.increment_fer, 1.0)
		Clock.schedule_interval(self.increment_nourriture, 1.0)
		self.batimentActuel = "nope"
		self.placementBatiment = ObjectProperty()
		self.nbFermes = 0;
		self.nbMines = 0;
		self.nbScieries = 0;

	def ouvrirMenuConstruction(self):
		#Placement des differents widget dans la Popup grace a des layouts
		print("fonction OuvrirMenuConstruction")
		box = BoxLayout(orientation='vertical')
		stack = StackLayout()
		fermer = Button(text="Fermer", font_size=20)
		scierie = Button(size_hint=(0.2, 0.2), background_normal = 'images/scierie.png')
		mine = Button(size_hint=(0.2, 0.2), background_normal = 'images/mine.png')
		ferme = Button(size_hint=(0.2, 0.2), background_normal = 'images/ferme.png')
		scierie.disabled = True
		mine.disabled = True
		ferme.disabled = True
		self.fenetre = Popup(title="Construction")
		
		if(self.cc.bois >= 50 and self.cc.fer >= 20):
			scierie.disabled = False
			
		if(self.cc.bois >= 20 and self.cc.fer >= 50):
			mine.disabled = False
			
		if(self.cc.bois >= 50 and self.cc.fer >= 50):
			ferme.disabled = False
			
		stack.add_widget(scierie)
		stack.add_widget(mine)
		stack.add_widget(ferme)
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
		self.fenetre.open()
	
	
	#Les fonctions d'incrementation de sressources
	def increment_bois(self, dt):
		self.cc.bois = self.cc.bois + self.cc.gain_bois
		#self.boisLabel.text = self.cc.bois

	def increment_fer(self, dt):
		self.cc.fer = self.cc.fer + self.cc.gain_fer
		#self.ferLabel.text = self.cc.fer

	def increment_nourriture(self, dt):
		self.cc.nourriture = self.cc.nourriture + self.cc.gain_nourriture
		#self.nourritureLabel = self.cc.nourriture


	#La fonction de construction
	def construire(self, typeBatiment):
		print("fonction construire")
		self.batimentActuel = typeBatiment
		self.placementBatiment = placementBatiment.PlacementBatiment(self)
		placementBatiment.active = True
		if typeBatiment == "scierie":
			self.cc.gain_bois = self.cc.gain_bois + 1
			self.nbScieries+=1
			self.cc.bois-=50
			self.cc.fer-=20
		elif typeBatiment == "mine":
			self.cc.gain_fer = self.cc.gain_fer + 1
			self.nbMines+=1
			self.cc.bois-=20
			self.cc.fer-=50
		elif typeBatiment == "ferme":
			self.cc.gain_nourriture = self.cc.gain_nourriture + 1
			self.nbFermes+=1
			self.cc.bois-=50
			self.cc.ferme-=50
		self.fenetre.dismiss()
		
