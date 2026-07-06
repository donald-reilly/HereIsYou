from utilities.custom_class import DescriptorExample, GoldenBase, GoldenClass
from utilities.tkinter_window import MiniDesktopApp
from HereIsYou import You
from pprint import pprint

cls_definitions = (MiniDesktopApp, DescriptorExample, GoldenBase, GoldenClass)

cls_instances = (
    MiniDesktopApp(),
    DescriptorExample(name = "test_name"), 
    GoldenBase(), 
    GoldenClass()
    )

inspector = You()

def test_class(test_definition):
        
        try:
            name = test_definition.__qualname__
            return name, inspector(test_definition)
        
        except AttributeError:
            name = test_definition.__class__.__qualname__
            return name, inspector(test_definition)

def inspect_class():
    """
    Damn my dumb ass brain us making this so much harder than it needs to be.
    Grow up bro, stop over complicating shit all the time.
    This isn't even hard, why you being dumb.
    """
    for total_test in range(0, 4):

        name, inspection = test_class(cls_definitions[total_test])
        def_inspections[name] = inspection

        name, inspection = test_class(cls_instances[total_test])
        instance_inpsect[name] = inspection

instance_inpsect = {}
def_inspections = {} 

inspections = {
     "Instance Inspections": instance_inpsect,
     "Definition Inspections": def_inspections
}
inspect_class()

