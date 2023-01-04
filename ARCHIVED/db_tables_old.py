import datetime
#change me!
db.define_table(
    "states",
    Field("state_name"),
    format='%(state_name)s'
    )

db.define_table(
    "companies",
    Field("company"),
    Field("city"),
    Field("state_name"),
    format='%(company)s'
    )


db.define_table(
    "contactType",
    Field("contactType"),
    format = '%(contactType)s'
    )

db.define_table(
    'contacts',
    Field('firstName'),
    Field('lastName'),
    Field('cellPhone'),
    Field('email'),
    Field('jobTitle'),
    Field('officePhone'),
    Field('officeEmail'),
    Field('city'),
    Field('contactType', 'reference contactType'),
    Field('company', 'reference companies')
    )
