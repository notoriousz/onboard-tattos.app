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
            sql_tattoo_artist = 'INSERT INTO tatuador (name, email, telefone, endereco) VALUES (%s, %s, %s, %s)'
            self.execute(sql_tattoo_artist, args) # Execute de insert with datas
            self.commit() # Save additions
            print('Insert Success')
        except Exception as e:
            print('Error to Insert', e)


    def delete_tattoo_artist(self):
        try:
            pass
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


class Portifolio(Tatuador):
    def __init__(self):
        Tatuador.__init__(self)

    def create_portifolio(self, imagem1):
        with open(imagem1, "rb") as image:
            read_img = image.read()
            bytea = bytearray(read_img)
            store_img = [f'{bytea[0]}']

        try:
            sql_portfolio = 'INSERT INTO portifolio (imagens) VALUES (%s)'
            self.execute(sql_portfolio, store_img) # create portfolio
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
