import aiopg.sa
import sqlalchemy as sa
from aiomysql.sa import create_engine

from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

user = Table(
    'user', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(250), nullable=False),
    Column('phone', Date, nullable=False)
)

contact = Table(
    'contact', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('address', String(255), nullable=False),

    Column('user_id',
           Integer,
           ForeignKey('user.id', ondelete='CASCADE'))
)


async def init_pg(app):
    conf = app['config']['mysql']
    engine = await create_engine(minsize=conf['minsize'], maxsize=conf['maxsize'],
                                 user=conf['user'], db=conf['database'],
                                 host=conf['host'], password=conf['password'])
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
