from ..management.connection import DBConnection
from datetime import time

class Tatuador(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)

    def insert_tattoo_artist(self, *args:str):
        '''
        Insert a new Tatto Artist on Postgresql with an Portfolio
        %s -> format to values
        '''
        try:
            SQL_INSERT = 'INSERT INTO tatuador (name, email, telefone, address) VALUES (%s, %s, %s, %s)'
            self.execute(SQL_INSERT, args) # Execute de insert with datas
            self.commit() # Save additions
            print('Tattoo artist inserted with Success')
        except Exception as e:
            print('Error to Insert tattoo artist', e)

    def delete_tattoo_artist(self, id:int):
        '''
        DELETE OPERATION
        '''
        try:
            SQL_DELETE = f"DELETE FROM public.tatuador WHERE id='{id}'"
            self.execute(SQL_DELETE) # delete data
            self.commit()
            print(f'Deleted tattoo artist id:{id} with Success')
        except Exception as e:
            print('Error to delete tattoo artist:', e)



    def read_tattoo_artist(self):
        try:
            SQL_QUERY = ''
        except Exception as e:
            print('Error to read tattoo artist:', e)



    def update_tattoo_artist(self):
        try:
            pass
        except:
            pass