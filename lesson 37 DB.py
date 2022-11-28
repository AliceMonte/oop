import sqlite3 as sl
conn = sl.connect("l37.db")
curs = conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS spravocnik (
    full_name TEXT,
    academic_degree TEXT,
    scientific_direction TEXT,
    place_of_work TEXT,
    department TEXT,
    position TEXT,
    country TEXT,
    city TEXT,
    adress TEXT,
    work_phone BIGINT,
    email TEXT,
    speaker_or_participant TEXT,
    invitation_data DATETIME,
    application_data DATETIME,
    topic TEXT,
    any_thesis TEXT,
    arrival_date DATETIME,
    hotel_need TEXT,
    departure_date DATETIME
    );""")
conn.commit()
curs.execute("""CREATE TABLE IF NOT EXISTS konference (
    Heading TEXT,
    Start_date DATETIME,
    Location TEXT,
    Organizers BIGINT,
    Sponsors BIGINT,
    conf_lasting BIGINT,
    participants_number BIGINT,
    speakers_number BIGINT
    );""")
conn.commit()
curs.close()
conn.close()

