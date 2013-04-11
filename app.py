#!/usr/bin/env python
from bottle import Bottle, run, template, debug, redirect, request, view, abort, error
from pymongo import MongoClient

DATABASE = 'BottleCMS'

app = Bottle()
# Connection to our Mongo Database
conn = MongoClient()

@app.route('<url:path>')
def main(url):
    # Select the correct database
    db = conn[DATABASE]
    # Get the page matching the url
    page = db.pages.find_one({'url':url})
    if not page: # If no page has been found, return 404
        abort(404)
    # Return the content of the page
    # @TODO: use template instead of content
    return page.get('content','')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8096, reloader=True)