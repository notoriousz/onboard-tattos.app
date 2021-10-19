import psycopg2 as database
from .db_config import config

class DBConnection:
    ''' PostgreSQL database connection '''
    def __init__(self):
        self.__params = config() # Get the file database.ini with de pairs key-value with configuration
        try:
            self.__conn = database.connect(**self.__params) # connection to database
            self.__cur = self.__conn.cursor()
            print('##### Connected #####\n')
        except(Exception, database.DatabaseError) as error:
            print(error)

    # these specials methods, allows we use the WITH instruction as context manager
    def __enter__(self):
        ''' return the database connection '''
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' close the database connection  '''
        self.commit()
        self.connection.close()       

    @property
    def connection(self):
        ''' Property to manipulate connection '''
        return self.__conn

    @property
    def cursor(self):
        ''' Property to manipulate cursor '''
        return self.__cur

    def execute(self, sql, params=None):
        '''
        execute SQL commands with params but no return nothing
        the execute instruction necessite a SQL command with params or a empty tuple
        '''
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        '''
        execute the SQL commands but return the query
        the execute instruction necessite a SQL command with params or a empty tuple
        '''
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def commit(self):
        ''' add the changes '''
        return self.connection.commit()

    def fetchall(self):
        ''' return registrys with SQL instruction '''
        return self.cursor.fetchall()