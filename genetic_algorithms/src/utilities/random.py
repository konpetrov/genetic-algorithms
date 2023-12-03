import random


def set_random_seed(value: int):
    random.seed(value)


def probability(value: float):
    return random.random() < value


def select_random_item(items: list):
    return random.choice(items)


def select_random_items(items: list, number_to_select: int):
    return random.choices(items, k=number_to_select)


def select_non_repeating_random_items(items: list, number_to_select: int):
    return random.sample(items, k=number_to_select)
