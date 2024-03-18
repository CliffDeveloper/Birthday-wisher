import smtplib

my_email = "cliffordmalonza66@gmail.com"
password = "mdbs rosa obge ihky"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="cliffordmalonza55@gmail.com", msg="Hello")
connection.close()


