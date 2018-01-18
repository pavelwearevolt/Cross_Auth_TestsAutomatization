__author__ = 'pavelkosicin'


def test_validation_check_correct_email_wrong_password(app):
    app.validation.enter_wrong_data(username="pavel.kosicin@wearevolt.com", password="aaaaaaaaaa")
    app.validation.check_wrong_data()
