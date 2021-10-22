from ..management.connection import DBConnection
import datetime


class Tatuador(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)

    def insert_tattoo_artist(self, *args):
        '''
        Insert a new Tatto Artist on Postgresql with an Portfolio
        %s -> format to values
        '''
        try:
            sql_tattoo_artist = 'INSERT INTO tatuador (name, email, telefone, address) VALUES (%s, %s, %s, %s)'
            self.execute(sql_tattoo_artist, args) # Execute de insert with datas
            self.commit() # Save additions
            print('Inserted with Success')
        except Exception as e:
            print('Error to Insert', e)

    def delete_tattoo_artist(self):
        '''
        DELETE OPERATION
        '''
        try:
            sql_tattoo_artist = 'INSERT INTO tatuador (name, email, telefone, address) VALUES (%s, %s, %s, %s)'
            self.execute(sql_tattoo_artist, args) # Execute de insert with datas
            self.commit() # Save additions
            print('Inserted with Success')
        except:
            pass

    def read_tattoo_artist(self):
        try:
            pass
        except:
            pass

    def update_tattoo_artist(self):
        try:
            pass
        except:
            pass