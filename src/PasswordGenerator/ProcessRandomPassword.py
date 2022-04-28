import random


class RandomPassword:
    '''
    @author: Simon Nguyen 
    @date: 2020-04-24
    '''

    def __init__(self, __length: int) -> None:
        self._lower:str= "abcdefghijklmnopqrstuvwxyz"
        self._upper:str= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._numbers:str= "0123456789"
        self._symbol:str= "!@#$%^&*()"
        self._length:int = __length
        self.joiner:str = ""

    def WithAllCases(self, _lower:bool=False, _upper:bool=False, _numbers:bool=False, _symbol:bool=False) -> str:
        try:
            if _lower:
                self.joiner = self._lower
            if _upper:
                self.joiner = self._upper
            if _numbers:
                self.joiner = self._numbers
            if _symbol:
                self.joiner = self._symbol

            if _lower and _upper:
                self.joiner = self._lower + self._upper
            if _lower and _numbers:
                self.joiner = self._lower + self._numbers
            if _lower and _symbol:
                self.joiner = self._lower + self._symbol
            if _upper and _numbers:
                self.joiner = self._upper + self._numbers
            if _upper and _symbol:
                self.joiner = self._upper + self._symbol
            if _numbers and _symbol:
                self.joiner = self._numbers + self._symbol

            if _lower and _upper and _numbers:
                self.joiner = self._lower + self._upper + self._numbers
            if _lower and _upper and _symbol:
                self.joiner = self._lower + self._upper + self._symbol
            if _lower and _numbers and _symbol:
                self.joiner = self._lower + self._numbers + self._symbol
            if _upper and _numbers and _symbol:
                self.joiner = self._upper + self._numbers + self._symbol
            if _lower and _upper and _numbers and _symbol:
                self.joiner = self._lower + self._upper + self._numbers + self._symbol
            self.password:str = "".join(random.choice(self.joiner) for i in range(self._length))
            return self.password
        except TypeError as T:
            print(T)
            return None