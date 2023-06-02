from enum import Enum
from .backtracking import backtracking
from .greedy_consigna import greedy_consigna
from .greedy_alternativo import greedy_alternativo


class Algorithm(str, Enum):
    EXACT = "E"
    GREEDY = "A"
    GREEDY_ALT = "A2"

    def func(self):
        if self == Algorithm.EXACT:
            return backtracking
        elif self == Algorithm.GREEDY:
            return greedy_consigna
        return greedy_alternativo

    def __str__(self):
        if self == Algorithm.EXACT:
            return "Backtracking"
        elif self == Algorithm.GREEDY:
            return "Greedy consigna"
        return "Greedy alternativo"
