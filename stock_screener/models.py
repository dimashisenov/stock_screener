from sqlalchemy import Boolean, Column, Integer, String, Numeric
from sqlalchemy.sql.coercions import ColumnsClauseImpl


from database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)#every new record is incremented
    symbol = Column(String,unique=True,index=True)
    price = Column(Numeric(10,2))
    forward_pe = Column(Numeric(10,2))
    forward_eps = Column(Numeric(10,2))
    dividend_yield = Column(Numeric(10,2))
    ma_50 = Column(Numeric(10,2))
    ma_200 = Column(Numeric(10,2))


