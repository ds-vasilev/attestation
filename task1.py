import itertools
from typing import Iterable, Dict, Optional, List, Any


class OutOfResourceError(Exception):
    """Ислючение при отстутствии вариантов"""
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


def get_type(item: Dict) -> Optional[int]:
    return item.get("тип")


def calculate(available_ingredients_list: list) -> List:
    conveyor_resource = itertools.groupby(available_ingredients_list, get_type)
    valid_ingrs = {"кофе": [], "вода": [], "молоко": [], "сироп": []}
    for_print = list()
    for key, group in conveyor_resource:
        for resource in group:
            if resource.get('количество') - resource.get('порция') >= 0:         # если ресурса хватает на процию
                valid_ingrs[resource.get("тип")].append(resource.get("ресурс"))  # вносим назв ресурса в соотв словарь

    if len(valid_ingrs["кофе"]) == 0 or len(valid_ingrs["вода"]) == 0:           # ээсепшн. если нет кофе или воды
        raise OutOfResourceError("Не удалось найти ни одного напитка который можно было бы приготовить")

    for_print = list(itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"])) \
                + list(itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"], valid_ingrs["молоко"])) \
                + list(itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"], valid_ingrs["сироп"])) \
                + list(itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"], valid_ingrs["молоко"], \
                                         valid_ingrs["сироп"]))   # первый вариант вывода
    return for_print

    # # list_for_keys = list() # второй вариант вывода
    # for int_new, val_new in enumerate(for_print):
    #     for int_list, val_list in enumerate(val_new):
    #         for int_base, val_base in enumerate(valid_ingrs):
    #             if val_list in valid_ingrs[val_base]:
    #                 print(f"'{val_base}' : '{val_list}'")
    #                 # list_for_keys.append(val_base)  # попытка реализации через zip()



    # for_mapping = {"арабика": "кофе", "нескафе": "кофе",  'вода': 'вода', 'молоко': 'молоко', "сироп": "карамель"}
    # on_exit = []
    # two_ingr = (itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"]))
    # zaglushka = dict()
    # for x in two_ingr:
    #     for j in x:
    #         zaglushka.update({for_mapping.get(str(j)): j})
    # on_exit.append(zaglushka)
    # two_plus_milk = (itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"], valid_ingrs["молоко"]))
    # zaglushka = dict()
    # for x in two_plus_milk:
    #     for j in x:
    #         zaglushka.update({for_mapping.get(str(j)): j})
    # on_exit.append(zaglushka)
    #
    # two_plus_syr = (itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"], valid_ingrs["сироп"]))
    # zaglushka = dict()
    # for x in two_plus_syr:
    #     for j in x:
    #         zaglushka.update({for_mapping.get(str(j)): j})
    # on_exit.append(zaglushka)

    # print(list(itertools.product(valid_ingrs["кофе"], valid_ingrs["вода"])))





    # some_list = list()
    #
    # for item, val in enumerate(for_print):
    #     some_list.append(dict.fromkeys(val))
    # print(some_list)

    # some_more_list = some_list
    # print(some_list)
    # for sl_i, j in enumerate(some_list):
    #     for i in j:
    #         some_more_list[sl_i].update({for_mapping.get(i):i})
    # print(some_more_list)








x = [
    {
        "ресурс" : "арабика",
        "тип" : "кофе",
        "количество" : 1000,
        "порция" : 10
    },
    {
        "ресурс" : "молоко",
        "тип" : "молоко",
        "количество" : 1000,
        "порция" : 60
    },
    {
        "ресурс" : "вода",
        "тип" : "вода",
        "количество" : 1000,
        "порция" : 60
    },
    {
        "ресурс" : "карамель",
        "тип" : "сироп",
        "количество" : 170,
        "порция" : 80
    },
    {
        "ресурс" : "неcкафе",
        "тип" : "кофе",
        "количество" : 110,
        "порция" : 10
    },
]

y = [
    {
        "ресурс" : "арабика",
        "тип" : "кофе",
        "количество" : 1000,
        "порция" : 10
    },
    {
        "ресурс" : "молоко",
        "тип" : "молоко",
        "количество" : 1000,
        "порция" : 60
    },
    {
        "ресурс" : "вода",
        "тип" : "вода",
        "количество" : 1000,
        "порция" : 60
    },
    {
        "ресурс" : "карамель",
        "тип" : "сироп",
        "количество" : 90,
        "порция" : 80
    },
]

calculate(x)
