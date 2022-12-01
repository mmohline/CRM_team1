db.define_table("contacts",
                Field("first_name", notnull = True),
                Field("last_name", notnull = True),
                Field("company_name"),
                Field("address"), # company address
                Field("city"),
                Field("state_name"),
                Field("zip"),
                Field("phone1", requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+'))),
                Field("phone2", requires = IS_EMPTY_OR(IS_MATCH('[\d\-\(\) ]+'))),
                Field("email", requires=IS_EMAIL()),
                Field("date_created"),
                Field("office_location" ),
                Field("office_phone"),
                Field("office_email"),
                Field("contact_type")
                )

db.define_table("game_types",
                Field("game_type")
                )


db.define_table("games",
                Field("game_name"),
                Field("game_type", "reference game_types")
                )

db.define_table("activities",
                Field("activty")
                )

db.define_table("lifecycle",
                Field("last_contacted", "reference contacts"),
                Field("how_contacted"),
                Field("game_of_intrest"),        #createTableForGames
                Field("next_update"),
                Field("game_bought", "reference games"),
                Field("game_type", "reference game_types")
                )

db.define_table("active_sales",
                Field("last_sale_date"),
                Field("location_of_sale", "reference locations"),
                Field("first_name", "reference contacts")
                )

db.define_table("region",
                Field("state_name","reference contacts"),
                Field("state_abbv"),
                Field("city","reference contacts"),
                Field("zip","reference contacts")
                )

db.define_table("locations",
                Field("address"),
                Field("company", "reference companies"),
                Field("state_abbv"),
                Field("city")
                )

db.define_table("companies",
                Field("company_name"),
                Field("address", "reference locations"),
                Field("date_created", requires=IS_DATE("%d/%m/%Y"))
                )

db.define_table("lead_source",
                Field("lead_source")
                )
