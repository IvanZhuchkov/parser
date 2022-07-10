def months(m):
    if ("december" == m) | ("декабря" == m )| ("декабрь"==m ):
        return "12"
    elif ("january" == m)|("январь" == m)|("января"==m):
        return "1"
    elif ("february" == m)|("февраль" == m)|("февраля"==m):
        return "2"
    elif ("march" == m)|("март" == m)|("март"==m):
        return "3"
    elif ("april" == m)|("апрель" == m)|("апреля"==m):
        return "4"
    elif ("may" == m)|("май" == m)|("мая"==m):
        return "5"
    elif ("june" == m)|("июнь" == m)|("июня"==m):
        return "6"
    elif ("jule" == m)|("июль" == m)|("июля"==m):
        return "7"
    elif ("august" == m)|("август" == m)|("августа"==m):
        return "8"
    elif ("september" == m)|("сентябрь" == m)|("сентября"==m):
        return "9"
    elif ("october" == m)|("октябрь" == m)|("октября"==m):
        return "10"
    elif ("november" == m)|("ноябрь" == m)|("ноября"==m):
        return "11"
    return 0
def week(m):
    if ("monday" == m)|("понедельник" == m)|("понедельникам"==m):
        return "Monday"
    if ("tuesday" == m)|("вторник" == m)|("вторникам"==m):
        return "Tuesday"
    if ("wednesday" == m)|("среда" == m)|("средам"==m)|("среду"==m):
        return "Wednesday"
    if ("thursday" == m)|("четверг" == m)|("четвергам"==m):
        return "Thursday"
    if ("friday" == m)|("пятница" == m)|("пятница"==m)|("пятницу"==m):
        return "Friday"
    if ("saturday" == m)|("суббота" == m)|("субботам"==m)|("субботу"==m):
        return "Saturday"
    if ("sunday" == m)|("воскресенье" == m)|("воскресеньям"==m)|("воскресенье"==m):
        return "Sunday"
    return 0

def main():
    dh="12"
    dm="00"
    message={'Status': 'Failure',"Date":{"Day":None}, "Params":{"Repeat_always":None}}
    n = input("Remaind: ")
    n=n.lower()
    i=0
    m=[]
    while 1:
        n=n.partition(" ")
        m.append(n[0])
        i=i+1
        n=n[2]
        if n == "":
            break
    n=""
    k=[]
    s=0
    e=[None]
    for j in range(i):
        e[0] = months(m[j])
        if e[0] :
            message["Status"] = "Success"
            message["Date"]["Month"] = e[0]
            if j-1>-1:
                if m[j-1].isdigit():
                    message["Date"]["Day"] = m[j-1]
                    del k[-1]
                    continue
        elif (("года" == m[j] )| ("year" == m[j]))&(m[j-1].isdigit()):
            if j-1>-1:
                message["Status"] = "Success"
                message["Date"]["Year"]=m[j-1]
                del k[-1]
                continue
        elif ("каждый"==m[j])|("every"==m[j])|("по"==m[j])|("каждую"==m[j])|("каждые"==m[j])|("каждое"==m[j]):
            if j+1<i :
                e[1]=week(m[j+1])
                if e[1]:
                    message["Params"]["Repeat_always"] = e[1]
                    message["Status"] = "Success"
                    message["Params"]["Day_of_week"] = e[1]
                    message["Date"]["Hour"] = dh
                    message["Date"]["Minute"] = dm
                    s=1
                    continue
                elif (m[j+1] =="день")|(m[j+1] =="day"):
                    message["Status"] = "Success"
                    message["Params"]["Repeat_always"] = "Every day"
                    message["Date"]["Hour"] = dh
                    message["Date"]["Minute"] = dm
                    s=1
                    continue
                elif (m[j+1] =="час")|(m[j+1] =="hour"):
                    message["Status"] = "Success"
                    message["Params"]["Repeat_always"] = "Every hour"
                    s=1
                    continue
                elif (m[j+1] =="минуту")|(m[j+1] =="minute"):
                    message["Status"] = "Success"
                    message["Params"]["Repeat_always"] = "Every minute"
                    s=1
                    continue
                elif (m[j+1] =="год")|(m[j+1] =="year"):
                    message["Status"] = "Success"
                    message["Params"]["Repeat_always"] = "Every year"
                    s=1
                    continue
                elif (m[j+1] =="неделю")|(m[j+1] =="week"):
                    message["Status"] = "Success"
                    message["Params"]["Repeat_always"] = "Every week"
                    s=1
                    continue
                elif (m[j+1] =="месяц")|(m[j+1] =="month"):
                    message["Status"] = "Success"
                    message["Params"]["Repeat_always"] = "Every month"
                    s=1
                    continue
                elif m[j+1].isdigit():
                    if (m[j+2] == "минут")|("minutes"==m[j+2])|((m[j+2] == "минуты")):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" minutes"
                        s=2
                        continue
                    if (m[j+2] == "часов")|("hours"==m[j+2])|(m[j+2] == "часа"):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" hours"
                        s=2
                        continue
                    if (m[j+2] == "дня")|("days"==m[j+2])|(m[j+2] == "дней"):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" days"
                        s=2
                        continue
                    if (m[j+2] == "лет")|("years"==m[j+2])|(m[j+2] == "года"):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" years"
                        s=2
                        continue
                    if (m[j+2] == "недели")|("weeks"==m[j+2])|(m[j+2] == "недель"):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" weeks"
                        s=2
                        continue
                    if (m[j+2] == "месяца")|("months"==m[j+2])|(m[j+2] == "месяцев"):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" months"
                        s=2
                        continue
                    if (m[j+2] == "число")|("date"==m[j+2]):
                        message["Status"] = "Success"
                        message["Params"]["Repeat_always"] = "Every " + m[j+1]+" each month"
                        s=2
                        continue
        elif("в" == m[j] ):
                if (j+1<i):
                    if ":" in m[j+1]:
                        h=m[j+1].partition(":")
                        message["Status"] = "Success"
                        message["Date"]["Hour"] = h[0]
                        message["Date"]["Minute"] = h[2]
                        s=1
                        continue
                    e[1]=week(m[j+1])
                    if e[1]:
                        message["Status"] = "Success"
                        message["Params"]["Day_of_week"] = e[1]
                        message["Date"]["Hour"] = dh
                        message["Date"]["Minute"] = dm
                        s=1
                        continue
        if s==0:
            k.append(m[j])
        else:
            s=s-1
    for t in k:
        n=n+t+" "
    n=n.capitalize()
    message["Text"]=n
    print(message)
main()