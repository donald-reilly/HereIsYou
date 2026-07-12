
from pprint import pprint

class Parser:
    """
    Parser: Extracts meta data from python objects.

    This class parses python objects to provide clean and readable meta data.
    """

    def __init__(self) -> None:
        """
        Initializes the Parser class.
        """

        # The method dispatcher, currently not in use, would like to add for easy extension.
        self.dispatcher = {
            # "module": self.parse_module,
            # "class": self.parse_class,
            # "method": self.parse_method,
            "instance": self._parse_class_instance
            # "function": self.parse_function,
            # "property": self.parse_property
        }

    def __call__(self, object_to_parse, object_type=None) -> dict:
        """
        Parse an object of a given type and return a dictionary representation.

        Params:
            object_to_parse: The object to be parsed.
            object_type: The type of the object to be parsed.
        Returns:
            A dictionary representation of the parsed object.
        """

        return self._parse_object(
            object_to_parse=object_to_parse, object_type=object_type
        )

    def _parse_object(self, object_to_parse, object_type=None) -> dict:
        """Parse an object of a given type and return a dictionary representation

        Params:
            object_to_parse: The object to be parsed.
            object_type: The type of the object to be parsed.
        Returns:
            A dicitonary representation of the parsed object.

        """

        meta_data_dict = self._extract_meta_data(object_to_parse)
        if object_type in self.dispatcher:
            meta_data_dict |= self.dispatcher[object_type](object_to_parse)
        return meta_data_dict

    def _extract_meta_data(self, object_to_parse) -> dict:
        """
        Parse an object, extract meta-data and format it into a dictionary.

        Params:
            object_to_parse: The object to be parsed.
            object_type: The Name of the object to be parsed.
        Returns:
            A dictionary representation of the meta data.
        """

        # Calls to meta data to be extracted.
        meta_data_map = {
            "name": lambda: object_to_parse.__name__,  # Object name
            "qualified name": lambda: object_to_parse.__qualname__,  # Qualified object name
            "module name": lambda: object_to_parse.__module__,  # Objects module name
            "bases": lambda: object_to_parse.__bases__,  # Base class names
            "doc string": lambda: object_to_parse.__doc__,  # Doc String
            "type hints": lambda: object_to_parse.__annotations__,  #   type hinting of variables
        }
        meta_data_dict = {}  # Initializng the meta data dictionary.
        for (meta_data) in (meta_data_map):  # For loop that cycles the meta data map and updates the meta_data dict if an expection isn't encountred.
            try:
                meta_data_dict[meta_data] = meta_data_map[meta_data]()
            except:
                continue
        return meta_data_dict

    def _parse_class_instance(self, instance_to_parse) -> dict:
        """
        Parse an instance of a class and return a dictionary representation of it.

        Params:
            instance_to_parse: The instance of a class to be parsed.
        Returns:
            A dictionary representation of the parsed instance of a class.
        """

        # Pulls the instance variables.
        instance_dict = {"Instance Variables": instance_to_parse.__dict__}
        return instance_dict

    def _parse_variables(self, function_to_parse) -> dict[str,  ]:
        """
        Parse the variables of a function.

        Params:
            function_to_parse: The functions whose variables need parsing.
        Returns:
            A dictionary representation of the parsed variables.
        """

        allvars = function_to_parse.__code__.co_varnames
        argsn = function_to_parse.__code__.co_argcount
        anns = function_to_parse.__annotations__ or ()
        defs = function_to_parse.__defaults__ or ()
        ldegs = len(defs)
        localvar = allvars[argsn:]
        args = allvars[:argsn]

        templst = [None] * (argsn-ldegs)
        templst += defs

        variables_defaults = list(zip(args,templst))
        dict_laid_out =[]

        for item in variables_defaults:
                tempd = {
                    "name": item[0],
                    "default": item[1],
                    "type":anns[item[0]] if item[0] in anns else None
                }
                dict_laid_out.append(tempd)

        return dict_laid_out

