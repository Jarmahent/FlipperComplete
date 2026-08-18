from datetime import datetime
from pathlib import Path
from typing import Optional
import os

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, mapped_column, Mapped, sessionmaker

Base = declarative_base()

DEFAULT_DATABASE_PATH = Path(__file__).resolve().parents[1] / 'flipperdb.db'
DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{DEFAULT_DATABASE_PATH}')

connect_args = {'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Vehicle(Base):
    __tablename__ = 'Vehicle'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    vin: Mapped[str] = mapped_column(unique=True)
    purchase_price_c: Mapped[float]
    auction_fee_c: Mapped[float]
    status: Mapped[str]
    purchase_date: Mapped[datetime]


class Part(Base):
    __tablename__ = 'Part'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('Vehicle.id'))
    vehicle = relationship(Vehicle, foreign_keys=[vehicle_id])
    name: Mapped[str]
    oem_number: Mapped[str]
    condition_note: Mapped[str]
    loc_locker: Mapped[str]
    loc_bin: Mapped[str]
    est_value_c: Mapped[float]
    status: Mapped[str]


class Listing(Base):
    __tablename__ = 'Listing'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    part_id: Mapped[int] = mapped_column(ForeignKey('Part.id'))
    part = relationship(Part, foreign_keys=[part_id])
    platform: Mapped[str]
    external_id: Mapped[str]
    url: Mapped[str]
    price_c: Mapped[float]
    fees_c: Mapped[float]
    status: Mapped[str]
    listed_datetime: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    sold_datetime: Mapped[Optional[datetime]] = mapped_column(nullable=True)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
