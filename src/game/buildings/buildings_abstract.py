"""
Файл с абстрактным классом 
про постройки игрока
"""

from abc import abstractmethod, ABC


class Buildings(ABC):
    """
    Постройки игрока
    """
    
    @abstractmethod
    def t(self) -> None:
        """
        """
        pass

