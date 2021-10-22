from ..management.connection import DBConnection



class Portifolio(DBConnection):
    def __init__(self):
        DBConnection.__init__(self)

    def create_portifolio(self, imagem, id):
        try:
            sql_portfolio = 'INSERT INTO portifolio (images, id_tatuador) VALUES (%s, %s)'
            self.execute(sql_portfolio, (imagem, id)) # create portfolio
            self.commit() # Save additions
            print('Create Portifolio with Success')
        except Exception as e:
            print('Error to Create Portifolio', e)


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
