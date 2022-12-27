# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    return locals()

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def contacts():
    form = SQLFORM.grid(db.contacts)
    return dict(grid=grid)

def companies():
    grid = SQLFORM.grid(db.companies)
    return dict(grid=grid)


def game_types():
    grid = SQLFORM.grid(db.game_types)
    return dict(grid=grid)

def games():
    grid = SQLFORM.grid(db.games)
    return dict(grid=grid)

def activites():
    grid = SQLFORM.grid(db.activities)
    return dict(grid=grid)

def lifecycle():
    grid = SQLFORM.grid(db.lifecycle)
    return dict(grid=grid)

def active_sales():
    grid = SQLFORM.grid(db.active_sales)
    return dict(grid=grid)

def states():
    grid = SQLFORM.grid(db.states)
    return dict(grid=grid)

def locations():
    grid = SQLFORM.grid(db.locations)
    return dict(grid=grid)

def lead_source():
    grid = SQLFORM.grid(db.lead_source)
    return dict(grid=grid)

def contact_types():
    grid = SQLFORM.grid(db.type_of_contacts)
    return dict(grid=grid)

def graph():
    response.view = "graph.html";
    return locals()

def filter():
    game_bought = db(db.contacts.game=="8").count()
    return locals()

def graph_data():
    cod = db(db.contacts.game=="7").count()
    cs = db(db.contacts.game=="8").count()
    val = db(db.contacts.game=="9").count()
    return response.json([cod,cs,val])

def search_results():
    if request.vars.search_term:
        session.sterm = request.vars.search_term
        response.view = "search_results.html"
    return dict()

def somefunction():
    pic = db(db.images=="1").select()   #select first picture
    return dict(pic=pic)
