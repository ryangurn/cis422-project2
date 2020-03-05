import os
import Datastore
import ClassParser

DB = 'seed.db'

if not os.path.exists('seed.db'):
    # setup datastore
    ds = Datastore.DB(DB)
    ds.generateTables()

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

for k, s in enumerate(subject_codes):
    for y in range(2015, 2020):
        for i in range(1, 5):
            print("(S:{}/{}) STARTING PARSE FOR {} {} - [{}]".format(k, k/len(subject_codes), y, i, s))

            p = ClassParser.ClassParser(str(y)+"0"+str(i), s, DB)
            p.deleteFormatting()
            p.parseData()

            print("(S:{}/{}) ENDING PARSE FOR {} {} - [{}]".format(k, k/len(subject_codes), y, i, s))

