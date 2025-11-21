"""
Файл с абстрактным классом 
про работников игрока
"""

from abc import abstractmethod, ABC


class Workers(ABC):
    """
    Работники игрока
    """
    
    @abstractmethod
    def t(self) -> None:
        """
        """
        pass
