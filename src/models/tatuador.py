from ..management.connection import DBConnection

class Tatuador(DBConnection):
    def __init__(self):
        pass


class Portifolio(Tatuador):
    def __init__(self):
        Tatuador.__init__(self)