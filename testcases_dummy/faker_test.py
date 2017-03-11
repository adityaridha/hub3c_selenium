from faker import Factory
fake = Factory.create()

i=0
while i<5:
	business		= fake.company()
	first_name 		= fake.first_name()
	last_name		= fake.last_name()
	email 			= first_name+"."+last_name+"@gmail.com"
	password		= "ZXasqw12"

	print(email)
	print(business)

	i=i+1