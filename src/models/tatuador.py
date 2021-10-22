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
            sql_insert = 'INSERT INTO tatuador (name, email, telefone, address) VALUES (%s, %s, %s, %s)'
            self.execute(sql_insert, args) # Execute de insert with datas
            self.commit() # Save additions
            print('Tattoo artist inserted with Success')
        except Exception as e:
            print('Error to Insert tattoo artist', e)

    def delete_tattoo_artist(self, id:int):
        '''
        DELETE OPERATION
        '''
        try:
            sql = f"SELECT * FROM public.tatuador WHERE id='{id}'"
            verify = self.query(sql)
            # verify if the id exists
            if verify[0][0] == id:
                sql_delete = f"DELETE FROM public.tatuador WHERE id='{id}'"
                self.execute(sql_delete) # delete data
                self.commit()
                print(f'Deleted tattoo artist {verify} with Success')
        except Exception as e:
            print('Error to delete tattoo artist:', e)


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