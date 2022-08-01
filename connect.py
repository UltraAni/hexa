import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="ROOT",database="restaurant")




mycus=mydb.cursor()

billNumber=int(input("Enter the bill number: "))
price=int(input("Enter the price: "))

query="update bill set price={} where b_no = {}".format(price,billNumber)

mycus.execute(query)
mydb.commit()






