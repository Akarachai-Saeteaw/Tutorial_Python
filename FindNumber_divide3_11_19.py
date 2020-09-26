#Factor of number for divide 3, 11, 19
aa = []
collect = [1]
def is_ugly(num):
    global collect
    global aa
    for i in range(2, 10000000):
      if len(collect) != num:
        if (i % 3 == 0) or (i % 11 == 0)or (i % 19 == 0):
          aa.append(i) 
          while len(aa) > 0:
            if aa[len(aa)-1] == 1:
              collect.append(i)
              aa.clear()
            else:
              if ((str(aa[len(aa)-1] // 19)).isdigit()) and (aa[len(aa)-1]//19 != 0) and ((aa[len(aa)-1]%19 == 0)):
                aa.append(aa[len(aa)-1]//19)  
                # print(aa[len(aa)-1]//3)
              elif ((str(aa[len(aa)-1] // 11)).isdigit()) and (aa[len(aa)-1]//11 != 0)and ((aa[len(aa)-1]%11 == 0)):
                aa.append(aa[len(aa)-1]//11) 
                # print(aa[len(aa)-1]//6)
              elif ((str(aa[len(aa)-1] // 3)).isdigit()) and (aa[len(aa)-1]//3 != 0)and ((aa[len(aa)-1]%3 == 0)):
                aa.append(aa[len(aa)-1]//3)  
                # print(aa[len(aa)-1]//3)
              else:
                aa.clear()
                pass
        else:
          pass
      else:
        break  
    return      
    # return num == 1
