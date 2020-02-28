"""
ClassParser.py this is the file that allows us to quickly query the data source:
classes.uoregon.edu

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Priority credit to:
Ryan Gurnick - 2/25/20  Creation

"""
import Parser
import requests


class RequirementsParser:
    def __init__(self):
        content = requests.get("http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/#degreeplantext")
        parser = Parser.Parser()
        parser.feed(str(content.content))

        self._parser = parser
        self._tables = self._parser.tables

    def deleteFormatting(self):
        pass

    def parseData(self):
        pass