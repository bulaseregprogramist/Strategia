"""
Файл с абстрактным классом 
про ресурсы игрока
"""

from abc import abstractmethod, ABC


class Resources(ABC):
    """
    Ресурсы игрока
    """
    
    @abstractmethod
    def t(self) -> None:
        """
        """
        pass

