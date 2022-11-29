# -*- coding: utf-8 -*-
db.define_table(
    "contacts",
    Field("first_name"),
    Field("last_name"),
    Field("company_name"),
    Field("address"),
    Field("city"),
    Field("state_name"),
    Field("zip"),
    Field("phone1"),
    Field("phone2"),
    Field("email", requires=IS_EMAIL()),
    )




db.define_table("companines",
                Field("name"),
                Field("address"),
                Field("date_time")
                )

db.define_table("lead_source",
                Field("web"),
                Field("walk_in"),
                Field("on_call"),
                Field("mail"),
                Field("email", requires=IS_EMAIL())
                )

db.define_table("locations",
                Field("address"),
                Field("company_name"),
                Field("main_phone"),
                Field("sic_number"),
                Field("state_abbv"),
                Field("city")
                )
db.define_table("activities",
                Field("direct_sale"),
                Field("advertiser"),
                Field("third_party"),
                Field("event_handler")
                )

db.define_table("lifecycle",
                Field("last_contacted")
                )

db.define_table("active_sales",
                Field("last_sale_date"),
                Field("location_of_sale"),
                Field("first_name"),
                Field("email", requires=IS_EMAIL())
                )
