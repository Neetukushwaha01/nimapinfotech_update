# from datetime import datetime
#
# contacts=[]
# while True:
#     print("Welcome to my Phonebook\nPress 1 to add new contact\nPress 2 to show contacts\nPress 3 to Delete Data \nPress 0 exits program.")
#     ch = input("Enter Your Choise:")
#     if ch=="0":
#         break
#     if ch=="1":
#         count=1
#         if contacts:
#             count =contacts[-1]['id']+1
#         print("New Contact")
#         name =input("Enter Name:")
#
#         mobile =input("Enter Number:")
#
#         date = datetime.today().strftime( "%y-%m-%d" )
#         data={'id':count,'name':name,'mobile':mobile,"Date":date}
#         contacts.append(data)
#     if ch=='2':
#         print("Your Contact list")
#         for c in contacts:
#             print(c)
#
#     if ch=='3':
#         print(contacts)
#         sid=int(input('Enter Id for  delete:'))
#         for c in contacts:
#             if sid==c.get('id'):
#                 c.clear()
#                 print("delete SuccessFully")
#
# print(contacts)
#
#
#

#
# 'username': "neetu12",
# 'password': 'neetu12',
# 'email': 'neetu12@gmail.com'


#auth=('admin','admin')

#
import requests
data_1 ={
    'project_name':"project_1",
    'client_name':"3",
    # 'email': 'admin@gmail.com'
}

data =requests.post("http://127.0.0.1:8000/project/api/projects/",auth=('neetu','neetu'),data=data_1)

print(data.text)








# myString = 'my name is neetu'
# print(len(myString))
# def mycount(v):
#     c = 0
#     for i in myString:
#         if i == v:
#             c = c + 1
#     return c
#
# print(mycount("e"))
















# a='this my string'
# v='y'
# cunt=0
# for i in a:
#     if i in [v.lower(),v.upper()] :
#         cunt+=1
# print(cunt)











