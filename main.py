import sys
import math
import re
import os
import base64
import streamlit as st

def amorpm(temp):
    log_0_h = int(temp[0][0])
    log_0_m = int(temp[0][1])
    log_1_h = int(temp[1][0])
    log_1_m = int(temp[1][1])
    m=0
    if(log_0_h == 12):
        if(log_1_h != 12):
            log_1_h = log_1_h + 12
    if(log_0_h < log_1_h):
        m = m + (log_1_h - log_0_h)*60
    else:
        if(log_0_h == log_1_h):
            m = 0
        else:
            m = m + (log_0_h - log_1_h)*60
                            
    if(log_1_m > log_0_m):
        m = m + (log_1_m - log_0_m)
    else:
        m = m - (log_0_m - log_1_m)
            
    return m

def ampm(temp):
    log_0_h = int(temp[0][0])
    log_0_m = int(temp[0][1])
    log_1_h = int(temp[1][0])
    log_1_m = int(temp[1][1])
    m=0
    if(log_0_h == 12):
        log_1_h = log_1_h - 12
    if(log_1_h != 12):
        log_1_h = log_1_h + 12
    if(log_0_h < log_1_h):
        m = m + (log_1_h - log_0_h)*60
    else:
        if(log_0_h == log_1_h):
            m = 0
        else:
            m = m + (log_0_h - log_1_h)*60
                            
    if(log_1_m > log_0_m):
        m = m + (log_1_m - log_0_m)
    else:
        m = m - (log_0_m - log_1_m)
            
    return m    
    
    
def pmam(temp):
    log_0_h = int(temp[0][0])
    log_0_m = int(temp[0][1])
    log_1_h = int(temp[1][0])
    log_1_m = int(temp[1][1])
    m=0
    if(log_0_h == 12):
        log_1_h = log_1_h - 12
    if(log_1_h != 12):
            log_1_h = log_1_h + 12
    if(log_0_h < log_1_h):
        m = m + (log_1_h - log_0_h)*60
    else:
        if(log_0_h == log_1_h):
            m = 0
        else:
            m = m + (log_0_h - log_1_h)*60
                            
    if(log_1_m > log_0_m):
        m = m + (log_1_m - log_0_m)
    else:
        m = m - (log_0_m - log_1_m)
            
    return m 

def expression(data):
    log_data = []
    d_ =  list(data.split("\n"))
    for variable in d_:
        log = re.findall(r'([01][0-9]|[0-9]):([0-5][0-9]|[0-9])([apAP][mM])',variable) 
        log_data.append(log)
    return log_data    
    
 
def output(m):
    raw_h = m/60
    floor_h = math.floor(raw_h)
    ceil_m = math.ceil((raw_h - floor_h)*60)
    raw_d = math.floor(raw_h/24)
    hour = math.floor((((m/60)/24)-raw_d)*24)
    mi = math.ceil((((((m/60)/24)-raw_d)*24)-hour)*60)
    if(hour == 0):
        st.write(f"{floor_h}hours {ceil_m}minutes -- {m} minutes -- {raw_d}days     {mi}minutes -- {raw_h}hours")
    else:
        st.write(f"{floor_h}hours {ceil_m}minutes -- {m} minutes -- {raw_d}days {hour}hours {mi}minutes -- {raw_h}hours")


 
def number_of_mins(data):
    tot = []
    for variable in data:
        m = 0
        if len(variable)!= 0:
            temp=list(variable)
            if variable[0][2] == 'am' or variable[0][2] == 'aM' or variable[0][2] == 'Am' or variable[0][2] == 'AM' :
                if variable[1][2] == 'am' or variable[1][2] == 'aM' or variable[1][2] == 'Am' or variable[1][2] == 'AM' :
                    m = amorpm(temp)
                    
            if variable[0][2] == 'pm' or variable[0][2] == 'pM' or variable[0][2] == 'Pm' or variable[0][2] == 'PM' :
                if variable[1][2] == 'pm' or variable[1][2] == 'pM' or variable[1][2] == 'Pm' or variable[1][2] == 'PM' :
                    m = amorpm(temp)            
                
            if variable[0][2] == 'am' or variable[0][2] == 'aM' or variable[0][2] == 'Am' or variable[0][2] == 'AM' :
                if variable[1][2] == 'pm' or variable[1][2] == 'pM' or variable[1][2] == 'Pm' or variable[1][2] == 'PM' :
                    m = ampm(temp)
                    
            if variable[0][2] == 'pm' or variable[0][2] == 'pM' or variable[0][2] == 'Pm' or variable[0][2] == 'PM' :
                if variable[1][2] == 'am' or variable[1][2] == 'aM' or variable[1][2] == 'Am' or variable[1][2] == 'AM' :
                    m = pmam(temp)           
            
            
            tot.append(m)
    tot_min = 0
    for variable in tot:
        tot_min = tot_min + variable
    return tot_min


        
        

if __name__ == "__main__" :

    st.title("TL parser")
    background = "background.jpg"
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
    file = st.file_uploader("", "txt")
    if st.button("Submit"):
        doc = str(file.read(),"utf-8")
        if not doc:
            st.write("Not Found")
        else:

            s = doc[0:8]

            x = re.search("Time Log", s)
            if x:
                formatted = expression(doc)
                number_of_mins = number_of_mins(formatted)
                output(number_of_mins)
            else:
                st.write(" Time Log not mentioned")
    
    
    
