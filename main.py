import os
import sys
import math
import streamlit as st
import base64

if __name__ == "__main__" :

    st.title("Streamlit Webapp for TL parser")
    background = "image.jpg"
    background_ext = "jpg"
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{background_ext};base64,{base64.b64encode(open(background, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    file = st.file_uploader(" Upload the TimeLog file here")
    if st.button("Generate"):
        doc = str(file.read(),"utf-8")
        #st.write(doc)
        infolist=[]
        for i in doc:
            infolist.append(i)
            #st.write(i)
        #st.write(infolist)

        #if "time log" in infolist[0].lower():

        pair=[]
       # for i in infolist:
       #     relate = re.findall(r'(2[0-3]|[01][0-9]|[0-9]):([0-5][0-9]|[0-9])([aApP][mM])',i)
       #     pair.append(relate)
       #st.write(pair)

        for i in infolist:
            a=[]
            b=[]
            c=[]
            s=''
            s1=''
            for j in range(len(i)-9):
                if(i[j] == '1')and(i[j+1] == '0' or i[j+1] == '1' or i[j+1] == '2' ) and (i[j+2] == ':') and (i[j+8] == '-'):
                    s=i[j]+i[j+1]
                    a.append(s)
                    j=j+1

                elif(i[j] == '0' or i[j] == '1' or i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9') and (i[j+1] == ':') and (i[j+7]=='-') and(i[j-1]!='0' or i[j-1]!='1' or i[j-1]!='2'):
                    s=i[j]
                    a.append(s)

                if(i[j] == ':') and ((i[j+4]=='M') or (i[j+4]=='m')) and (i[j+6]=='-'):
                    s=i[j+1]+i[j+2]
                    s1=i[j+3]+i[j+4]
                    a.append(s)
                    a.append(s1)
                    j=j+4

                if(i[j] == '1')and(i[j+1] == '0' or i[j+1] == '1' or i[j+1] == '2' ) and (i[j+2] == ':') and (i[j+8] != '-'):
                    s=i[j]+i[j+1]
                    b.append(s)
                    j=j+1

                elif(i[j] == '0' or i[j] == '1' or i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9') and (i[j+1] == ':') and (i[j+7]!='-'):
                    s=i[j]
                    b.append(s)

                if(i[j] == ':') and ((i[j+4]=='M') or (i[j+4]=='m')) and (i[j+6]!='-'):
                    s=i[j+1]+i[j+2]
                    s1=i[j+3]+i[j+4]
                    b.append(s)
                    b.append(s1)
                    j=j+4


                if len(a)== 3 and len(b)==3:
                    c.append(a)
                    c.append(b)
                    pair.append(c)

                #print(a,b)




        for i in pair:
            for j in i:
                if len(j) == 4:
                    j.pop(1)
                if len(j) == 5:
                    j.pop(0)
                    j.pop(1)
                if len(j) == 6:
                    j.pop(0)
                    j.pop(1)
                    j.pop(3)
                #print(j)
            #print(i)




        add=[]
        #print(pair)
        for i in pair:
            time=0
            if not i:
                continue
            else:
                x=list(i);
                hour0=int(x[0][0])
                min0=int(x[0][1])
                hour1=int(x[1][0])
                min1=int(x[1][1])


                if x[0][2] == 'pm' or x[0][2] == 'pM' or x[0][2]=='Pm' or x[0][2]=='PM':
                    if x[1][2] == 'am' or x[1][2] == 'aM' or x[1][2]=='Am' or x[1][2]=='AM':
                        if(hour1!=12):
                            hour1=hour1+12
                        if(hour0==12):
                            hour0=hour0-12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60
                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60


                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)




                if x[0][2] == 'am' or x[0][2] == 'aM' or x[0][2]=='Am' or x[0][2]=='AM':
                    if x[1][2] == 'pm' or x[1][2] == 'pM' or x[1][2]=='Pm' or x[1][2]=='PM':
                        if(hour0==12):
                            hour1=hour1-12
                        if(hour1!=12):
                            hour1=hour1+12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60
                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60

                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)

                if x[0][2] == 'pm' or x[0][2] == 'pM' or x[0][2]=='Pm' or x[0][2]=='PM':
                    if x[1][2] == 'pm' or x[1][2] == 'pM' or x[1][2]=='Pm' or x[1][2]=='PM':
                        if(hour0==12 and hour1!=12):
                            hour1=hour1+12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60
                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60


                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)


                if x[0][2] == 'am' or x[0][2] == 'aM' or x[0][2]=='Am' or x[0][2]=='AM':
                    if x[1][2] == 'am' or x[1][2] == 'aM' or x[1][2]=='Am' or x[1][2]=='AM':

                        if(hour0==12 and hour1!=12):
                            hour1=hour1+12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60

                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60



                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)






                add.append(time)
        tt=0
        for i in add:
            tt=tt+i




        h = tt/60
        rh = math.floor(h)
        rt = math.ceil((h-rh)*60)
        d = math.floor(h/24)
        dh=(((tt/60)/24)-d)*24
        dm =   math.ceil((dh-math.floor(dh))*60)
        if(math.floor(dh)==0):
            st.write("{}hours {}minutes -- {} minutes -- {}days     {}minutes -- {}hours".format(rh,rt,tt,d,dm,round(h,6)))

        else:
            st.write("{}hours {}minutes -- {} minutes -- {}days {}hours {}minutes -- {}hours".format(rh,rt,tt,d,math.floor(dh),dm,round(h,6)))
