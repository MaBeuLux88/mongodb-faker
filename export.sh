#!/usr/bin/env bash
mongoexport --uri "mongodb://localhost/test" --collection coll --type csv --out persons.csv --fields=_id,firstname,lastname,age,size,alive,timestamp,date_of_birth,licence_date,certificate_date,year_inserted,month_inserted,day_inserted,address_number,street_name,postcode,city,country
