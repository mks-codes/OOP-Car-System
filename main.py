from abc import ABC, abstractmethod

class License(ABC):

    @abstractmethod
    def security(self):
        pass
    
class Customer(License):
    def __init__(self,name,id):
        self.__name = name
        self.id = id

    def security(self):
        return f"Customer {self.__name} (ID: {self.id}) is verified with license."
class Car:
    def __init__(self,model,brand):
        self._model = model
        self._brand = brand
    
    def Logo(self):
        return 'Marcedise Benze'

    
class SportCar(Car):
    def __init__(self, model, brand,hoursepower):
        super().__init__(model, brand)
        self.hoursepower = hoursepower

    def show_detials(self):
        return f"{self._brand} {self._model} with {self.hoursepower} HP"


    
cus = Customer('mks',2)
print(cus.security())

sp = SportCar("Gt","Mercedes-Benz", 200)
print(sp.show_detials())
print(sp.Logo())

