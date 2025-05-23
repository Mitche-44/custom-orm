from config import conn, cursor


class Customer:
    def __init__(self, first_name, last_name, email, phone, gender, password, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.password = password
        self.id = id

    # string representation
    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT UNIQUE,
            gender TEXT,
            password TEXT
            );
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customers;"

        cursor.execute(sql)
        conn.commit()

    # save data inside database

    def save(self):
        sql = """
            INSERT INTO customers (
            first_name,
            last_name,
            email,
            phone,
            gender,
            password
            ) VALUES (?, ?, ?, ?, ?, ?);
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.email,
                self.phone,
                self.gender,
                self.password,
            ),
        )
        conn.commit()

        last_row_id = cursor.lastrowid
        print(last_row_id)

        self.id = last_row_id

    @classmethod
    def create(cls, first_name, last_name, email, phone, gender, password):
        # create a customer instance
        customer = cls(first_name, last_name, email, phone, gender, password)

        customer.save()

        return customer

    def update(self):
        sql = """
            UPDATE customers SET first_name = ?, last_name= ?,  email = ?,
            phone = ?,
            gender = ?,
            password = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.email,
                self.phone,
                self.gender,
                self.password,
                self.id,
            ),
        )
        conn.commit()

        print(f"the instance id is : {self.id}")

    def delete(self):
        sql = "DELETE FROM customers WHERE id = ?;"

        cursor.execute(sql, (self.id,))
        conn.commit()

    # fetch an instance from the db
    # fetch by id
    # fetch all records
    # fetch by first_name
    # fetch by last_name
    # create relationships between objects
