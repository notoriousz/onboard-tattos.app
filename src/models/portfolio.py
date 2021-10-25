from ..management.connection import DBConnection
from datetime import datetime

class Portifolio(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)

    def insert_portifolio(self, imagem, id:int):
        ''' Operation to create a portifolio from especific tattoo artist '''
        try:
            SQL_INSERT = 'INSERT INTO portifolio (images, id_tatuador) VALUES (%s, %s)'
            self.execute(SQL_INSERT, (imagem, id)) # create portfolio
            self.commit() # Save additions
            return 'Create Portifolio with Success'
        except Exception as e:
            print('Error to Create Portifolio', e)

    def delete_portifolio(self, id:int):
        ''' Operation to delete a portfolio with ID '''
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

    def read_portifolio(self, id:int=None):
        ''' Read a Portfolio specific if pass the ID, or return all'''
        if id is None:
            try:
                SQL_QUERY = 'SELECT * FROM public.portifolio'
                self.execute(SQL_QUERY)
                return self.fetchall()
            except Exception as e:
                print('Error to read portfolio:', e)
        else:
            try:
                SQL_QUERY = f'SELECT * FROM public.portifolio WHERE id_tatuador={id}'
                self.execute(SQL_QUERY)
                return self.fetchall()
            except Exception as e:
                print('Error to read portfolio:', e)

    def insert_images(self, id, images=str):
        ''' The string contains all links to images '''
        try:
            SQL_INSERT = f"UPDATE portifolio SET images = '{images}' WHERE id_tatuador = {id}"
            self.execute(SQL_INSERT, images)
            current_date = datetime.today()
            actual = current_date.strftime('%A, %B %d, %Y %H:%M:%S')
            update_at_sql = f"UPDATE portifolio SET update_at = '{actual}' WHERE id_tatuador = {id}"
            self.execute(update_at_sql)
            self.commit()
            return 'Images add with success'
        except Exception as e:
            print('Error to add images:', e)

    def clean_images(self, id):
        try:
            SQL_CLEAN = f"UPDATE portifolio SET images = '{None}' WHERE id_tatuador = {id}"
            # delete images
            self.execute(SQL_CLEAN)
            self.update_at(id)
            self.commit()
            return 'Images deleted with success'
        except Exception as e:
            print('Error to delete images:', e)

    def update_at(self, id):
        current_date = datetime.today()
        actual = current_date.strftime('%A, %B %d, %Y %H:%M:%S')
        update_at_sql = f"UPDATE portifolio SET update_at = '{actual}' WHERE id_tatuador = {id}"
        self.execute(update_at_sql)