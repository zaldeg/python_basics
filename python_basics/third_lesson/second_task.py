def data(
    name="-",
    surname="-",
    year_of_birthday="-",
    city="-",
    email="-",
    telephon_number="-",
):
    # ugly print
    print(name, surname, year_of_birthday, city, email, telephon_number)

    # pretty print
    # print(
    #     f"Name and surname: {name} {surname}\nyear_of_birthday: {year_of_birthday}\n"
    #     f"City: {city}\nEmail: {email}\nTelephone number: {telephon_number}"
    # )


# a = ("A", "B", 50, "New York", "somemail@google.com", "+7846435633")
# data(*a)

n = "A"
s = "B"
y = 50
ci = "New York"
e = "somemail@google.com"
t = "+7846435633"
# data(email=e, name=n, surname=s, year_of_birthday=y, city=ci, telephon_number=t)
data(email=e, name=n, surname=s, city=ci, telephon_number=t)

