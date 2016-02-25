from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty, BooleanProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.label import Label
 
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
        print("blbl")
 
    def increment_bois(self, dt):
        self.cc.bois = self.cc.bois + self.cc.gain_bois
        #self.boisLabel.text = self.cc.bois
 
    def increment_fer(self, dt):
        self.cc.fer = self.cc.fer + self.cc.gain_fer
        #self.ferLabel.text = self.cc.fer
 
    def increment_nourriture(self, dt):
        self.cc.nourriture = self.cc.nourriture + self.cc.gain_nourriture
        #self.nourritureLabel = self.cc.nourriture