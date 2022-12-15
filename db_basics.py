# -*- coding: utf-8 -*-
# try something like

def index():
    return locals()

def request_args():
    arg1 = float(request.args(0))
    arg2 = float(request.args(1))
    total = arg1 + arg2
    return locals()

def post():
    form = SQLFORM(db.contact).process()
    return locals()

def filter():
    row1_count = db(db.contact).count()
    row2_count = db(db.contact.city=='Cleveland').count()
    row2_all_sorted_by_name=db(db.contact).select(orderby=db.contact.lastName | db.contact.firstName)
    row2_startswith = db(db.contact.lastName.startswith('M')).select(orderby=db.contact.city)
    row3_by_state = db(~(db.contact.states==1)).select(orderby=db.contact.lastName)
    row3_combo = db((db.contact.states==220)&(db.contact.lastName.startswith('M'))).select(orderby=db.contact.lastName)
    return locals()


def bootstrap_datetime(field, value):
    input = INPUT(_name=field.name, _type='text',
                  _id='%s_%s' % (field.tablename, field.name),
                  data=dict(format='dd/MM/yyyy hh:mm:ss'),
                  value=str(value) if value is not None else '',
                  requires=field.requires)
    return DIV(input,
               SPAN(I(data={'time-icon': 'icon-time',
                            'date-icon': 'icon-calendar'})),
               _class='input-append date')

def display_your_form():
    update = db.register(request.args(0))
    form = SQLFORM(db.contactType, update)
    return dict(form=form)



def counter():
    if not session.counter:
        session.counter=1
    else:
        session.counter +=1
    return dict(message="Hello from my app", counter=session.counter)

def first():
   if request.vars.visitor_name:
    session.visitor_name=request.vars.visitor_name
    redirect(URL('second'))
   return dict()

def second():
    return dict()

def New_Contact_Form():
    record = db.contact(request.args(0))
    form = SQLFORM(db.contact, formstyle='bootstrap4_inline')
    form.add_button('Back', URL('other_page'))
    if form.process().accepted:
        response.flash = 'New contact added'
    elif form.errors:
        response.flash = 'Edit fields to add new contact'
    else:
        response.flash = 'Enter info to add a new contact'
    return dict(form=form)

def Manual_Add_Contact_Form():
    record = db.contact(request.args(0))
    form = SQLFORM(db.contact, record)
    if form.process(session=None, formname='contact').accepted:
        response.flash = 'New contact added'
    elif form.errors:
        response.flash = 'Edit fields to add new contact'
    else:
        response.flash = 'Enter info to add a new contact'
    return dict()

def add_contact_btsrapForm():
    record = db.contact(request.args(0))
    form = SQLFORM(db.contact, record)
    if form.process(session=None, formname='contact').accepted:
        response.flash = 'New contact added'
    elif form.errors:
        response.flash = 'Edit fields to add new contact'
    else:
        response.flash = 'Enter info to add a new contact'
    return dict()


def Add_Contact():
    form = SQLFORM.factory(
        Field('firstName',
              label='First Name',
              requires=IS_NOT_EMPTY()),
        Field('lastName',
              label='Last Name',
              requires=IS_NOT_EMPTY()),
        Field('company',
              label='Company',
              requires=IS_NOT_EMPTY()),
        Field('email',
              label='Email'),
        Field('mobile',
              label='Cell Phone'),
        Field('address',
              label='Address'),
        Field('city',
              label='City'),
        Field('states',
              label='State'),
        Field('jobTitle',
              label='Job Title'),
        Field('contactType',
              label='Type of Contact'),
        Field('lifecycleStage',
              label="Lifecycle Stage"),
        Field('leadSource',
              label='Lead Source (where info came from)'),
        Field('leadStatus',
              label='Lead Status'),
        Field('createdDate',
              label='Date info Acquired',
              requires = IS_DATE(format=T('%Y-%m-%d'),
                                error_message='must be YYY-MM-DD!'))
        )
    if form.process().accepted:
        response.flash = 'New contact added'
    elif form.errors:
        response.flash = 'Edit fields to add contact'

    return dict(form=form)


@auth.requires_login()
def new_contact():
    form = SQLFORM(db.contact).process()
    return locals()

def company():
    grid = SQLFORM.grid(db.company)
    return dict(grid=grid)

def states():
    grid = SQLFORM.grid(db.states)
    return dict(grid=grid)

def contactType():
    grid = SQLFORM.grid(db.contactType)
    return dict(grid=grid)

def lifecycleStage():
    grid = SQLFORM.grid(db.lifecycleStage)
    return dict(grid=grid)


def testdb():
    rows = db( db.contact.firstName != None).select()
    response.view = "testdb.html";
    return locals();

def graphs():
    simulation = start.Simulation()
    graphs = simulation.run()
    return graphs
