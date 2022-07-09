import re
def main():
    message={'Status': 'Failure',"Date":{"Month":None}}
    n = input("Remaind: ")
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
    for j in range(i):
        if ("Декабря" == m[j]) | ("Декабре" == m[j])|("December" == m[j])|("декабря" == m[j]):
            message["Status"] = "Success"
            message["Date"]["Month"] = "December"
            if m[j-1].isdigit():
                message["Date"]["Day"] = m[j-1]
                del k[-1]
        elif "April" == m[j]:
            message["Status"] = "Success"
            message["Date"]["Month"] = "Апрель"
            message["Date"]["Day"] = m[j-1]
            del k[-1]
        elif (("года" == m[j] )| ("year" == m[j]))&(m[j-1].isdigit()):
                message["Status"] = "Success"
                message["Date"]["Year"]=m[j-1]
                del k[-1]
        elif("в" == m[j] ):
                if (j+1<i) or (":" in m[j+1]):
                    h=m[j+1].partition(":")
                    message["Status"] = "Success"
                    message["Date"]["Hour"] = h[0]
                    message["Date"]["Minute"] = h[2]
                    s=1
                    continue
        elif s==0:
            k.append(m[j])
        s=0
    for t in range(len(k)):
        n=n+k[t]+" "
    message["Text"]=n
    print(message)
main()