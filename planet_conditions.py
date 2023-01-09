#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#======================================#
#=         PLANET CONDITIONS          =#
#======================================#

"""
    Выбирает случайное количество и случайные настройки для игры
    в соответствии с весовыми коэффициентами вероятностей.
    Для игры Dome Keeper.
"""


from random import choices, sample
from typing import Any


class Settings(dict):
    def __init__(self, *kv_args: tuple[Any, int]):
        super().__init__({setting:prob for (setting, prob) in kv_args})
        self._choices = list(self.keys())

    def choices(self):
        return self._choices

    # gives first weighted choice
    def weighted_choice(self):
        return choices(self.choices(), list(self.values()))[0]

class BeatifulHeader:
    def __init__(self, title: str):
        self._title = f' {title} '

    def __repr__(self):
        return f'{self._title:=^55}'


# Количество случайных настроек
AMOUNTS = Settings(
#   Количество             Вероятность
    (0,                    4),
    (1,                    4),
    (2,                    3),
    (3,                    2),
    (4,                    1),
)


# Настройки планеты
PLANET_CONDITIONS = Settings(
#   Настройка              Вероятность
    ("Feeble enemies",     2),
    ("Long cycles",        3),
    ("Double iron",        1),
    ("Maze structure",     4),
)


# Unit test
def test_weighted_choice(settings: Settings):
    stats = {stat:0 for stat in range(len(settings))}
    test_range = 10_000
    for _ in range(test_range):
        choice = settings.weighted_choice()
        stats[choice] += 1
    percented_stats = { k: f"{int(v / test_range * 100)}%" for k, v in stats.items() }
    print(f"Probability distribution test results:\n{percented_stats}")


#===================== MAIN =====================

def main():
    print(BeatifulHeader('Testing probabilities'))
    test_weighted_choice(AMOUNTS)
    print()
    print(BeatifulHeader('Detecting planet conditions'))
    
    amount = AMOUNTS.weighted_choice()
    if amount == 0:
        print("No planet conditions.\n")
        return

    print(f"Amount of planet conditions: {amount}")

    result = sample(PLANET_CONDITIONS.choices(), k=amount)
        
    print("\n".join(f'\t+ {r}' for r in result))
    print()

#================================================


if __name__ == "__main__":
    main()