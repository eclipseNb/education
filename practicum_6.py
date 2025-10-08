class Engine:
    def __init__(self, hp, fuel_type):
        """Мощность двигателя и тип топлива"""
        self.hp = hp
        self.fuel_type = fuel_type

    def __str__(self):
        return f"\nМощность: {self.hp} л.с. \nТопливо: {self.fuel_type}"


class CarBody:
    def __init__(self, car_type, doors):
        """Кузов автомобиля, количество дверей"""
        self.type = car_type
        self.doors = doors

    def __str__(self):
        return f"Тип кузова: {self.type} \nДверей: {self.doors}"


class Wheel:
    def __init__(self, diameter, type_wheel):
        """Диаметр колёс и тип шин"""
        self.diameter = diameter
        self.type_wheel = type_wheel

    def __str__(self):
        return f"Диски: {self.diameter} дюйма(ов) \nТип резины: {self.type_wheel}"


class Car:
    def __init__(self, title, engine, body, wheel):
        """Авто целиком, со всеми компонентами"""
        self.title = title
        self.engine = engine
        self.body = body
        self.wheel = wheel

    def __str__(self):
        return f"\n\033[1m\033[4m{self.title}\033[0m{self.engine}\n{self.body}\n{self.wheel}"

if __name__ == '__main__':

    mustang = Car(title='Ford Mustang, 2016',
                  engine=Engine(hp=300, fuel_type='бензин'),
                  body=CarBody('седан', 2),
                  wheel=Wheel(18, 'летняя')
                  )

    hilux = Car(title='Hilux Surf, 2002',
                engine=Engine(hp=200, fuel_type='дизель'),
                body=CarBody('SUV', 4),
                wheel=Wheel(22, 'шипованная')
                )

    print(mustang)
    print(hilux)


