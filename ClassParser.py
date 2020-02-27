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


class ClassParser:
    def __init__(self, parser: Parser):
        """
        Initializer for the class parser. This will allow a parser to be
        specified that will generate a set of tables in the form of lists
        of lists

        :param parser:

        Example Usage:
        p = Parser.Parser()
        parser = ClassParser.Parser(p)
        """
        self._parser = parser
        self._tables = parser.tables
        self._intermediateData = []
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
        del self._tables[:3]  # strip some of the formatting nonsense
        del self._tables[-3:]  # strip some js and empty rows (formatting nonsense)

        # copy data for move to _intermediateData
        ret_arr = []
        for data in self._tables:
            ret_arr.append(data)

        del ret_arr[0][0]
        for key, val in enumerate(ret_arr):
            # skip the zero-th item
            if key != 0:
                # removes headers from the start of each table
                del ret_arr[key][0:3]
                for ret_arr_key, ret_arr_val, in enumerate(ret_arr[key]):
                    if len(ret_arr[key][ret_arr_key]) == 1:
                        del ret_arr[key][ret_arr_key]  # delete empty lists at the end of each row
            elif key == 0:
                # replace some bad formatting
                ret_arr[0][0][0] = ret_arr[0][0][0].replace("Classes Found   ", "", 1)

        del ret_arr[-1]  # removing the number of classes found
        for k, v in enumerate(ret_arr):
            if len(ret_arr[k]) == 1:
                del ret_arr[k]

        self._intermediateData = ret_arr

    def parseData(self, parser: Parser):
        pass
