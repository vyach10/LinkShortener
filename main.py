from flask import Flask, redirect
from flask_restful import Resource, Api
from create_table import create_table
from search import search_by_full_link, search_by_short_link
from insert import insert

app = Flask(__name__)
api = Api(app)

create_table()

class SearchShortLink(Resource):
    def get(self, short_link):
        full_link = search_by_short_link(short_link)
        if full_link is not False:
            full_link = full_link[0]
            if full_link[0:6] != 'http://':
                full_link = 'http://' + full_link
            return redirect(full_link)
        else:
            return("Shortcut has not been created yet.")

class AddLink(Resource):
    # метод GET – чтобы работало из браузера
    def get(self, full_link):
        short_link = search_by_full_link(full_link)
        if short_link is False:
            short_link = insert(full_link)
            return(f'Shortcut created: {short_link}')
        else:
            return(f"Shortcut has been created before: {short_link[0]}")

api.add_resource(SearchShortLink, '/<string:short_link>')
api.add_resource(AddLink, '/add/<string:full_link>')

if __name__ == '__main__':
    app.run(debug=True)