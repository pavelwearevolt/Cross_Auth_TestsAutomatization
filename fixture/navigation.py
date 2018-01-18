__author__ = 'pavelkosicin'


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_cross_auth_page(self):
        wd = self.app.wd
        wd.get("https://cross-auth-staging.herokuapp.com/")
