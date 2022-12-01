# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from tables.py")


def data():
    rows = db(db.contacts).select()
    return locals()



def contacts():
    grid = SQLFORM.grid(db.contacts)
    return dict(grid=grid)

def companies():
    grid = SQLFORM.grid(db.company)
    return dict(grid=grid)

def view():
    if request.args(0) is None:
        rows = db(db.contacts).select(orderby=db.contacts.last_name | db.contacts.first_name)
    else:
        letter = request.args(0)
        rows = db(db.contacts.last_name.startswith(letter)).select(orderby=db.contacts.last_name | db.contacts.first_name)
    return locals()


def update():
    record = db.contacts(request.args(0)) or redirect(URL("view"))
    form = SQLFORM(db.contacts, record)
    if form.process().accepted:
        redirect(URL("view"))
        response.flash = T("Record Updated")

    else:
        response.flash= T("Please complete the form.")
    return locals()
