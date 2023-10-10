from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        return print("Um animal vai fazer algum som")


class Cao(Animal):
    def __init__(self):
        pass

    def falar(self):
        print("AU-AU !!!")


class Gato(Animal):
    def __init__(self):
        pass

    def falar(self):
        print("MIAU-MIAU !!!")


class Papagaio(Animal):
    def __init__(self):
        pass

    def falar(self):
        print("CURUPACO-PACO !!!")


cao = Cao()
cao.falar()

gato = Gato()
gato.falar()

papagaio = Papagaio()
papagaio.falar()
