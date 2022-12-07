import datetime

db.define_table(
    "states",
    Field("state_name"),
    format='%(state_name)s'
    )

db.define_table(
    "companies",
    Field("company"),
    format='%(company)s'
    )


db.define_table(
    "office_locations",
    Field("Region")
    )

db.define_table(
    "contactType",
    Field("contactType")
    )

db.define_table(
    'contacts',
    Field('firstName'),
    Field('lastName'),
    Field('cell', requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+')) ),
    Field('email', requires = IS_EMPTY_OR(IS_EMAIL()) ),
    Field('city'),
    Field('state_name', 'reference states'),
    Field('zip', requires = IS_EMPTY_OR(IS_LENGTH(5,5)) ),
    Field('companyId', 'reference companies'),
    Field('officeLocationId', 'reference office_locations'),
    Field('officePhone', requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+')) ),
    Field('title'),
    Field('contactType', 'reference contactType'),
    Field('createdDate', type='date'),
    Field('lastChanged', type='date'),
   )
