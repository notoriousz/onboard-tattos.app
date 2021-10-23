from ..management.connection import DBConnection
from datetime import time


class Portifolio(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)

    def insert_portifolio(self, imagem, id:int):
        try:
            SQL_INSERT = 'INSERT INTO portifolio (images, id_tatuador) VALUES (%s, %s)'
            self.execute(SQL_INSERT, (imagem, id)) # create portfolio
            self.commit() # Save additions
            print('Create Portifolio with Success')
        except Exception as e:
            print('Error to Create Portifolio', e)

    def delete_portifolio(self, id:int):
        try:
            SQL_QUERY = f"SELECT * FROM public.portifolio WHERE id_tatuador='{id}'"
            verify = self.query(SQL_QUERY)
            print(verify)
            # verify if the id exists
            if verify[0][0] == id:
                SQL_DELETE = f"DELETE FROM public.portifolio WHERE id_tatuador='{id}'"
                self.execute(SQL_DELETE) # delete data
                self.commit()
                print(f'Deleted portfolio {verify} with Success')
        except Exception as e:
            print('Error to Delete portfolio:', e)

    def insert_images(self):
        try:
            pass
        except:
            pass

    def delete_images(self):
        try:
            pass
        except:
            pass