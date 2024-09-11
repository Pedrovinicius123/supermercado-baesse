from sklalchemy import create_engine
from sklalchemy.ext.declarative import declarative_base
from sklalchemy import Table, String, Integer

engine = create_engine(":///")
base = declarative_base(engine)