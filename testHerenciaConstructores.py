from futbolista import Futbolista
from deportista import Deportista
from persona import Persona

def testFutbolista():
    futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
    ok = False
    if (futbolista.getNombre() == "Juan Pablo" and futbolista.getEdad() == 30 and futbolista.getAltura()=="1,80" and futbolista.getSexo() == "M" and futbolista.getAñosPracticando() == 12 and futbolista.getGolesMarcados()==400 and futbolista.getTarjetasRojas() == 1 and futbolista.getPiernaHabil() == "Derecha"):
        ok = True
    assert(ok)


def testToString():
    futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
    ok = False
    if (futbolista.__str__() == "Mi nombre es Juan Pablo soy profesional en el deporte Futbol Tengo 30 años de edad y llevo 12 años en el deporte"):
        ok = True
    assert(ok)

def testHerencia():
    futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
    ok = False
    if (isinstance(futbolista, Deportista) and isinstance(futbolista, Persona)):
        ok = True
    assert(ok)
