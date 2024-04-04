import re
import json
import time
import requests


def cooki():  
    try:
        q=requests.get("http://login.sreyas.ac.in:80/authcheck.aspx",allow_redirects=False)	
        cook=q.cookies.get_dict()
        q=requests.get("http://login.sreyas.ac.in:80/default.aspx",allow_redirects=False,cookies=cook)
        burp0_data = {"__VIEWSTATE": q.text[1759:2047], "__VIEWSTATEGENERATOR": "CA0B0334", "__EVENTVALIDATION": q.text[2227:2315], "txtId1": '', "txtPwd1": '', "txtId2": "21ve1a6680", "txtPwd2": "webcap", "imgBtn2.x": "40", "imgBtn2.y": "4"}
        q=requests.post("http://login.sreyas.ac.in:80/default.aspx",cookies=cook,data=burp0_data,allow_redirects=False)
        with open("keys.txt","w") as f:
            f.write(cook['ASP.NET_SessionId']+'\n'+q.cookies['frmAuth'])
    except:
        return "retry"

def getAttendance(roll):
    try:
        with open('keys.txt','r') as f:
            key=f.read().split('\n')
        url = "http://login.sreyas.ac.in:80/ajax/StudentAttendance,App_Web_studentattendance.aspx.a2a1b31c.ashx?_method=ShowAttendance&_session=no"
        cookiess = {"ASP.NET_SessionId":key[0], "frmAuth": key[1]}
        data = f"""rollNo={roll}
fromDate=
toDate=
excludeothersubjects=false"""
        q=requests.post(url, cookies=cookiess, data=data)
        t=q.content[:9]
        if(t==b'\r\n\r\n<!DOC'):
            cooki()
            return getAttendance(roll)
        else:
            return q.text
    except Exception as e:
        return "retry"

def home(roll):
    with open("name.json",'a+') as f:
        f.write("{}".format(roll))
    l=getAttendance(roll)
    if(l=='retry'):
        return "Invalid input"
    else:
        s=''
    for i in l:
          s+=i
    l=s
    l=l[1073::]
    x=re.findall('>[a-zA-Z0-9% ./-]+',l)
    l=[i[1:] for i in x]
    d=l[:10:]
    p=l[10::]
    del l
    p.insert(-4,'17')
    data=""
    for i in range(0,10,2):
        data+=f'{d[i]}  : {d[i+1]} \n'
            
    data+=f'Total  : {p[(5*11)+4]}'
    print(data)
    return data
