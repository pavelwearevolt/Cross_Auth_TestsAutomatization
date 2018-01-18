__author__ = 'pavelkosicin'


def test_validation_check_wrong_email_correct_password(app):
    app.validation.enter_wrong_data(username="test@example.com", password="abcd1234")
    app.validation.check_wrong_data()
