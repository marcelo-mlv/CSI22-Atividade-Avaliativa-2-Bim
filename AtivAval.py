#Atividade avaliativa 2 bimestre
#Alunos: Lean Kaique Cardoso de Souza e Marcelo  Loiola Lopes Vera
#Professora: Karla Donato Fook

#Componente
class SaborPizza:
    def getDescription (self):
        return self.__class__.__name__
    def getTotalCost (self):
        return self.__class__.cost
#Componente concreto
class Pizza(SaborPizza):
    cost = 56
#Decorador
class Decorator(SaborPizza):
    def __init__(self, saborPizza):
        self.sabor = saborPizza

    def getTotalCost(self):
        return self.sabor.getTotalCost() + SaborPizza.getTotalCost(self)
    
    def getDescription(self):
        return self.sabor.getDescription() + ' ' + SaborPizza.getDescription(self)
#Decorador concreto
class Gorgonzola (Decorator):
        cost = 15
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Calabresa (Decorator):
        cost = 10
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Pepperoni (Decorator):
        cost = 12
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Mussarela (Decorator):
        cost = 5
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)
    
class Ovo (Decorator):
        cost = 5
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Frango (Decorator):
        cost = 20
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Catupiry (Decorator):
        cost = 15
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Parmesão (Decorator):
        cost = 15
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Rúcula (Decorator):
        cost = 25
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class MolhoDeTomate (Decorator):
        cost = 5
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Azeitona (Decorator):
        cost = 5
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Alho (Decorator):
        cost = 5
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Orégano (Decorator):
        cost = 2
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Palmito (Decorator):
        cost = 15
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Bacon (Decorator):
        cost = 16
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Chocolate (Decorator):
        cost = 40
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)


class DoceDeLeite (Decorator):
        cost = 40
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Brownie (Decorator):
        cost = 30
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Morango (Decorator):
        cost = 25
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class Coco (Decorator):
        cost = 25
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)

class MM (Decorator):
        cost = 25
        def __ini__(self, saborPizza):
            Decorator.__init__(self, saborPizza)


#Exemplos de pedidos
pizza1 = Calabresa(Pepperoni(MolhoDeTomate(Pizza())))
print (pizza1.getDescription() + ": R$" + str(pizza1.getTotalCost()))
pizza2 = Frango(Gorgonzola(Pepperoni(MolhoDeTomate(Pizza()))))
print (pizza2.getDescription() + ": R$" + str(pizza2.getTotalCost()))
pizza3 = Mussarela(Bacon(MolhoDeTomate(Alho(Pizza()))))
print (pizza3.getDescription() + ": R$" + str(pizza3.getTotalCost()))
pizza4 = Chocolate(Morango(MM(Pizza())))
print (pizza4.getDescription() + ": R$" + str(pizza4.getTotalCost()))