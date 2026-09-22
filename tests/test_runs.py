# This file is part of HereIsYou
# Copyright (C) 2026 Donald Raymond Reilly Jr.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from hereisyou import You
from dubslib.path import (
                                add_date_time,
                                add_version,
                                ensure_path,
                                get_object_name,
                                _get_module_version,
                                _get_package_version
                                )
from dubslib.io import Persistence
from dubslib.mockclasses import (
                        GoldenClass, 
                        DescriptorExample, 
                        GoldenBase,
                        MiniDesktopApp
                        )
from pathlib import Path

def create_inspection(object_to_inspect):

    new_inspector = You()
    new_inspection = new_inspector(object_to_inspect)

    return new_inspection
   
def create_file_path(object_to_inspect):
     
    object_name = get_object_name(object_to_inspect)

    you_version_number = "Version_" + _get_package_version("HereIsYou")
    try:
        object_version = "Version_" + _get_module_version(object_to_inspect)
    except:
        object_version = "Unversioned_Object"
    folder = add_date_time(None, month = True, day = True, year = True)
    file_name = add_date_time(object_name, hour = True, minute = True, 
                              extension = ".json")

    new_inspection_file_name = Path(__file__).parents[0] / "HereIsYou" / you_version_number / object_name/ object_version / folder / file_name 

    return new_inspection_file_name
def new_inspection(object_to_inspect):
    persist = Persistence()
    inspection = create_inspection(object_to_inspect)
    
    file_path = create_file_path(object_to_inspect)

    ensure_path(file_path)

    persist.to_file(inspection, file_path, "json")

if __name__ == "__main__":

    classes_to_inspect = (DescriptorExample, GoldenBase, GoldenClass, MiniDesktopApp, You, int, str, object, __builtins__)

    for obj_to_inspect in classes_to_inspect:
        new_inspection(obj_to_inspect)
