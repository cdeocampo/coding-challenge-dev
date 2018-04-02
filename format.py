import abc

class Format(abc.ABC):
    @abc.abstractmethod
    def getCost(self):
        pass