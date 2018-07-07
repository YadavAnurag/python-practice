# import datetime

# default_name = ['Anurag', 'Yadav', 'Sarvesh', 'Shukla', 'Shivam','Amit', 'Tiwari', 'sahu']
# default_amounts = [200, 4342, 34, 235,6,73,2354, 2342423]

# unformatted_msg = 'Hi {name}! Thank you for the purchase on {date}. The purchase total was {total}'

# def make_msg(names, amounts):
#     messages = []
#     if len(names)==len(amounts):
#         i=0
#         for name in names:
#             new_amount = "%.2f" %(amounts[i])
#             today = datetime.date.today()
#             new_msg = unformatted_msg.format(name=name.capitalize(), date=today, total =new_amount )
#             print(new_msg)
#             i+=1
# make_msg(default_name, default_amounts)




#                             # Working with classes

# class anu():
#     name='Shivam Shukla'
#     likes= 'Abhay Kumar Jaiswal'
#     def get_likes(self):
#         return self.likes

# obj = anu()
# obj.name
# obj.get_likes()
    

# class Animal():
#     noise= 'Grunt'
#     size= 'Large'
#     color= 'Brown'
#     hair= 'Covers body'
#     @property
#     def get_noise(self):
#         return self.noise
#     def get_color(self):
#         return self.color

# class Dog(Animal):
#     name= 'Shivam Shukla'

# dog = Dog()

# print(dog.name, dog.get_noise);


# email_address = 'anuragyadav13481@gmail.com'
# from_list = ['anu@gmail.com', 'anufz90@gmail.com', 'anufz00@gmail.com']
# to_list = ['shivam@gmail.com','rat@gmail.com', 'sahu@gmail.com']

# def send_email(email=email_address, from_list=from_list, to_list= to_list):
#     for l in from_list:
#         print(l)


# class MessageUser():
#     user_deatails = []
#     message = []
#     base_massage = """Hi {name}!









num = int(input())

my_list = []
def my_fun(my_list):
    my_list = my_list.split(" ")
    work = my_list.pop(0)
    def listfun(work):
        switcher = {
            "insert":my_list.append(int(my_list[1]), int(my_list[2])),
            "print": print(my_list),
            "remove": my_list.remove(int(my_list[1])),
            "append": my_list.append(int(my_list[1])),
            "sort": my_list.sort(),
            "pop": my_list.pop(),
            "reverse": my_list.sort(reverse = True)
        }    
        return switcher.get(work, "No match found")
    return my_list

while(num):
    input_list = input().split(" ")
     







