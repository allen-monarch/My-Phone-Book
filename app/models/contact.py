class Contact:
    def __init__(self,first_name,last_name,mobile="",phone="",email="",fax="",address="",company="",group_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.phone = phone
        self.email = email
        self.fax = fax
        self.address = address
        self.company = company
        self.group_name = group_name



if __name__ == "__main__":
    contact = Contact(
        first_name="Ali",
        last_name="Ahmadi",
        mobile="09121234567",
        phone="02112345678",
        email="ali@example.com",
        company="Kaverak",
        group_name="Friends"
    )

    print("Name:", contact.first_name)
    print("Last Name:", contact.last_name)
    print("Mobile:", contact.mobile)
    print("Company:", contact.company)
    print("Group:", contact.group_name)

# id          → SQLite ایجاد می‌کند
# created_at  → برنامه ایجاد می‌کند
# updated_at  → برنامه مدیریت می‌کند         
# موارد بالا رو نذاشتیم چون مدیریتش با دیتابیسه 