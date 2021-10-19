from configparser import ConfigParser
''' 
    We will parse the file database.ini, to get the config of database
    module -> https://docs.python.org/3/library/configparser.html
'''
def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {} # will return the dict with the config
    if parser.has_section(section):
        params = parser.items(section)
        for key, value in params:
            db[key] = value
    else:
        raise Exception(f"Section {section} has no found")
    return db
