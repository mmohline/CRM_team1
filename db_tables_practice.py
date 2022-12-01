db.define_table(
    "contacts",
    Field("first_name", notnull = True),
    Field("last_name", notnull = True),
    Field("company_name", ),
    Field("address"), # company address
    Field("city"),
    Field("state_name", ),
    Field("zip", ),
    Field("phone1", requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+'))),
    Field("phone2", requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+'))),
    Field("email", requires=IS_EMAIL()),
    Field("date_created"),
    Field("office_location" ),
    Field("office_phone"),
    Field("office_email"),
    Field("contact_type")
    )
