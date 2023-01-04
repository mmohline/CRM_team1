# -*- coding: utf-8 -*-
import time
import os
import matplotlib
import pygal


def graph():
    return locals()

@auth.requires_login()
def graph1():
    return dict(rows = db(db.contact).count(),
                new_lead_count = db(db.contact.lifecycleStage==1).count(),
                opportunity_count = db(db.contact.lifecycleStage==2).count(),
                currentcustomer_count = db(db.contact.lifecycleStage==3).count(),
                competitor_count = db(db.contact.lifecycleStage==4).count(),
                social_media_lead = db(db.contact.leadSource==1).count(),
                web_lead = db(db.contact.leadSource==2).count(),
                callin_lead = db(db.contact.leadSource==3).count(),
                coldcall_lead = db(db.contact.leadSource==4).count(),
                website_lead = db(db.contact.leadSource==5).count(),
                referral_lead = db(db.contact.leadSource==6).count(),
                searchengine_lead = db(db.contact.leadSource==7).count(),
                event_lead = db(db.contact.leadSource==8).count()
                )

def graph2():
    return dict(rows = db(db.contact).count(),
                new_lead_count = db(db.contact.lifecycleStage==1).count(),
                opportunity_count = db(db.contact.lifecycleStage==2).count(),
                currentcustomer_count = db(db.contact.lifecycleStage==3).count(),
                competitor_count = db(db.contact.lifecycleStage==4).count(),
                social_media_lead = db(db.contact.leadSource==1).count(),
                web_lead = db(db.contact.leadSource==2).count(),
                callin_lead = db(db.contact.leadSource==3).count(),
                coldcall_lead = db(db.contact.leadSource==4).count(),
                website_lead = db(db.contact.leadSource==5).count(),
                referral_lead = db(db.contact.leadSource==6).count(),
                searchengine_lead = db(db.contact.leadSource==7).count(),
                event_lead = db(db.contact.leadSource==8).count()
                )


def analytics():
    return locals()

def b_chart(): #couldn't get this to work
    custom_style = Style(
    colors=('#E80080', '#404040', '#9BC850')),
    b_chart = pygal.Bar(style=custom_style),
    b_chart.title = "Destiny Kill/Death Ratio",
    b_chart.add("Dijiphos", [0.94]),
    b_chart.add("Punisherdonk", [1.05]),
    b_chart.add("Musclemuffins20", [1.10]),
    b_chart.render_in_browser()

def serve_file():
    filename=request.args(0)

def index():
    return locals()

@auth.requires_login()
def index2():
    t = time.ctime()

    return dict(rows=db(db.contact).count(),
               states=db(db.states).count(),
               companies=db(db.company).count(),
               active_leads=db(db.contact.leadStatus=="active").count(),
               inactive_leads=db(db.contact.leadStatus=="inactive").count(),
               new_lead_count = db(db.contact.lifecycleStage==1).count(),
               percentage_new_lead_count = (db(db.contact.lifecycleStage==1).count()/db(db.contact).count()),
               rows2 = db(db.contact).select().last()['firstName'],
               rows3 = db(db.contact).select().last()['lastName'],
               rows4 = db(db.contact).select().last()['email'],
               rows5 = db(db.contact).select().last()['mobile'],
               rows6 = db(db.contact).select().last()['createdDate'],
               time = t
               )

@auth.requires_login()
def active_leads():
    if request.args(0) is None:
        rows = db(db.contact.leadStatus=="active").select()
    return locals()

@cache(request.env.path_info, time_expire=5, cache_model=cache.ram)
def cache_controller_and_view():
    """cache the output of the controller rendered by the view in ram"""

    t = time.ctime()
    d = dict(time=t, link=A('Reload page', _href=URL(r=request)))
    return response.render(d)


def user1():
    return dict(form=auth())

@auth.requires_login()
def contacts():
    if request.args(0) is None:
        rows = db(db.contact).select(orderby=db.contact.lastName | db.contact.firstName)
    else:
        letter = request.args(0)
        rows = db(db.contact.lastName.startswith(letter)).select(orderby=db.contact.lastName | db.contact.firstName)

    return locals()

def contacts1():
    return none
          #sql = "SELECT contact.id, contact.firstName, contact.lastName, contact.company, contact.email, contact.mobile, contact.address, contact.city, contact.states, contact.jobTitle, contact.contactType, #contact.lifecycleStage, contact.leadSource, contact.leadStatus, contact.createdDate "
        #sql = sql + "FROM contact;"
        #rows = db.executesql(sql)
        #return locals()


@auth.requires_login()
def companies():
    if request.args(0) is None:
        rows = db(db.company).select()
    return locals()


def companies1():
    return dict(rows=db(db.company).select())

def search_results():
    if request.vars.search_term:
        session.sterm = request.vars.search_term
        response.view = URL('basics','search_results.html')
    return dict()


def request_args():
    arg1 = float(request.args(0))
    arg2 = float(request.args(1))
    total = arg1 + arg2
    return locals()

@auth.requires_login()
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


#@auth.requires_login()

def contact_smartgrid():
    smartgrid = SQLFORM.smartgrid(db.contact, linked_tables=['lifecycleStage'])
    return dict(smartgrid=smartgrid)

def contact():
    grid = SQLFORM.grid(db.contact)
    return dict(grid=grid)

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
