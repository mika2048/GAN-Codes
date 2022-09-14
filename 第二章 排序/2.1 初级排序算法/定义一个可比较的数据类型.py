class Comparable:
    _day:int
    _month:int
    _year:int

    def __init__(self,d:int,m:int,y:int):
        self._day=d;self._month=m;self._year=y

    def day(self):return self._day
    def month(self):return self._month
    def year(self):return self._year

    def compareTo(self,other:"Comparable"):
        if self._year>other._year:return 1
        if self._year<other._year:return -1
        if self._month>other._month:return 1
        if self._month<other._month:return -1
        if self._day>other._day:return 1
        if self._day<other._day:return -1
        return 0
    
    def __str__(self):
        return f"{self._day}/{self._month}/{self._year}"