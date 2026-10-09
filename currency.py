

class Convertor:

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if not self._initialized:
            self.rates_to_usd = {
                "USD": 1.0,
                "EUR": 1.09,
                "JPY": 0.0067,
                "GBP": 1.27,
                "CNY": 0.14,
                "CHF": 1.13,
                "CAD": 0.74
            }
            self._initialized = True


    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates_to_usd or to_currency not in self.rates_to_usd:
            raise ValueError("Unsupported currency for conversion.")
        amount_in_usd = float(amount) * self.rates_to_usd[from_currency]
        return round(amount_in_usd / self.rates_to_usd[to_currency], 2)




class Currency:

    def __init__(self, amount, denom="USD"):
        self.amount = float(amount)
        self.denomination = denom.upper()
        self.helper = Convertor()


    def __str__(self):
        return f"{self.amount:.2f} {self.denomination}"


    def getAmount(self):
        return self.amount


    def __add__(self, amount):
        new_total = self.amount + float(amount)
        return Currency(new_total, self.denomination)


    def __iadd__(self, amount):
        self.amount += float(amount)
        return self


    def __sub__(self, amount):
        new_total = self.amount - float(amount)
        return Currency(new_total, self.denomination)


    def __isub__(self, amount):
        self.amount -= float(amount)
        return self

    def __mul__(self, amount):
        new_total = self.amount * float(amount)
        return Currency(new_total, self.denomination)


    def __imul__(self, amount):
        self.amount *= float(amount)
        return self


    def __truediv__(self, amount):
        new_total = self.amount / float(amount)
        return Currency(new_total, self.denomination)


    def __itruediv__(self, amount):
        self.amount /= float(amount)
        return self


    def __floordiv__(self, amount):
        new_total = self.amount // float(amount)
        return Currency(new_total, self.denomination)


    def __round__(self, ndigits=0):
        self.amount = round(self.amount, ndigits)


    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False
        return self.amount == other.amount and self.denomination == other.denomination


    def __lt__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        
        return self.amount < other.amount


    def __gt__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        
        return self.amount > other.amount


    def __le__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        
        return self.amount <= other.amount


    def __ge__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        
        return self.amount >= other.amount


    def set_amount(self, amt):
        self.amount = float(amt)


    def convert(self, new_denom):
        newDenom = new_denom.upper()
        self.amount = self.helper.convert(self.amount, self.denomination, newDenom)
        self.denomination = newDenom

