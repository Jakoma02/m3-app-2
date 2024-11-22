from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Subform2 import Subform2
from ..Subform1 import Subform1


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.navigation_link_1.

  def navigation_link_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.content.clear()
    self.content.add_component(Subform1())
    self.navigation_link_1.selected = True
    self.navigation_link_2.selected = False

  def navigation_link_2_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.content.clear()
    self.content.add_component(Subform2())
    self.navigation_link_1.selected = False
    self.navigation_link_2.selected = True
