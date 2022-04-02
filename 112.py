import itertools
from typing import Iterable, Dict, Optional, List, Any


class NoProductionError(Exception):
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)



def get_conveyor(item: Dict) -> Optional[int]:
    return item.get("конвейер")


def calculate(mydict: Iterable) -> List:
    # группируем исходные данные по конвейерам
    print(mydict)
    conveyor_resource = itertools.groupby(mydict, get_conveyor)
    print(conveyor_resource)
    dough = None
    other_resources = list()
    overall_instruction = list() # запишем сюда все инструкции
    conveyor_manager = dict() # для того чтобы распределять ресурсы на разных конвейерах и избежать пересечений
    for key, group in conveyor_resource:
        if not conveyor_manager.get(key):
            conveyor_manager[key] = dict()
            conveyor_manager[key]["начинки"] = list()
        for resource in group:
            if resource.get("ингридиент") == "тесто": # тесто - базовый ресурс, работаем с ним отдельно
                conveyor_manager[key]["тесто"] = resource
            else:
                conveyor_manager[key]["начинки"].append(resource) # начинки - в отдельный список, для упорядочивания


    for key, item in conveyor_manager.items():
        dough = item.get("тесто")
        other_resources = item.get("начинки")
        other_resources = sorted(other_resources, key=lambda item: item.get('порция')) # сортируем начинки по порциям
        max_cakes_available = int(dough.get("количество") // dough.get("порция")) # выясняем сколько возможно кексиков
        for other_resource in other_resources:

            # Выясняем сколько раз можем использовать эту начинку
            portions_avail = int(other_resource.get("количество") // other_resource.get("порция"))

            # Предусматриваем вариант, что использований начинок может быть больше, чем оставшегося теста
            portions_with_rest_of_dough = min((max_cakes_available, portions_avail))

            # Пополняем инструкции для производства новыми инструкциями изготовления кексиков
            for _ in range(portions_with_rest_of_dough):
                overall_instruction.append(
                    {
                        dough.get("ингридиент"): dough.get("порция"),
                        other_resource.get("ингридиент"): other_resource.get("порция"),
                        "конвейер": key
                    }
                )
            # вычитаем из возможного количества порций. тесто уже использовано.
            max_cakes_available -= portions_with_rest_of_dough

    # если не удалось составить ни одной инструкции - говорим что ресурсы распределены неверно
    if overall_instruction == []:
        raise NoProductionError("no production")


    return overall_instruction

print(calculate([
    {
        "ингридиент" : "тесто",
        "количество" : 10,
        "конвейер" : 1,
        "порция" : 2,
    },
    {
        "ингридиент" : "тесто",
        "количество" : 10,
        "конвейер" : 2,
        "порция" : 2,
    },
    {
        "ингридиент" : "изюм",
        "количество" : 2,
        "конвейер" : 1,
        "порция" : 1,
    },
    {
        "ингридиент" : "изюм",
        "количество" : 2,
        "конвейер" : 2,
        "порция" : 1,
    },
    {
        "ингридиент" : "шоколад",
        "количество" : 10,
        "конвейер" : 1,
        "порция" : 2,
    },
    {
        "ингридиент" : "клубничное варенье",
        "количество" : 10,
        "конвейер" : 1,
        "порция" : 1.5,
    }
]
))






{
    1: {'начинки':
            [
                {'ингридиент': 'изюм', 'количество': 2, 'конвейер': 1, 'порция': 1},
                {'ингридиент': 'шоколад', 'количество': 10, 'конвейер': 1, 'порция': 2},
                {'ингридиент': 'клубничное варенье', 'количество': 10, 'конвейер': 1, 'порция': 1.5}
            ],
        'тесто': {'ингридиент': 'тесто', 'количество': 10, 'конвейер': 1, 'порция': 2}
    },
    2: {'начинки':
            [
                {'ингридиент': 'изюм', 'количество': 2, 'конвейер': 2, 'порция': 1}
            ],
        'тесто':
            {'ингридиент': 'тесто', 'количество': 10, 'конвейер': 2, 'порция': 2}
    }
}