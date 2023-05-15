#Class-шаблон для создания обектов
class Car:
    def __init__(self,name,spiid):
#Otribute-эта переменая обекта
        self.name=name
        self.spiid=spiid
        self.ovel=100
#metod-эта функция в класах которую может вызывать обект
    def go(self):
        if self.ovel>=5:
            print("""
            Машина едит в Дурку
            """)
            self.ovel-=5
        else:
            print("""
            Вызывайте Дурку на дам
            """)

#Создали обект(экземпляр класса)
lada=Car("lada",30)