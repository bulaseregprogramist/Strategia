"""
Файл, отвечающий за работу с БД
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


class StrategyDataBase(Base):
    __tablename__ = "strategy_db"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    value_name: Mapped[str] = mapped_column(index=True, nullable=False)

    value_count: Mapped[str] = mapped_column(index=True, nullable=False)


class StrategySQLAlchemy:
    """
    Класс для работы с базой данных 
    (Используется SQLAlchemy)
    """
    
    def __init__(self):
        self.engine = create_engine(
            "sqlite:///strategy_database.db",
            echo=False,          
            future=True 
        )
        Base.metadata.create_all(bind=self.engine)
    
    def create_table(self) -> None:
        """Создание таблицы"""
        Session = sessionmaker(bind=self.engine, expire_on_commit=False) 

    def insert_in_table(self) -> None:
        """Добавление в таблицу"""
        Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        with Session() as session:
            session.commit()

    def update_table(self) -> None:
        """Обновление таблицы"""
        Session = sessionmaker(bind=self.engine, expire_on_commit=False) 
        with Session() as session:
            session.commit()

