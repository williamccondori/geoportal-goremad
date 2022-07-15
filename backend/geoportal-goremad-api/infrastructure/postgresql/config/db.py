from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///:memory:", echo=True)

metadata = MetaData()

connection = engine.connect()
