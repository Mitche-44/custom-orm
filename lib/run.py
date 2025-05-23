from customer import Customer

# drop table if it exists
Customer.drop_table()

# create customers table
Customer.create_table()


# create instances of customers
customer1 = Customer.create(
    "Jeff", "Bezos", "jeff@gmail.com", "0776543926", "Male", "2345678"
)
customer2 = Customer.create(
    "John", "Doe", "jdoe@gmail.com", "0712345678", "Male", "12345"
)
customer3 = Customer.create(
    "Jane", "Doe", "janedoe@gmail.com", "0712342352", "Female", "12345"
)
customer4 = Customer.create(
    "Alex", "Doe", "alex@gmail.com", "0743517468", "Male", "12345"
)
customer5 = Customer.create(
    "Bob", "Marley", "bob@gmail.com", "0723417654", "Male", "12345"
)


# update Jeff's phone number
customer1.phone = "070600000"
customer1.first_name = "EricksDad"

customer1.update()

# deleting Alex
customer4.delete()
