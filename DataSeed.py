"""
DataSeed.py is the program that will seed the database and complete all of the
parsing that needs to be handled before hand. It will setup all of the classes
based on the classes.uoregon.edu dataset.

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Priority credit to:
Ryan Gurnick - 3/4/20  Creation

"""
import os

import ClassParser
import Datastore

DB = 'seed.db'

if not os.path.exists('seed.db'):
    # setup datastore
    ds = Datastore.DB(DB)
    # generate them default tables
    ds.generateTables()

# all of the subject codes
subject_codes = ["AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ANTM", "ARB", "ARCH", "ARH", "ART", "ARTC",
                 "ARTD", "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BI", "BIKC",
                 "BIOE", "BLST", "CARC", "CAS", "CDS", "CFT", "CH", "CHKC", "CHN", "CHNF", "CINE", "CIS", "CIT", "CLAS",
                 "COLT", "CPSY", "CRDG", "CRES", "CRWR", "CSCH", "DAN", "DANC", "DANE", "DIST", "DSGN", "EALL", "EC",
                 "ECE", "EDLD", "EDST", "EDUC", "ENG", "ENVS", "ERTH", "ES", "ESC", "EURO", "FHS", "FIN", "FINN", "FLR",
                 "FR", "GEOG", "GEOL", "GER", "GRK", "GRST", "GSAE", "GSCL", "GSGE", "GSST", "HBRW", "HC", "HIST",
                 "HPHY", "HUM", "IARC", "ICH", "INTL", "IST", "ITAL", "J", "JDST", "JGS", "JPN", "KC", "KRN", "LA",
                 "LAS", "LAT", "LAW", "LEAD", "LERC", "LIB", "LING", "LT", "MATH", "MDVL", "MENA", "MGMT", "MIL",
                 "MKTG", "MUE", "MUJ", "MUP", "MUS", "NAS", "NORW", "OBA", "OIMB", "OLIS", "PD", "PDX", "PE", "PEAQ",
                 "PEAS", "PEC", "PEF", "PEI", "PEIA", "PEL", "PEMA", "PEMB", "PEO", "PERS", "PERU", "PETS", "PEW",
                 "PHIL", "PHKC", "PHYS", "PORT", "PPPM", "PREV", "PS", "PSY", "QST", "REES", "REL", "RL", "RUSS",
                 "SBUS", "SCAN", "SCYP", "SERV", "SLP", "SOC", "SPAN", "SPD", "SPED", "SPM", "SPSY", "SWAH", "SWED",
                 "TA", "TLC", "UGST", "WGS", "WR"]

# tri loop
for k, s in enumerate(subject_codes):  # for each subject
    for y in range(2015, 2020):  # for each year
        for i in range(1, 5):  # for each term
            print("(S:{} - {}/{:.2%}) STARTING PARSE FOR {} {} - [{}]".format(k, len(subject_codes),
                                                                              k / len(subject_codes), y, i, s))

            # parse the data and store it.
            p = ClassParser.ClassParser(str(y) + "0" + str(i), s, DB)
            p.deleteFormatting()
            p.parseData()

            print(
                "(S:{} - {}/{:.2%}) ENDING PARSE FOR {} {} - [{}]".format(k, len(subject_codes), k / len(subject_codes),
                                                                          y, i, s))
