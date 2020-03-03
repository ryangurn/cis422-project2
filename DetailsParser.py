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


class DetailsParser:
    def __init__(self, subject: str, crn: str):
        content = requests.get("http://classes.uoregon.edu/pls/prod/hwskdhnt.p_viewdetl?term="+subject+"&crn="+crn)
        parser = Parser.Parser()
        parser.feed(str(content.content))

        self.subject = subject
        self.crn = crn
        self._parser = parser
        self._tables = self._parser.tables
        self._intermediateData = None
        self._dict = {}

    def deleteFormatting(self):
        del self._tables[:3]
        del self._tables[1]
        del self._tables[-3:]
        del self._tables[-3:-1]

        ret_arr = []
        for data in self._tables:
            ret_arr.append(data)

        self._intermediateData = ret_arr

    def parseData(self):
        for key, val in enumerate(self._intermediateData):
            data = self._intermediateData[key]

            if key == 0:
                for k, v in enumerate(data):
                    if k == 2:
                        self._dict.update({
                            "description": data[k][0]
                        })
                    if "Prereqs/Comments" in data[k][0]:
                        self._dict.update({
                            "prereqs": data[k][1].replace('Prereq: ', '')
                        })

            elif key == 1:
                #TODO: add functionality to parse academic deadlines
                pass

            elif key == 2:
                #TODO: add functionality to parse long course description
                pass

    def getPrereqs(self):
        if 'prereqs' in self._dict.keys():
            return self._dict['prereqs']
        else:
            return ''

    def getDescription(self):
        if 'description' in self._dict.keys():
            return self._dict['description']
        else:
            return ''