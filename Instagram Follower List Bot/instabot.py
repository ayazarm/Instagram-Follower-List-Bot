import instaloader
from datetime import date


guc = instaloader.Instaloader()
today = date.today()

username = input("Enter your instagram Username : ")
password = input("Enter your instagram Password : ")


guc.login(username, password)


profile = instaloader.Profile.from_username(guc.context, username)


follow_list = []
count = 0
for follomen in profile.get_followers():
    follow_list.append(follomen.username)
    file = open("{}.txt".format(today), "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    count = count + 1
