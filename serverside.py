import sqlite3 import random
# establishing connection
con = sqlite3.connect("railways.db") print("connection successful")
status confirmed
passenger_id 6924
                                      arrival_time 6:00
departure_ti available_sea me ts
19:00 20
                                          # creating cursor object
curs = con.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS train(train_no INTEGER PRIMARY KEY, source VARCHAR(30), dest VARCHAR(30), arrival_time VARCHAR(20), departure_time VARCHAR(30), available_seats INTEGER)")
curs.execute("CREATE TABLE IF NOT EXISTS passenger(passenger_id INTEGER PRIMARY KEY, name VARCHAR(20), gender VARCHAR(2), age INTEGER, train_no INTEGER, foreign key(train_no) references train(train_no))")
curs.execute("CREATE TABLE IF NOT EXISTS station(name VARCHAR(30), station_no INTEGER, train_no INTEGER, halt_time VARCHAR(10), primary key(station_no), foreign key(train_no) references train(train_no))")
curs.execute("CREATE TABLE IF NOT EXISTS ticket(ticket_no INTEGER, train_no INTEGER, status VARCHAR(20), passenger_id INTEGER,primary key(ticket_no),foreign key(train_no) references train(train_no), foreign key(passenger_id) references passenger(passenger_id))") print("welcome to railway reservation")
print("Menu 1-PASSENGER 2-ADMIN") op = int(input("enter choice:"))
try:
    if op==1:
        u_id = (input("enter id:"))
        pas = (input("enter password:"))
        if u_id=='user' and pas=='user':
            passenger_id = random.randint(1000,10000)
            name = input("enter passenger name:")
            gender = input("enter gender{M/F}:")
            age = input("enter age:")
            train_no = input("enter train number")
            curs.execute("insert into passenger (passenger_id,name,gender,age,train_no) VALUES(?,?,?,?,?)", (passenger_id, name, gender, age, train_no))
            con.commit()
            curs.execute("select * from passenger")
            print("passenger table")
            for row in curs.fetchall():
                print(row)
            #generating ticket
            ticket_no = random.randint(1000,10000)
            status = input("enter status of ticket:")
            curs.execute("insert into ticket (ticket_no,train_no,status,passenger_id) VALUES(?,?,?,?)", (ticket_no, train_no, status, passenger_id))
            con.commit()
            curs.execute("select * from ticket")
            print("ticket table")
            for row in curs.fetchall():
                print(row)
        elif op==2:
            u_id = (input("enter id:"))
            pas = (input("enter password:"))
            if u_id=='admin' and pas=='admin':
                # create train table
                train_no = input("enter train number:")
                source = input("enter train source:")
                dest = input("enter train destination:")
                arrival_time = input("enter train arrival time:")
                departure_time = input("enter train departure time:")
                available_seats = input("enter number of available seats:")
                curs.execute("INSERT INTO train(train_no,source,dest,arrival_time,departure_time,available_seats) VALUES(?,?,?,?,?,?)", (train_no, source, dest, arrival_time, departure_time, available_seats))
                con.commit() curs.execute("select * from train") print("train table")
                for row in curs.fetchall():
                    print(row)
                # station table
                name = input("enter station name:")
                station_no = input("enter station number:")
                halt_time = input("enter train halt duration:")
                curs.execute("insert into station (name,station_no,train_no,halt_time) VALUES(?,?,?,?)",(name,station_no,train_no,halt_time))
                con.commit()
                curs.execute("select * from ticket")
                print("ticket table")
                for row in curs.fetchall():
                    print(row)
except Exception as ex:
    print('error:', ex)
finally:
    con.close()
    print("data base connection has been terminated")
