# Ramon Ramiro Soo Rincón
# 1215100917
# Singleton
# GITI9072
# Tecnologías de la Información y la Comunicación
class Borng:
    _shared_state = {}  # Attribute dictonary

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictonary


class Singleton(Borng):
    def __init__(self, **kwargs):
        Borng.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP="Hyper Text Trnasfer Protocol")
print(x)

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
