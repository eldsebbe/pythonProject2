from typing import Optional
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import delete
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)

session = Session(engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    adress: Mapped[str] = mapped_column(String(50))
    postadress: Mapped[str] = mapped_column(String(50))
    postnummer: Mapped[str] = mapped_column()
    paid: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, lastname={self.lastname!r}," \
               f"adress={self.adress!r}, postadress={self.postadress!r}, postnummer={self.postnummer!r}, paid={self.paid!r})"
    def __init__(self, namn, lastnamn, adressin, padress, pnummer, betalt):
        self.name = namn
        self.lastname = lastnamn
        self.adress = adressin
        self.postadress = padress
        self.postnummer = pnummer
        self.paid = betalt

def Inserted(name, lastname, adress, postadress, postnummer, paid):
    user_tab = User(name,lastname,adress,postadress,postnummer,paid)
    session.add(user_tab)
    session.commit()

def CreateDB():
    Base.metadata.create_all(engine)

def selectuser(ids):
    stmt = select(User).where(User.id.is_(ids))
    for user in session.scalars(stmt):
        return user

def deleteuser(ids):
    stmt = delete(User).where(User.id.is_(ids))
    session.execute(stmt)
    session.commit()

