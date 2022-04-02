from __future__ import annotations
from abc import ABC, abstractmethod


class Details(ABC):
    """Абстрактный класс деталей."""

    @abstractmethod
    def creation(self):
        pass

# Конкретный продукт
class Engine(Details):

    def creation(self):
        return 'Создан двигатель'

# Конкретный продукт
class FuelCans(Details):

    def creation(self):
        return 'Создан топливный отсек'

# Конкретный продукт
class Equipment(Details):

    def creation(self):
        return 'Создана аппаратура'

# Абстрактная фабрика
class DetailsFactory(ABC):
    """Абстрактная фабрика деталей."""

    @abstractmethod
    def create_detail(self):
        """Создание абстрактного продукта."""
        pass

# Конеретная фабрика
class EngineFactory(DetailsFactory):
    """Конкретная фабрика двигателей."""

    def create_detail(self):
        return Engine()

# Конеретная фабрика
class FuelCansFactory(DetailsFactory):
    """Конкретная фабрика игрового топливных баков."""

    def create_detail(self):
        return FuelCans()

# Конеретная фабрика
class EquipmentFactory(DetailsFactory):
    """Конкретная фабрика оборудования."""

    def create_detail(self):
        return Equipment()


class RocketCreator(ABC):
    """Метод в котором определяются методы, которыми будет владеть каждая ракета"""

    @abstractmethod
    def factory_method(self):
        pass

    def assembly(self):
        pass

    def transfer(self):
        pass


class RocketForMoon(RocketCreator):
    def __init__(self, ):
        self.EngineFactory = EngineFactory.create_detail
        self.FuelCansFactory = FuelCansFactory.create_detail
        self.EquipmentFactory = EquipmentFactory.create_detail
        pass
