import sqlite3 as sl
conn = sl.connect("l39.db")
curs = conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS Spravocnik (
    full_name TEXT,
    academic_degree TEXT,
    scientific_direction TEXT,
    place_of_work TEXT,
    department TEXT,
    position TEXT,
    country TEXT,
    city TEXT,
    adress TEXT,
    work_phone TEXT,
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
curs.execute("""CREATE TABLE IF NOT EXISTS Konference (
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
l1 = ['Grigorenko E.S.', 'Bachelor', 'Social Sciences', 'Institute of Social Sciences RANEPA', 'Department of Social Sciences', 'Lecturer', 'Russia', 'Moscow', 'pr. Vernadsky, 82/3', '+7495 642-92-46', 'Gkate@gmail.com', 'speaker', '20.11.2022', '25.11.2022', 'Social Sciences', 'yes', '02.12.2022', 'yes', '05.12.2022']
l2 = ['Kamornikova M.V.', 'Doctoral Degree', 'Humanitarian sciences', 'Moscow Humanitarian University', 'Department of Humanitarian sciences', 'Headmaster', 'Russia', 'Moscow', 'st. Youth, 5', '+7499 374-51-71', 'Kmv@gmail.com', 'speaker', '20.11.2022', '27.11.2022', 'Humanitarian sciences', 'yes', '03.12.2022', 'no', '04.12.2022']
l3 = ['Iskritskaya O.A.', 'Associate Degree', 'Humanitarian sciences', 'Moscow State Humanitarian and Economic University', 'Department of Humanitarian sciences', 'Assistant', 'Russia', 'Moscow', ' st. Losinoostrovskaya, 49', '+7499 160-22-05', 'OlyaI@gmail.com', 'participant', '25.11.2022', '26.11.2022', '-', '-', '03.12.2022', 'yes', '05.12.2022']
l4 = ['Vorotilkina M.S.', 'Doctoral Degree', 'Natural Sciences', 'Institute of Genetics and Cytology', 'Department of Genetics', 'Senior researcher', 'Belarus', 'Minsk', 'st. Academic, 27', '+8017 378-18-56', 'Vmasha@gmail.com', 'speaker', '20.11.2022', '23.11.2022', 'Genetics', 'no', '01.12.2022', 'yes', '05.12.2022']
l5 = ['Beliaev D.V.', 'Associate Degree', 'Natural Sciences', 'Lithuanian University Medical Academy for Health Sciences', 'Department of Health Sciences', 'Laboratory assistant', 'Lithuania', 'Kaunas', 'A. Mickevičiaus g. 9', '+370 37 327201', 'DimaB@gmail.com', 'participant', '25.11.2022', '28.11.2022', '-', '-', '03.12.2022', 'no', '04.12.2022']
l6 = ['Malaskova I.A.', 'Bachelor', 'Social Sciences', 'University of Social and Human Sciences', 'Department of Social Sciences', 'Lecturer', 'Poland', 'Warszawa', ' st. Chodakowska 19/31', '+4822 517-96-00', 'MIra@gmail.com', 'participant', '25.11.2022', '26.11.2022', '-', '-', '02.12.2022', 'yes', '04.12.2022']
zap1 = """ INSERT INTO Spravocnik VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
curs.execute("SELECT full_name FROM Spravocnik")
if curs.fetchone() is None:
    curs.execute(zap1, l1)
    curs.execute(zap1, l2)
    curs.execute(zap1, l3)
    curs.execute(zap1, l4)
    curs.execute(zap1, l5)
    curs.execute(zap1, l6)
    conn.commit()
else:
    print('Такой участник уже имеется!')
conn.commit()
t1 = ('Advances in Science and Technology', '04.12.2022', 'Belarusian State University', 2, 5, 1, 150, 10)
t2 = ('Eurasiascience', '05.12.2022', 'Belarusian State University', 3, 8, 2, 300, 20)
t3 = ('Students Cup 2022"', '07.12.2022', 'Belarusian State University', 2, 2, 1, 100, 10)
t4 = ('Science and education: topical issues, achievements and innovations', '08.12.2022', 'Belarusian State University', 2, 3, 1, 90, 5)
t5 = ('The unity of science and education as a tool for the transition to the post-industrial world', '09.12.2022', 'Belarusian State University', 2, 4, 2, 200, 10)
t6 = ('The development of science and technology: a mechanism for choosing and implementing priorities', '11.12.2022', 'Belarusian State University', 3, 5, 2, 130, 10)
zap2 = """ INSERT INTO Konference VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
curs.execute("SELECT Heading FROM Konference")
if curs.fetchone() is None:
    curs.execute(zap2, t1)
    curs.execute(zap2, t2)
    curs.execute(zap2, t3)
    curs.execute(zap2, t4)
    curs.execute(zap2, t5)
    curs.execute(zap2, t6)
    conn.commit()
else:
    print('Такая тема уже есть!')
conn.commit()
curs.execute("DELETE FROM Konference WHERE Organizers = 2 ")
conn.commit()
curs.execute("UPDATE Spravocnik SET invitation_data = '20.11.2022' WHERE invitation_data = '25.11.2022'")
conn.commit()
curs.close()
conn.close()