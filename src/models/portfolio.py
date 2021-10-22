from ..management.connection import DBConnection
from datetime import time


class Portifolio(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)

    def insert_portifolio(self, imagem:list[str], id:int):
        try:
            sql_portfolio = 'INSERT INTO portifolio (images, id_tatuador) VALUES (%s, %s)'
            self.execute(sql_portfolio, (imagem, id)) # create portfolio
            self.commit() # Save additions
            print('Create Portifolio with Success')
        except Exception as e:
            print('Error to Create Portifolio', e)

    def delete_portifolio(self, id:int):
        try:
            sql = f"SELECT * FROM public.portifolio WHERE id_tatuador='{id}'"
            verify = self.query(sql)
            print(verify)
            # verify if the id exists
            if verify[0][0] == id:
                sql_delete = f"DELETE FROM public.portifolio WHERE id_tatuador='{id}'"
                self.execute(sql_delete) # delete data
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