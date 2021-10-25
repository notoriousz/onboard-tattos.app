from abc import abstractclassmethod
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
            return 'Tattoo artist inserted with Success'
        except Exception as e:
            print('Error to Insert tattoo artist', e)

    def delete_tattoo_artist(self, id:int):
        '''
        Delete an Tattoo Artist from Postgres
        '''
        try:
            SQL_DELETE = f"DELETE FROM public.tatuador WHERE id='{id}'"
            self.execute(SQL_DELETE) # delete data
            self.commit()
            return f'Deleted tattoo artist id:{id} with Success'
        except Exception as e:
            print('Error to delete tattoo artist:', e)

    def read_tattoo_artist(self, id:int=None):
        '''
        Read an Tatto Artist from Postgres
        '''
        if id is None:
            try:
                SQL_QUERY = 'SELECT * FROM public.tatuador'
                self.execute(SQL_QUERY)
                return self.fetchall()
            except Exception as e:
                print('Error to read tattoo artist:', e)
        else:
            try:
                SQL_QUERY = f'SELECT * FROM public.tatuador WHERE id={id}'
                self.execute(SQL_QUERY)
                return self.fetchall()
            except Exception as e:
                print('Error to read tattoo artist:', e)

    def update_tattoo_artist(self, id, *args):
        try:
            SQL_UPDATE = f'UPDATE public.tatuador SET name = %s, email = %s, telefone = %s, address = %s WHERE id = {id}'
            self.execute(SQL_UPDATE, args)
            self.commit()
            return 'Update with success'
        except Exception as e:
           print(f'Error to update:', e)