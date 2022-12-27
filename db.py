
db.define_table("contact_types",
                 Field("contact"),
                 format = "%(contact)s"
                 )

db.define_table("games",
                Field("game"),
                format = "%(game)s"
                )



db.define_table("contacts",
                Field("first_name"),
                Field("last_name"),
                Field("company"),
                Field("address"), # company address
                Field("city"),
                Field("state_name"),
                Field("zip"),
                Field("phone", requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+'))),
                Field("email", requires=IS_EMAIL()),
                Field("date_created"),
                Field("office_location"),
                Field("office_phone"),
                Field("office_email"),
                Field("contact", "reference contact_types"),
                Field("game", "reference games")
                )



db.define_table("locations",
                Field("address", "reference contacts"),
                Field("company", "reference contacts"),
                Field("city", "reference contacts"),
                Field("state_name", "reference contacts")
                )



db.define_table("companies",
                Field("company", "reference contacts"),
                Field("address", "reference locations"),
                Field("date_created", requires=IS_DATE("%d/%m/%Y"))
                )


db.define_table("activities",
                Field("activty")
                )


db.define_table("lifecycle",
                Field("date_created", "reference contacts"),
                Field("game", "reference games"), #so we know what games they are into
                Field("how_to_contact") #not sure about this field the table bassically gives us this info from the data the date_created,lead_source and game_name
                )

db.define_table("active_sales",
                Field("last_sale_date"),
                Field("location_of_sale", "reference locations"),
                Field("first_name", "reference contacts")
                )

db.define_table('images',Field('picture','upload'))