user_number = int(input()) #Input number of people
user_Time = int(input()) #Input time for waiting from another

#Create list for collect data
Time_wait = []
Time_Nor = []
ww = []
total = []

#Determine time from number people (toward)
for i in range(0, user_number, 2):
    Time_wait.append(i)

#Determine time from number people (backward)
for i in range(user_number, 0, -user_Time):
    Time_Nor.append(i)

#Consider number of people
if user_number < 5000:
  for i in range(1, 5000):
    if len(total) == 0:
      # print((Time_Nor[i+1]+sum(total), Time_wait[i]))
      if (Time_Nor[i+1] - Time_wait[i] < user_Time):
        total.append(len(ww))
        ww.clear()
        pass
      else:
        ww.append(Time_wait[i])
    elif len(total) != 0:
      if (Time_Nor[i]+sum(total) - Time_wait[i-1] <= user_Time):
        ww.append(Time_wait[i])
        total.append(len(ww))
        ww.clear()
        break
      else:
        if (Time_Nor[i]+sum(total) > Time_wait[i]):
          ww.append(Time_wait[i])
          pass

else:
  for i in range(1, 5000):
    if len(total) == 0:
      if (Time_Nor[i+1] - Time_wait[i] < user_Time):
        total.append(len(ww))
        ww.clear()
        pass
      else:
        ww.append(Time_wait[i])
    elif len(total) != 0:
      if (Time_Nor[i]+sum(total) - Time_wait[i-1] <= user_Time):
        ww.append(Time_wait[i])
        total.append(len(ww))
        ww.clear()
        if (Time_Nor[i+1]+sum(total) < Time_wait[i-1]):
          break
        else:
          pass
      else:
        if (Time_Nor[i]+sum(total) > Time_wait[i]):
          ww.append(Time_wait[i])
          pass
  del total[len(total)-1]

# print(total)
# print(sum(total))
a = ((sum(total)+user_number)%60)
b = (sum(total)+user_number)//60
print(len(Time_Nor))
if  (sum(total)+len(Time_Nor)*2) > 60:
  print("%dh %dm" %(b, a))
else:
  print("%dm" %(a))
