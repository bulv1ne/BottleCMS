#!/usr/bin/env python
from bottle import Bottle, run, template, debug, redirect, request, view, abort, error
from pymongo import MongoClient
from bson.objectid import ObjectId

DATABASE = 'BottleCMS'

# Connection to our Mongo Database
conn = MongoClient()


# Admin app
admin_app = Bottle()

@admin_app.route('/', name='admin', template='admin.tpl')
def admin():
    # Select the correct database
    db = conn[DATABASE]
    return {
            'pages': db.pages.find(),
            'get_url':admin_app.get_url
            }

@admin_app.route('/page/<page>', method=['GET','POST'], name='admin_page', template='admin_page.tpl')
def admin_page(page):
    # Select the correct database
    db = conn[DATABASE]
    page = db.pages.find_one({ '_id': ObjectId(page) })
    if not page:
        abort(404)
        
    # Check for post request
    if request.method == "POST":
        page.update(request.forms)
        db.pages.save(page)
    
    return {
            'page': page,
            'get_url':admin_app.get_url
            }

@admin_app.route('/page/new', method=['GET','POST'], name='admin_page_new', template='admin_page_new.tpl')
def admin_page_new():
    # Check for post request
    if request.method == "POST":
        # Select the correct database
        db = conn[DATABASE]
        page = {}
        page.update(request.forms)
        db.pages.save(page)
        redirect(admin_app.get_url('admin_page', page=page.get('_id')))
    
    return {
            'page': {},
            'get_url':admin_app.get_url
            }
 

# Root app
app = Bottle()
# Mount the admin app
app.mount('/admin', admin_app)

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
    page_template = page.get('template', None)
    if not page_template:
        # Return the content of the page
        return page.get('content','')
    return template(page_template, page=page)
    

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8096, reloader=True)
