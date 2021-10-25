import pytest
from src.models.portfolio import Portifolio
from ..models.tatuador import Tatuador

class TestUpdate:
    
    @pytest.mark.parametrize('id', [(171)])
    def test_update_tatoo_artist(self, id):
        '''
        If you want test with another ID, change in parametrize
        '''
        tattoo_artist = Tatuador()
        SQL_QUERY_ID = f"SELECT name, email, telefone, address FROM public.tatuador WHERE id = {id} ;"
        tattoo_artist.update_tattoo_artist(id, 'PytestUpdate', '@pytest', '999999test', 'rua test')
        new_values = tattoo_artist.query(SQL_QUERY_ID)
        assert new_values[0] == ('PytestUpdate', '@pytest', '999999test', 'rua test')