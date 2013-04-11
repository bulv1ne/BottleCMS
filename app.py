#!/usr/bin/env python
from bottle import Bottle, run, template, debug, redirect, request, view, abort, error
from pymongo import MongoClient

DATABASE = 'BottleCMS'

app = Bottle()
# Connection to our Mongo Database
conn = MongoClient()


def get_page(callback):
    def wrapper(*args, **kwargs):
        # Select the correct database
        db = conn[DATABASE]
        # Get the page matching the url
        page = db.pages.find_one({'url':request.fullpath})
        if not page: # If no page has been found, return 404
            abort(404)
        body = callback(*args, page=page, **kwargs)
        return body
    return wrapper

@app.route('<url:path>')
@get_page
def main(url, page):
    # Return the content of the page
    page_template = page.get('template', None)
    if not page_template:
        return page.get('content','')
    return template(page_template, page=page)
    

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8096, reloader=True)