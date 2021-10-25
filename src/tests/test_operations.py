import pytest
from src.models.portfolio import Portifolio
from ..models.tatuador import Tatuador

class TestINSERT:
    @pytest.mark.parametrize('name,email,telefone,address', [('pytest', 'test@gmail', '99999', 'rua test')])
    def test_insert_tattoo_artist(self, name, email, telefone, address):
        ''' Insert Operation in Tatuador '''
        tattoo_artist = Tatuador()
        tattoo_artist.insert_tattoo_artist(name, email, telefone, address)
        SQL_QUERY = f"SELECT email FROM public.tatuador WHERE name = 'pytest'"
        tattoo_artist.execute(SQL_QUERY)
        fetch = tattoo_artist.cursor.fetchone()
        assert fetch[0] == 'test@gmail'

    @pytest.mark.parametrize('image, id_tatuador', [('pytest.png', 9999)])
    def test_insert_portfolio(self, image, id_tatuador):
        ''' Insert Operation in Portifolio'''
        portfolio = Portifolio()
        portfolio.insert_portifolio(image, id_tatuador)
        SQL_QUERY = "SELECT images FROM portifolio WHERE images = 'pytest.png'"
        portfolio.execute(SQL_QUERY)
        fetch = portfolio.cursor.fetchone()
        assert fetch[0] == 'pytest.png'

    def test_delete_tatuador(self):
        ''' Delete Operation in Tatuador'''
        tattoo_artist = Tatuador()
        SQL_QUERY_ID = f"SELECT id FROM public.tatuador WHERE name = 'pytest'"
        tattoo_artist.execute(SQL_QUERY_ID)
        fetch_id = tattoo_artist.cursor.fetchone()
        tattoo_artist.delete_tattoo_artist(fetch_id[0])
        SQL_QUERY = f"SELECT id FROM public.tatuador WHERE name = 'pytest'"
        tattoo_artist.execute(SQL_QUERY)
        verify = tattoo_artist.cursor.fetchone()
        assert verify == None

    def test_delete_portifolio(self):
        ''' Delete Operation in Portifolio'''
        portfolio = Portifolio()
        portfolio.delete_portifolio(9999)
        SQL_QUERY = f"SELECT images FROM portifolio WHERE id_tatuador=9999"
        portfolio.execute(SQL_QUERY)
        fetch = portfolio.cursor.fetchone()
        assert fetch == None
