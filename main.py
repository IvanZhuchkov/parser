import time
class Parser():
    message={'Status': 'Failure',"Date":{"Day":None}, "Params":{"Repeat_always":None, "Day_of_week":None}}
    def __init__(self):
        message = self.message
        n=time.asctime()
        i=0
        m=[]
        while 1:
            n=n.partition(" ")
            m.append(n[0])
            i=i+1
            n=n[2]
            if n == "":
                break
        message["Date"]["Day"]=m[2]
        message["Date"]["Month"]= self.months(m[1])
        message["Day_of_week"]= self.week(m[0])
        message["Date"]["Year"]=m[4]
        message["Date"]["Hour"]=m[3][0]+m[3][1]
        message["Date"]["Minute"]=m[3][3]+m[3][4]
    def months(self,m):
        if ("december" == m) | ("декабря" == m )| ("декабрь"==m )|("Dec"==m):
            return "12"
        elif ("january" == m)|("январь" == m)|("января"==m)|("Jan"==m):
            return "1"
        elif ("february" == m)|("февраль" == m)|("февраля"==m)|("Feb"==m):
            return "2"
        elif ("march" == m)|("март" == m)|("март"==m)|("Mar"==m):
            return "3"
        elif ("april" == m)|("апрель" == m)|("апреля"==m)|("Apr"==m):
            return "4"
        elif ("may" == m)|("май" == m)|("мая"==m)|("May"==m):
            return "5"
        elif ("june" == m)|("июнь" == m)|("июня"==m)|("Jun"==m):
            return "6"
        elif ("jule" == m)|("июль" == m)|("июля"==m)|("Jul"==m):
            return "7"
        elif ("august" == m)|("август" == m)|("августа"==m)|("Aug"==m):
            return "8"
        elif ("september" == m)|("сентябрь" == m)|("сентября"==m)|("Sep"==m):
            return "9"
        elif ("october" == m)|("октябрь" == m)|("октября"==m)|("Oct"==m):
            return "10"
        elif ("november" == m)|("ноябрь" == m)|("ноября"==m)|("Nov"==m):
            return "11"
        return 0
    def week(self,m):
        if ("monday" == m)|("понедельник" == m)|("понедельникам"==m)|("Mon"==m):
            return "1"
        if ("tuesday" == m)|("вторник" == m)|("вторникам"==m)|("Tue"==m):
            return "2"
        if ("wednesday" == m)|("среда" == m)|("средам"==m)|("среду"==m)|("Wed"==m):
            return "3"
        if ("thursday" == m)|("четверг" == m)|("четвергам"==m)|("Thu"==m):
            return "4"
        if ("friday" == m)|("пятница" == m)|("пятница"==m)|("пятницу"==m)|("Fri"==m):
            return "5"
        if ("saturday" == m)|("суббота" == m)|("субботам"==m)|("субботу"==m)|("Sat"==m):
            return "6"
        if ("sunday" == m)|("воскресенье" == m)|("воскресеньям"==m)|("воскресенье"==m)|("Sun"==m):
            return "7"
        return 0
    def dict (self,m):
        message=self.message
        if (m =="день")|(m =="day"):
           message["Date"]["Day"]= str(int(message["Date"]["Day"])+1)
           return "day"
        elif (m =="час")|(m =="hour"):
            message["Date"]["Hour"]=str(int(message["Date"]["Hour"])+1) 
            return "hour"
        elif (m =="минуту")|(m =="minute"):
            message["Date"]["Minute"]= str(int(message["Date"]["Minute"])+1)
            return "minute"
        elif (m =="год")|(m =="year")|("году"==m):
            message["Date"]["Year"]= str(int(message["Date"]["Year"])+1)
            return "year"
        elif (m =="неделю")|(m =="week"):
            message["Date"]["Day"]= str(int(message["Date"]["Day"])+7)
            return "week"
        elif (m =="месяц")|(m =="month")|("месяце"==m):
            message["Date"]["Month"]= str(int(message["Date"]["Month"])+1)
            return "month"
        return 0
    def adict(self, m,e):
        message = self.message
        if (m == "минут")|("minutes"==m)|((m == "минуты")):
            message["Date"]["Minute"]= str(int(message["Date"]["Minute"])+int(e))
            return "minutes"
        if (m == "часов")|("hours"==m)|(m == "часа"):
            message["Date"]["Hour"]= str(int(message["Date"]["Hour"])+int(e))
            return "hours"
        if (m == "дня")|("days"==m)|(m == "дней"):
            message["Date"]["Day"]= str(int(message["Date"]["Day"])+int(e))
            return "days"
        if (m == "лет")|("years"==m)|(m == "года"):
            message["Date"]["Year"]= str(int(message["Date"]["Year"])+int(e))
            return "years"
        if (m == "недели")|("weeks"==m)|(m == "недель"):
            message["Date"]["Day"]= str(int(message["Date"]["Day"])+7*e)
            return "weeks"
        if (m == "месяца")|("months"==m)|(m == "месяцев"):
            message["Date"]["Month"]= str(int(message["Date"]["Month"])+e)
            return "months"
        if (m == "число")|("date"==m):
            if e>31:
                raise ValueError
            y= e - int(message["Date"]["Day"])>0
            if y>0:
                message["Date"]["Day"]= str(int(message["Date"]["Day"])+y)
            else:
                message["Date"]["Day"]= str(int(message["Date"]["Day"])+(7-abs(y)))
            return "each month"
        return 0
    def check(self):
        l=[1,3,5,7,8,10,12]
        sh=[4,6,9,11]
        message=self.message
        if int(message["Date"]["Minute"])>=60:
            message["Date"]["Hour"] = int(message["Date"]["Hour"])+int(message["Date"]["Minute"])//60
            message["Date"]["Minute"] = int(message["Date"]["Minute"])%60
        if int(message["Date"]["Hour"])>=24:
           message["Date"]["Day"]= str(int(message["Date"]["Day"])+int(message["Date"]["Hour"])//24)
           message["Date"]["Hour"]= str(int(message["Date"]["Hour"])%24)
        while True:
            if int(message["Date"]["Month"]) in l:
                if(int (message["Date"]["Day"])>31):
                    message["Date"]["Day"]=str(int (message["Date"]["Day"])-31)
                    message["Date"]["Month"]=str(int(message["Date"]["Month"])+1)
                else:
                    break
            elif int(message["Date"]["Month"]) in sh:
                    if(int (message["Date"]["Day"])>30):
                        message["Date"]["Month"]=str(int(message["Date"]["Month"])+1)
                        message["Date"]["Day"]=str(int (message["Date"]["Day"])-30)
                    else:
                        break
            elif int(message["Date"]["Month"]) == "2":
                    if(int (message["Date"]["Day"])>28):
                        message["Date"]["Month"]=str(int(message["Date"]["Month"])+1)
                        message["Date"]["Day"]=str(int (message["Date"]["Day"])-28)
                    else:
                        break
        if int(message["Date"]["Month"])>12:
            message["Date"]["Year"] = int(message["Date"]["Year"])+int(message["Date"]["Month"])//12
            message["Date"]["Month"] = int(message["Date"]["Month"])%12

    def opperate(self, n):
        message=self.message
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
        e=[None,None,None]
        for j in range(i):
            e[0] = self.months(m[j])
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
                    e[1]=self.week(m[j+1])
                    e[2]=self.dict(m[j+1])
                    if e[1]:
                        message["Params"]["Repeat_always"] = e[1]
                        message["Status"] = "Success"
                        message["Params"]["Day_of_week"] = e[1]
                        y = int(e[1]) - int (message["Day_of_week"]) 
                        if (y<=0):
                            message["Date"]["Day"]= str(int(message["Date"]["Day"])+(7-abs(y)))
                        else :
                            message["Date"]["Day"]= str(int(message["Date"]["Day"])+y)
                        s=1
                        continue
                    elif ("выходным"==m[j+1])|("weekend"==m[j+1]):
                        message["Params"]["Repeat_always"] = "Saturday and Sunday"
                        message["Status"] = "Success"
                        message["Params"]["Day_of_week"] = "Saturday and Sunday"
                        y = 6 - int (message["Day_of_week"]) 
                        if (y<=0):
                            message["Date"]["Day"]= str(int(message["Date"]["Day"])+(7-abs(y)))
                        else :
                            message["Date"]["Day"]= str(int(message["Date"]["Day"])+y)
                        s=1
                        continue
                    elif e[2]:
                            message["Status"]= "Success"
                            message["Params"]["Repeat_always"]="Every"+e[2]
                            s=1
                            continue
                    elif m[j+1].isdigit():
                        e[2]=self.adict(m[j+2], m[j+1])
                        if e[2]:
                            message["Status"] = "Success"
                            message["Params"]["Repeat_always"] = "Every " + m[j+1]+" "+e[2]
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
                        if "." in m[j+1]:
                            h=m[j+1].partition(".")
                            message["Status"] = "Success"
                            message["Date"]["Hour"] = h[0]
                            message["Date"]["Minute"] = h[2]
                            s=1
                            continue
                        e[1]=self.week(m[j+1])
                        if e[1]:
                            message["Status"] = "Success"
                            message["Params"]["Day_of_week"] = e[1]
                            y = int(e[1]) - int (message["Day_of_week"]) 
                            if (y<=0):
                                message["Date"]["Day"]= str(int(message["Date"]["Day"])+(7-abs(y)))
                            else :
                                message["Date"]["Day"]= str(int(message["Date"]["Day"])+y)
                            if j+2<i:
                                if ":" in m[j+2]:
                                    h=m[j+2].partition(":")
                                    message["Status"] = "Success"
                                    message["Date"]["Hour"] = h[0]
                                    message["Date"]["Minute"] = h[2]
                                    s=2
                                    continue
                            s=1
                            continue
                        if ("следующем"==m[j+1])|("следующий"==m[j+1])|("следующую"==m[j+1])|("следующие"==m[j+1])|("next"==m[j])|("следующей"==m[j+1])|("следующее"==m[j+1]):
                            if j+2<i :
                                e[1]=self.week(m[j+2])
                                e[2]=self.dict(m[j+2])
                                if e[1]:
                                    message["Params"]["Wait_until"] = e[1]
                                    message["Status"] = "Success"
                                    message["Params"]["Day_of_week"] = e[1]
                                    y = int(e[1]) - int (message["Day_of_week"]) 
                                    if (y<=0):
                                        message["Date"]["Day"]= str(int(message["Date"]["Day"])+(7-abs(y)))
                                    else :
                                        message["Date"]["Day"]= str(int(message["Date"]["Day"])+y)
                                    s=2
                                    continue
                                elif e[2]:
                                    message["Status"] = "Success"
                                    message["Params"]["Wait_until"] = "Next " + e[2]
                                    s=2
                                    continue
                                elif m[j+2].isdigit():
                                    e[2]=self.adict(m[j+3])
                                    if e[2]:
                                        message["Status"] = "Success"
                                        message["Params"]["Wait_until"] = "Next " + m[j+2]+" "+e[2]
                                        s=3
                                        continue
                        if m[j+1].isdigit():
                            if j+2 == i:
                                message["Status"] = "Success"
                                message["Date"]["Hour"] =m[j+1]
                                s=1
                                continue
                            if j+2<i:
                                if ("часов"==m[j+2])|("pm"==m[j+2])|("am"==m[j+2]):
                                    message["Status"] = "Success"
                                    message["Date"]["Hour"] =m[j+1]
                                    s=2
                                    continue
            elif ("на"==m[j])|("on"==m[j]):
                if j+1 < i:
                    if ("выходных"==m[j+1])|("weekend"==m[j+1]):
                        message["Status"] = "Success"
                        message["Params"]["Day_of_week"] = "Saturday and Sunday"
                        s=1
                        continue
                    if ("неделе"==m[j+1])|("week"==m[j]):
                        message["Status"] = "Success"
                        message["Params"]["Day_of_week"] = "Monday, Tuesday, Wednesday, Thursday, Friday"
                        s=1
                        continue
            elif ("через"==m[j])|("in"==m[j]):
                if j+1<i :
                    e[2]=self.dict(m[j+1])
                    if e[2]:
                        message["Status"] = "Success"
                        message["Params"]["Wait_until"] = "Next "+e[2]
                        s=1
                        continue
                    elif m[j+1].isdigit():
                        e[2]=self.adict(m[j+2], m[j+1])
                        if e[2]:
                            message["Status"] = "Success"
                            message["Params"]["Wait_until"] =m[j+1]+" " + e[2]
                            s=2
                            continue
            if ("утром"==m[j])|("morning"==m[j]):
                message["Status"] = "Success"
                message["Date"]["Hour"] ="9"
                message["Date"]["Minute"] ="00"
                continue
            if ("днём"==m[j])|("daytime"==m[j]):
                message["Status"] = "Success"
                message["Date"]["Hour"] ="13"
                message["Date"]["Minute"] ="00"
                continue
            if ("вечером"==m[j])|("evening"==m[j]):
                message["Status"] = "Success"
                message["Date"]["Hour"] ="18"
                message["Date"]["Minute"] ="00"
                continue
            if ("ночью"==m[j])|("night"==m[j]):
                message["Status"] = "Success"
                message["Date"]["Hour"] ="22"
                message["Date"]["Minute"] ="00"
                continue
            if ("завтра"==m[j])|("tommorow"==m[j]):
                message["Status"] = "Success"
                message["Date"]["Day"]=str(int(message["Date"]["Day"])+1)
                message["Params"]["Wait_until"] ="Next day"
                continue
            if ("послезавтра"==m[j])|("aflertommorow"==m[j]):
                message["Status"] = "Success"
                message["Date"]["Day"]=str(int(message["Date"]["Day"])+2)
                message["Params"]["Wait_until"] ="2 days"
                continue
            if ("числа"==m[j])|("pm"==m[j])|("am"==m[j]):
                if j-1>-1:
                    if m[j-1].isdigit():
                        message["Status"] = "Success"
                        message["Date"]["Day"] =m[j-1]
                        del k[-1]
                        continue
            if m[j].count(".")==2:
                h=m[j].partition(".")
                o=h[2].partition(".")
                message["Status"] = "Success"
                message["Date"]["Day"] =h[0]
                message["Date"]["Month"]=o[0]
                message["Date"]["Year"]=o[2]
                continue
            
            if s==0:
                k.append(m[j])
            else:
                s=s-1
        for t in k:
            n=n+t+" "
        n=n.capitalize()
        message["Text"]=n
        del message["Day_of_week"]
        if message["Params"]["Repeat_always"] != None:
                if message["Params"]["Repeat_always"] =="1":
                    message["Params"]["Repeat_always"] ="Monday"
                    message["Params"]["Day_of_week"] ="Monday"
                elif message["Params"]["Repeat_always"] =="2":
                    message["Params"]["Repeat_always"] ="Tuesday"
                    message["Params"]["Day_of_week"] ="Tuesday"
                if message["Params"]["Repeat_always"] =="3":
                    message["Params"]["Repeat_always"] ="Wednesday"
                    message["Params"]["Day_of_week"] ="Wednesday"
                if message["Params"]["Repeat_always"] =="4":
                    message["Params"]["Repeat_always"] ="Thursday"
                    message["Params"]["Day_of_week"] ="Thursday"
                if message["Params"]["Repeat_always"] =="5":
                    message["Params"]["Repeat_always"] ="Friday"
                    message["Params"]["Day_of_week"] ="Friday"
                if message["Params"]["Repeat_always"] =="6":
                    message["Params"]["Repeat_always"] ="Saturday"
                    message["Params"]["Day_of_week"] ="Saturday"
                if message["Params"]["Repeat_always"] =="7":
                    message["Params"]["Repeat_always"] ="Sunday"
                    message["Params"]["Day_of_week"] ="Sunday"
        if message["Params"]["Repeat_always"] != None:
                if message["Params"]["Day_of_week"] =="1":
                    message["Params"]["Day_of_week"] ="Monday"
                elif message["Params"]["Day_of_week"] =="2":
                    message["Params"]["Day_of_week"] ="Tuesday"
                if message["Params"]["Day_of_week"] =="3":
                    message["Params"]["Day_of_week"] ="Wednesday"
                if message["Params"]["Day_of_week"] =="4":
                    message["Params"]["Day_of_week"] ="Thursday"
                if message["Params"]["Day_of_week"] =="5":
                    message["Params"]["Day_of_week"] ="Friday"
                if message["Params"]["Day_of_week"] =="6":
                    message["Params"]["Day_of_week"] ="Saturday"
                if message["Params"]["Day_of_week"] =="7":
                    message["Params"]["Day_of_week"] ="Sunday"
        self.check()
        print(message)
def main():
    newp = Parser()
    n=input("Remaind: ")
    newp.opperate(n)
if __name__=="__main__":
    main()