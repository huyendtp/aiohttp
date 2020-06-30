import aiohttp_jinja2
from aiohttp import web
import db


async def index(request):
    return web.Response(text=str('demo'))

@aiohttp_jinja2.template('index.html')
async def get_all_user(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.user.select())
        records = await cursor.fetchall()
        user_list = [dict(q) for q in records]
        # return web.Response(text=str(user))
        return {'users': user_list}