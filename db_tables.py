# -*- coding: utf-8 -*-


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



db.define_table("games",
                Field("game_name"),
                Field("game_type")
                )

db.define_table("activities",
                Field("direct_sale"),
                Field("advertiser"),
                Field("third_party"),
                Field("event_handler")
                )

db.define_table("lifecycle",
                Field("last_contacted", "reference contacts"),
                Field("how_contacted"),
                Field("game_of_intrest"),        #createTableForGames
                Field("next_update"),
                Field("game_bought", "reference games"),
                Field("game_type", "reference games")
                )

db.define_table("active_sales",
                Field("last_sale_date"),
                Field("location_of_sale"),
                Field("first_name", "references contacts"),
                Field("email", requires=IS_EMAIL())
                )

db.define_table("region",
                Field("state_name","references contacts"),
                Field("state_abbv"),
                Field("city","references contacts"),
                Field("zip","references contacts")
                )

db.define_table("locations",
                Field("address"),
                Field("company_name", "references contacts"),
                Field("office_location","references contacts"),
                Field("state_abbv"),
                Field("city")
                )

db.define_table("companines",
                Field("company_name", "references locations"),
                Field("address", "references locations"),
                Field("date_created", requires=IS_DATE("%d/%m/%Y"))
                )

db.define_table("lead_source",
                Field("web","references contacts"),
                Field("walk_in","references contacts"),
                Field("on_call","references contacts"),
                Field("mail","references contacts"),
                Field("email","references contacts")
                )
