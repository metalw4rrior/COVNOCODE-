import sqlite3 as sl
con = sl.connect('humans.db')
with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name='schtab'")
    for row in data:
        if row[0] == 0:
            with con:    
                con.execute("""
                    CREATE TABLE users (
                    name VARCHAR PRIMARY KEY,
                    inn INTEGER,
                    passport VARCHAR,
                    snils VARCHAR,
                    birthday DATE);""")
# sql = 'INSERT INTO users (name, inn, passport, snils, birthday) values(?,?,?,?,?)'
# data = [
#     ('Галкин Осип Авксентьевич', 114555579222, '2244 326666','464 562 222 66','1992-6-02'),
#     ('Гуляев Богдан Гордеевич', 223511363334, '4232 362343','962 933 322 88','2012-6-14'),
#     ('Лазарев Митрофан Денисович', 1611144449555, '7522 112623','565 232 782 08','2002-6-12'),
#     ('Белоусов Дмитрий Святославович', 5111541229123, '1363 122223','663 223 401 08','1968-11-2'),
#     ('Мартынов Альфред Парфеньевич', 534111229123, '1322 126223','632 962 402 08','1962-7-2'),
#     ('Авдеев Алексей Максимович', 344555119222, '2264 322266','434 562 622 66','1996-3-02'),
#     ('Николаев Нелли Леонидович', 223541163334, '4232 312643','922 933 622 88','2012-6-14'),
#     ('Стрелков Корнелий Семенович', 1612344449555, '7622 112223','555 632 782 08','2002-6-12'),
#     ('Ситников Донат Феликсович', 567541129123, '1338 122223','633 223 461 08','1976-11-2'),
#     ('Поляков Захар Данилович', 534561221123, '1382 122223','632 952 462 08','1962-7-2')]
# with con:
#     con.executemany(sql, data)
with con:
    data = con.execute("SELECT * FROM users")
    for row in data:
        print(row)