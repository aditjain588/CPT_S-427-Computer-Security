pw1 = open("password1.txt","r")

Total_Entries=0
most_failed_login = 0
most_failed_login_user = 0
passwords_list = []
count=0

while True:
    count+=1
    line=pw1.readline()
    if not line:
        count-=1
        break
    x=line.split(",")
    if(int(x[6])>most_failed_login):
        most_failed_login = int(x[6])
        most_failed_login_user = x[0]
    passwords_list.append(x[4])

max_count=0
for i in range(0,len(passwords_list)):
    curr_count=0
    for j in range(0,len(passwords_list)):
        if(passwords_list[i]==passwords_list[j]):
            curr_count+=1
    if(curr_count>max_count):
        max_count=curr_count
        passw = passwords_list[i]
    
print("Total entries in password1 file is: ", count)
print("User with most failed login is ",most_failed_login_user, " with ", most_failed_login ," failed attempts")
print("Most common password is ", passw, " with count of: ", max_count)
