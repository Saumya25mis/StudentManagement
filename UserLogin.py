#!python
import cherrypy

from AuthController import AuthController, require, member_of, name_is


class RestrictedArea:

    _cp_config = {
        'auth.require': [member_of('admin')]
    }

    @cherrypy.expose
    def index(self):
        return """This is the admin only area."""


class Root:
    _cp_config = {
        'tools.sessions.on': True,
        'tools.auth.on': True
    }

    auth = AuthController()

    restricted = RestrictedArea()

    @cherrypy.expose
    @require()
    def index(self):
        return """Welcome"""


if __name__ == '__main__':
    cherrypy.quickstart(Root())
