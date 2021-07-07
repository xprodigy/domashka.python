print('Lesson 7_2:')

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def add():
        pass


class Topcoat(Clothes):
    __total = 0

    def add(self, size):
        self.__total += size * 6.5 + 0.5

    @property
    def total(self):
        return self.__total


class Suit(Clothes):
    __total = 0

    def add(self, height):
        self.__total += 2 * height + 0.3

    @property
    def total(self):
        return self.__total


topcoats = Topcoat()
suits = Suit()

#   Добавляем в рассчет несколько единиц одежды
topcoats.add(48)
suits.add(154)
topcoats.add(52)
suits.add(162)

#   Выводим резульат рассчета расхода ткани
print(f"Расход ткани на пиджаки {topcoats.total:.2f}, расход на костюмы {suits.total:.2f}. \n"
      f"Общий расход ткани {topcoats.total + suits.total:.2f}")
