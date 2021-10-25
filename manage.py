from src.models.tatuador import Tatuador
from src.models.portfolio import Portifolio

def main():
    portifolio_model = Portifolio()
    tattoo_artist_model = Tatuador()

    # tattoo_artist_model.insert_tattoo_artist('Lucas', 'meugmail1@gmail.com', '11 998023311', 'Rua Test')
    # tattoo_artist_model.insert_tattoo_artist('Caio', 'meugmail2@gmail.com', '11 998023322', 'Rua Test')
    # tattoo_artist_model.insert_tattoo_artist('Luiza', 'meugmail3@gmail.com', '11 998023333', 'Rua Test')
    # tattoo_artist_model.insert_tattoo_artist('Carvalho', 'meugmail4@gmail.com', '11 998023344', 'Rua Test')
    # tattoo_artist_model.insert_tattoo_artist('Juninho', 'meugmail5@gmail.com', '11 998023355', 'Rua Test')

    # portifolio_model.insert_portifolio('Lucas.png', 227)
    # portifolio_model.insert_portifolio('Caio.png', 228)
    # portifolio_model.insert_portifolio('Luiza.png', 229)
    # portifolio_model.insert_portifolio('Carvalho.png', 230)
    # portifolio_model.insert_portifolio('Juninho.png', 231)

    print(portifolio_model.read_portifolio(), sep='')
    print(tattoo_artist_model.read_tattoo_artist())

if __name__ == '__main__':
    '''
    The tables were created manually in postgres CLI.
    The tables.sql file contains the code to check
    '''
    main()







