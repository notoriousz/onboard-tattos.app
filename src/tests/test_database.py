import pytest
import os
from ..management.connection import DBConnection

class TestDB:
    def connection(self):
        db = DBConnection()
        try:
            db.execute("SELECT VERSION()")
            result = db.cursor.fetchone()
            if result:
                return True
        except (Exception, db.DatabaseError) as error:
            return False

    def test_database_isready(self):
        ''' 
        Verified, if the postgre is ready to connect
        https://www.postgresql.org/docs/9.3/app-pg-isready.html
         ''' 
        os.system('pg_isready -d onboard -h localhost -p 5432')
        status = os.system('echo $?')
        assert status == 0

    def test_database_conn(self):
        ''' 
        Execute a SQL command, if return True, we are connected
        '''
        assert self.connection() == True