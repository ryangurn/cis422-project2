"""
DetailsParser.py this is the file that allows us to quickly query the data source:
classes.uoregon.edu specifically the detailed view for any specific subject and crn
combination

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Priority credit to:
Ryan Gurnick - 2/27/20  Creation

"""
import Parser
import requests


class RequirementsParser:
    def __init__(self, crn, subject):
        content = requests.get("http://classes.uoregon.edu/pls/prod/hwskdhnt.p_viewdetl?term="+subject+"&crn="+crn)
        parser = Parser.Parser()
        parser.feed(str(content.content))

        self.subject = subject
        self.crn = crn
        self._parser = parser
        self._tables = self._parser.tables

    def deleteFormatting(self):
        pass

    def parseData(self):
        pass