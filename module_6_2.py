# Vehicle - это любой транспорт
class Vehicle:
    # Атрибут класса с допустимыми цветами
    __COLOR_VARIANTS = ['Red', 'Black', 'White', 'Blue', 'Green', 'Yellow']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner  # Владелец
        self.__model = model  # Модель
        self.__engine_power = engine_power  # Мощность двигателя
        # Проверка на допустимость цвета
        if color.capitalize() in Vehicle.__COLOR_VARIANTS:
            self.__color = color.capitalize()  # Цвет
        else:
            raise ValueError(f"Цвет '{color}' не допустим!")

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if new_color.capitalize() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color.capitalize()
        else:
            print(f"Нельзя сменить цвет на '{new_color}'")

    def about(self) -> None:
        print("Информация о транспортном средстве:")
        self.print_info()


# Sedan - наследник класса Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Пассажиров в седане

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)  # Вызов конструктора родительского класса

    def about(self) -> None:
        print("Информация о седане:")
        super().about()  # Вызов метода about из родительского класса


# Создание экземпляра класса Sedan
vehicle1 = Sedan('Борис А.М.', 'Toyota Mark II', 280, 'Blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства, вызывая методы
vehicle1.set_color('Pink')  # Цвет не допустимый
vehicle1.set_color('Black')  # Цвет допустимый
vehicle1.owner = 'Георгий М.В.'  # Меняем владельца

# Проверяем что поменялось
vehicle1.print_info()
