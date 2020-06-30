from views.demo import index, get_all_user


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/users', get_all_user)
