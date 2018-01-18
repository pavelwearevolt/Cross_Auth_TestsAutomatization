__author__ = 'pavelkosicin'


def test_validation_check_invalid_email_short_password(app):
    app.validation.enter_wrong_data(username="p", password="a")
    app.validation.check_invalid_email_short_password_error_message()
