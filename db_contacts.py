import datetime

db.define_table(
    "company",
    Field("name"),
    format = '%(name)s'
    )

db.define_table(
    "states",
    Field("stateNames"),
    format = '%(stateNames)s'
    )

db.define_table(
    "contactType",
    Field("contactType"),
    format = '%(contactType)s'
    )

db.define_table(
    "lifecycleStage",
     Field("lifecycleStage"),
    format = '%(lifecycleStage)s'
    )


db.define_table(
    "contact",
    Field("firstName", notnull=True),
    Field("lastName"),
    Field("company", "reference company"),
    Field("email", requires=IS_EMAIL()),
    Field("mobile"),
    Field("address"),
    Field("city"),
    Field("states", "reference states"),
    Field("jobTitle"),
    Field("contactType", "reference contactType"),
    Field("lifecycleStage", "reference lifecycleStage"),
    Field("leadStatus", requires=IS_IN_SET(["active", "inactive"])),
    Field("createdDate", type='datetime', default=datetime.datetime.now, requires=IS_DATE(format=('%Y-%m-%d')))
    )
