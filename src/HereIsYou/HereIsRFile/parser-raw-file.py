

class DubsParser:
    """DubsParser, an attempt at language agnostic parsing."""
    
    def __init__(self, language):

        # WORK [ ]: Parse objects first.
        # NOTES: This allows me to build reusable branches from classes and 
        # functions, since expressions could make multiple instances.
        # NOTES: Also going to need to track immutables across calls. To see 
        # all of this. Fuck this is going to be a toughy. I'll need
        # NOTES: This will be cool to see where they match up. If I build this 
        # out and see that self.listof should exist here here and here,
        # NOTES: but somehow a copy got made or whatever, yeah i'm excited aout 
        # the understanding i'm going to gain from this.

    def _parse_expression(self, pyscript):
        """
        Parse a Dub script and return an abstract syntax tree (AST).

        Params:
            pyscript (str): The path to the Dub script to parse.
        Returns:
            The AST representing the parsed Dub script.
        """

        for line in self._load_file(pyscript):
            operator_map = self._get_operators(line)
            print(operator_map)

    def _load_file(self, pyscript):
        """
        Load a Dub script from a file and yield its lines.
        
        Params:
            pyscript (str): The path to the Dub script to load.
        Yields:
            str: Each line of the Dub script.
        """

        # For now, this method will just yield the lines of the Dub script as strings.
        with open(pyscript, "r") as f:
            yield from f.readlines()

    def _define_ast(self, lvalue, rhs):
        """
        Define the abstract syntax tree (AST) for the Dub programming language.
        
        This method will be used to define the structure of the AST that will be used to represent parsed Dub scripts.
        """

        #NOTES: You don't fucker, you grab it all in one go, put it together later. Makes it quick and easy. No problems. then you have anothter master class. you put those in. why do i do this though. hmm. This is correct.
        #NOTES: if I have everything in seperate master classes, allow adding, them together, I can easily plug and play execution. Just add them together in the correct order. I think. Prebuild all classes, functions blah blah, load them from file on start. Collapse into a dict when not using keep "hot paths" alive in memory or something like that.
        #NOTES: This lets me execute from mapping, quick shit. Maybe I don't I haven't actually tried this, it makes sense though to me. I will even add a to binary method for executing straigh in CPU. It would need a lot of validation and shit though. All of this is who knows
        #self.ast[lvalue]
        pass
        
    def _provide_chars(self, line):
        """
        Provide each character in a line of code along with its index.
        
        Params:
            line (str): The line of code to provide characters from.
        Yields:
            tuple: A tuple containing the character and its index.
        """

        for index, char in enumerate(line):
            yield char, index

    def _get_operators(self, line):
        """
        Get the indices of the assignment operator and arithmetic operators in a line of code.
        
        Params:
            line (str): The line of code to get operators from.
        Returns:
            tuple: A tuple containing the index of the assignment operator and a list of indices of arithmetic operators.
        """
        for index, char in self._provide_chars(line):
            try:
                self.operating_mapping[char]
    
if __name__ == "__main__":
    dub_parser = DubParser()
    dub_parser._parse_expression("/home/donald-reilly/Documents/Unstable/dub/scripts/test_script.dub")