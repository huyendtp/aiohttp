import aiopg
from sqlalchemy import create_engine, MetaData

from db import user, contact
from settings import config

connection_str = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[user, contact])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(user.insert(), [
        {'name': 'huyendtp', 'phone': '0909090909'}
    ])
    conn.execute(contact.insert(), [
        {'name': 'huyendtp', 'address': '17 Ba Huyen Thanh Quan', 'user_id': 1},
        {'name': 'huyendtp', 'address': '740/8 Su Van Hanh', 'user_id': 1}
    ])
    conn.close()


if __name__ == '__main__':
    db_url = connection_str.format(**config['mysql'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
