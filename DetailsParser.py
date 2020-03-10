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
import urllib.request

import Parser


class DetailsParser:
    def __init__(self, subject: str, crn: str):
        """
        Initializer for the class parser. This will allow a parser to be
        specified that will generate a set of tables in the form of lists
        of lists

        Example Usage:
        parser = DetailsParser.DetailsParser("CIS", "12332")
        """
        content = "http://classes.uoregon.edu/pls/prod/hwskdhnt.p_viewdetl?term="+subject+"&crn="+crn
        with urllib.request.urlopen(content) as response:
            html = response.read()

        parser = Parser.Parser()
        parser.feed(str(html))

        self.subject = subject
        self.crn = crn
        self._parser = parser
        self._tables = self._parser.tables
        self._intermediateData = None
        self._dict = {}

    def deleteFormatting(self):
        """
        deleteFormatting is here to remove the formatting from the
        table design that is provided by classes.uoregon.edu

        This will remove headers from each course subsection
        This will remove the amount of results from the bottom
        This will remove many empty arrays that are to denote formatting

        This will NOT remove empty arrays or empty strings that denote
        empty fields such as Instructor or Location that are not provided
        for some unknown reason.

        :return:

        Example Usage:
        (Continuation of the __init__ example)

        parser.deleteFormatting()
        """
        del self._tables[:3]
        del self._tables[1]
        del self._tables[-3:]
        del self._tables[-3:-1]

        ret_arr = []
        for data in self._tables:
            ret_arr.append(data)

        self._intermediateData = ret_arr

    def parseData(self):
        """
        This function will take the intermediateData produced after calling the deleteFormatting and
        get it into a usable object.
        :return:
        """
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
                pass

            elif key == 2:
                pass

    def getPrereqs(self):
        """
        This function will return just the prerequisites stored
        :return:
        """
        if 'prereqs' in self._dict.keys():
            return self._dict['prereqs']
        else:
            return ''

    def getDescription(self):
        """
        This function will return just the description stored
        :return:
        """
        if 'description' in self._dict.keys():
            return self._dict['description']
        else:
            return ''
