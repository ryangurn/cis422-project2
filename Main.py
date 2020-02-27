"""
Main.py is the first file that will be run when the program starts being run
This will start the running of all other subroutines for graphics, parsing,
processing.

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
import requests
import Parser
import ClassParser

# change classes.uoregon.edu variables
term = "201903"
subject = "CIS"
cis_catalog_url = "http://classes.uoregon.edu/pls/prod/hwskdhnt.P_ListCrse?term_in="+term+"&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&sel_subj="+subject+"&sel_crse=&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&submit_btn=Show+Classes"
catalog = requests.get(cis_catalog_url)

# initialize the html table parser
parser = Parser.Parser()
parser.feed(str(catalog.content))

# call ClassParser
p = ClassParser.ClassParser(parser)
p.deleteFormatting()
print(p._intermediateData)
print(p._dict)
p.parseData(parser)