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

import castle 
import statsCastle

Builder.load_file('inCastle.kv')

class InCastle(Widget) :
	boisLabel = ObjectProperty()
	ferLabel = ObjectProperty()
	nourritureLabel = ObjectProperty()
	cc = ObjectProperty(statsCastle.StatsCastle())

	def __init__(self):
		super(InCastle, self).__init__()
		Clock.schedule_interval(self.increment_bois, 1.0)
		Clock.schedule_interval(self.increment_fer, 1.0)
		Clock.schedule_interval(self.increment_nourriture, 1.0)

	def ouvrirMenuConstruction(self):
		box = BoxLayout(orientation='vertical')
		grid = GridLayout(cols=3, row_default_height=40)
		fermer = Button(text="Fermer", font_size=20)
		scierie = Button(text="scierie")
		mine = Button(text="mine")
		ferme = Button(text="ferme")
		fenetre = Popup(title="Construction")
		grid.add_widget(scierie)
		grid.add_widget(mine)
		grid.add_widget(ferme)
		box.add_widget(grid)
		box.add_widget(fermer)
		fenetre.add_widget(box)
		fermer.size_hint=(1,.1)
		fermer.bind(on_press=fenetre.dismiss)
		fenetre.open()

	def increment_bois(self, dt):
		self.cc.bois = self.cc.bois + self.cc.gain_bois
		#self.boisLabel.text = self.cc.bois

	def increment_fer(self, dt):
		self.cc.fer = self.cc.fer + self.cc.gain_fer
		#self.ferLabel.text = self.cc.fer

	def increment_nourriture(self, dt):
		self.cc.nourriture = self.cc.nourriture + self.cc.gain_nourriture
		#self.nourritureLabel = self.cc.nourriture

	def construire(type):
		pass
