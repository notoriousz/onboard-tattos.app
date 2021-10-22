import pytest
from src.models.portfolio import Portifolio
from ..management.connection import DBConnection
from ..models.tatuador import Tatuador

'''
 INSERT tests
'''

class TestINSERT:
    @pytest.mark.parametrize('name,email,telefone,address', [('pytest', 'test@gmail', '99999', 'rua test')])
    def test_insert_tattoo_artist(self, name, email, telefone, address):
        tattoo_artist = Tatuador()
        tattoo_artist.insert_tattoo_artist(name, email, telefone, address)
        connect = DBConnection()
        sql = f"SELECT email FROM public.tatuador WHERE name = 'pytest'"
        connect.execute(sql)
        fetch = connect.cursor.fetchone()
        assert fetch[0] == 'test@gmail'


    @pytest.mark.parametrize('image,id_tatuador', [('pytest.png', 9999)])
    def test_insert_portfolio(self, image, id_tatuador):
        portfolio = Portifolio()
        portfolio.create_portifolio(image, id_tatuador) # create the portfolio test
        connect = DBConnection()
        sql = f"SELECT images FROM public.portifolio WHERE images = 'pytest.png'" # select the portfolio created
        connect.execute(sql)
        fetch = connect.cursor.fetchone()
        assert fetch[0] == 'pytest.png'