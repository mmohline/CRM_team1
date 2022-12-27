def index(): return dict(message="hello from contacts.py")

def data():
    rows = db(db.contacts).select()
    return locals()


def add():
    form = SQLFORM(db.contacts).process()
    return locals()

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
        response.flash = T("Record Updated")
    else:
        response.flash = T("Please complete the form")
    return locals()

def search_results():
    if request.vars.search_term:
        session.sterm = request.vars.search_term
        response.view = "search_results.html"
    return dict()

def somefunction():
    pic = db(db.images).select().first().picture   #select first picture
    return dict(pic=pic)