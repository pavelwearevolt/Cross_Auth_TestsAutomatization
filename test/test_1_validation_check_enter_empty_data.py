__author__ = 'pavelkosicin'


def test_validation_check_enter_empty_data(app):
    app.validation.enter_wrong_data(username="", password="")
    app.validation.check_empty_data_error_message()
