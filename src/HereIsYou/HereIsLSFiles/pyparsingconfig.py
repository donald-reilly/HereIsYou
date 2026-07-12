from figman import MasterGroup, Group, Setting

# WORK [ ]: This has some good potential.
# NOTES: I really like this idea for Lexical Analysis. This allows for 
# different groups to handle different scopes. It allows for an ast to made so 
# easily. This handle AST creation durring lexical analysis. Or at least that 
# is what it seems like to me. Until I do it I won't know for sure how it's 
# going to work out.
class ParsingMasterGroup(MasterGroup):
    """
    This extenson of MasterGroup provides a inteface more aimed at
    the parsing of any text file.
    
        Inherits:
    from MasterGroup:
        def __init__(self, member_id):
        def __str__(self):
        def __repr__(self):
        def __call__(self, search_list: dict | list):
        def __iter__(self):
        def __getitem__(self, name):
        def __setitem__(self, member_id, **settings):
        def member_id(self):
        def member_id(self, member_id):
        def members(self):
        def members(self, new_member):
        def members(self):
        def serialized_state(self):
        def kwargs(self):
        def args(self):
        def add_setting(self, **settings):
        def add_group(self, member_id: str):
        def walk_members(self):
        def remove_member(self, member_id: str) -> bool:
        def to_dict(self)-> dict[str, ]:
        def _search_all_members(self, search_list:str | list, recursed_object = None, temp_path=None):
    """
    scope_operators = {
        "await", 
        ":=",
        "   def",
        "class",
        "@"
        }

class documentation(Group):

    documentation_operators = [

        "#",
        "\"",
        "\"\"\""
    ]

    def __init__(self, member_id, master_group, operator):
        """
        Initialize the documentation.
        
        Params(str): The operator that signals the creation of this instance.
        """

        super().__init__(member_id, master_group)
        self.operator = operator

class expression(Group):

    expression_operators = [
        f"()",
        f"[]",
        f"{{:}}", 
        f"{{}}",
        f"x[]",
        f"x[:]",
        f"x()",
        f"x.attribute"
    ]
    def __init__(self, member_id, master_group, operator):
        """
        Initialize the documentation.

        Params(str): The operator that signals the creation of this instance.
        """

        super().__init__(member_id, master_group)
        self.operator = operator

class documentation(Group):

    def __init__(self, member_id, master_group, operator):
        """
        Initialize the documentation.

        Params(str): The operator that signals the creation of this instance.
        """

        super().__init__(member_id, master_group)

        self.operator = operator

class documentation(Group):

    def __init__(self, member_id, master_group, operator):
        """
        Initialize the documentation.

        Params(str): The operator that signals the creation of this instance.
        """

        super().__init__(member_id, master_group)

        self.operator = operator


class documentation(Group):

    def __init__(self, member_id, master_group, operator):
        """
        Initialize the documentation.
        
        Params(str): The operator that signals the creation of this instance.
        """

        super().__init__(member_id, master_group)

        self.operator = operator

def get_arithmetic_operators():
    """Get arithmetic operator mappings."""

    arithmetic_operators = [
        "<<", 
        ">>", 
        "**", 
        "+x",  
        "-x", 
        "~x", 
        "*", 
        "@", 
        "/", 
        "//", 
        "%", 
        "+", 
        "-" 
    ]
    return arithmetic_operatorsx

def get_boolean_operators():
    """Get boolean operator mappings."""
    
    boolean_operators = [
        "^",
        "&",
        "|",
        "==",
        "!=",
        "<",
        "<=",
        ">",
        ">=",
        "in",
        "not",
        "is",
        "is",
        "not",
        "and",
        "or",
        "if",
        "else" 
    ]
    return boolean_operators

class assignment_operators(operator):
    assignment_operators = [
        "=", 
        "+=",
        "-=",
        "*=",
        "/=",
        "//=",
        "%=",
        "**=",
        "&=",
        "\|=",
        "^=",
        ">>=",
        "<<=",
        ":"
    ]

