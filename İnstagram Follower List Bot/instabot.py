
import instaloader

guc = instaloader.Instaloader()


username = "" # your username gonna be came here / Kullanici isminizi buraya giriceksiniz
password = "" # your password gonna be came here / Sifrenizi isminizi buraya giriceksiniz
guc.login(username, password) 


profile = instaloader.Profile.from_username(guc.context, username)


follow_list = []
count = 0
for follomen in profile.get_followers():
    follow_list.append(followmen.username)
    file = open("takipciler.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
