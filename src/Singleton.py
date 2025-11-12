class Singleton(type):

    __instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instancias:
            instancia = super().__call__(*args, **kwargs)
            cls.__instancias[cls] = instancia
        return cls.__instancias[cls]
