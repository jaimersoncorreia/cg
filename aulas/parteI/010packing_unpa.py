'''
Recebendo um número arbitrário de argumentos: packing & unpacking

'''
from datetime import date

d = (2013,3,15)

print(date(d[0],d[1],d[2]))
print(date(*d))


def new_user(active = False, admin = False):
	print(active)
	print(admin)

config = {"active":False, "admin":True}
print("\n")
print(new_user(config.get('active'),config.get('admin')))
print("\n")
print(new_user(**config))
