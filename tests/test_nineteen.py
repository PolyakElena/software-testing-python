from Apps.app import Application


def test_nineteen(app: Application):
    app.add_products(3)
    app.delete_all_products_from_cart()
