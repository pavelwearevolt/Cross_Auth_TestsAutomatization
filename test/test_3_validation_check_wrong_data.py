__author__ = 'pavelkosicin'


def test_validation_check_wrong_data(app):
    app.validation.enter_wrong_data(username="test@example.com", password="aaaaaaaaaaa")
    app.validation.check_wrong_data()
