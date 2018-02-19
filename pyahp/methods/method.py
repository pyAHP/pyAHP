from abc import ABC, abstractmethod


class Method(ABC):
    def __init__(self):
        super.__init__()

    @abstractmethod
    def estimate(self, preference_matrix):
        pass
