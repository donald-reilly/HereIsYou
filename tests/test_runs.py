from FilePaths.file_paths import add_date_time, add_version
from HereIsYou import You

from utilities.custom_class import DescriptorExample, GoldenBase, GoldenClass
from utilities.tkinter_window import MiniDesktopApp

from pathlib import Path
from importlib.metadata import metadata

def get_object_name(object_to_inspect):

    try:
        object_name = object_to_inspect.__name__
        return object_name

    except AttributeError:
        object_name = object_to_inspect.__class.__name__
        return object_name

def create_inspection(object_to_inspect):

    new_inspector = You()
    new_inspection = new_inspector(object_to_inspect)

    object_name = get_object_name(object_to_inspect)

    folder = add_date_time(None, month = True, day = True, year = True)
    file_name = add_date_time(object_name, hour = True, minute = True) + ".md"

    new_inspection_file_name = Path(__file__).parents[0] /folder / file_name 

    return new_inspection, new_inspection_file_name

if __name__ == "__main__":
    new_inspection, new_inspection_file_name = create_inspection(MiniDesktopApp)
    print(new_inspection_file_name)
   
