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


from random import choices
from typing import Any


class Settings(dict):
    def __init__(self, *kv_args: tuple[Any, int]):
        super().__init__({setting:prob for (setting, prob) in kv_args})
        self._choices = list(self.keys())

    def choices(self) -> list[Any]:
        return self._choices

    def weighted_choice(self, num_choices: int = 1) -> list[Any]:
        return choices(self.choices(), list(self.values()), k=num_choices)

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
    test_condition = settings.weighted_choice()
    assert len(test_condition) > 0
    del test_condition

    stats = {stat:0 for stat in range(len(settings))}
    test_range = 10_000
    for _ in range(test_range):
        choice = settings.weighted_choice()[0]
        stats[choice] += 1
    percented_stats = { setting: f"{prob / test_range:.2%}" for setting, prob in stats.items() }
    print(f"Probability distribution test results:\n{percented_stats}")


#===================== MAIN =====================

def main():
    print(BeatifulHeader('Testing probabilities'))
    test_weighted_choice(AMOUNTS)
    print()
    print(BeatifulHeader('Detecting planet conditions'))
    
    condition = AMOUNTS.weighted_choice()
    assert len(condition) == 1
    
    num_conditions = condition[0]
    if num_conditions == 0:
        print("No planet conditions.\n")
        return

    print(f"Amount of planet conditions: {num_conditions}")

    result = PLANET_CONDITIONS.weighted_choice(num_conditions)
        
    print("\n".join(f'\t+ {r}' for r in result))
    print()

#================================================


if __name__ == "__main__":
    main()