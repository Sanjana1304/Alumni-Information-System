#connecting with MySQL_database to store details.
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="***",database="Alumni_Information_System")
#creating cursor object
cursor=mycon.cursor()

#using GUI programming
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("1278x868")

#Dandelion Image in login window.
photo_pb1=PhotoImage(master=window,file="Dandelions.png")
label_pb1=Label(window, image=photo_pb1)
label_pb1.pack()

window.title("Sign-in | SignUp")

label_head=Label(window,text="Alumni Information System",fg='black',bg='white',font=("arial",20,"bold")).place(x=465,y=10)

usid_label=Label(window,text="USER ID : ",bg="white",fg='black',font=("arial",12,"bold"))
usid_label.place(x=160,y=340)

usid_entry=Entry(window,width=25,font=(12))
usid_entry.place(x=370,y=342)

pwd_label=Label(window,text="PASSWORD : ",bg="white",fg='black',font=("arial",12,"bold"))
pwd_label.place(x=160,y=440)

pwd_entry=Entry(window,width=25, font=(12))
pwd_entry.place(x=370,y=442) 

small_label=Label(window,text="Dont have an account? ",fg='blue',relief=RIDGE,font=("arial",7,"bold"))
small_label.place(x=380,y=630)

#function to logout from their account
def logout():
    global window1
    window1.withdraw()
    window.deiconify()
     
#function to search for an alumni after logging in
def search_alumni(a):
    query="select USER_ID,Name,E_mail,Mobile_no,Joined_SV,left_SV,DOB,Marital_status,Proffession,Address_line1,Address_line2,Address_line3,Life_After_SV,Memories_from_SV from alumni_table where USER_ID=%s"
    val=(a,)
    cursor.execute(query,val)
    res1=cursor.fetchall()
    if res1==[]:
        messagebox.showinfo("Oh No!","Record Not Found !\n Pls enter valid User Id")
    else:

        window2=Tk()
        window2.geometry("700x700")
        window2.config(bg="pale turquoise")
        window2.title("Details")
        label_2=Label(window2,text="The details of the user are : ",bg="pale turquoise",fg='black',font=("arial",22))
        label_2.place(x=145,y=10)
        detail_list=Listbox(window2,height=15,width=30, font=("Constantia",17))
        detail_list.place(x=300,y=100)

        label_usid=Label(window2, text="User ID:",bg="pale turquoise",fg="black",font=("Constantia",15))   
        label_usid.place(x=80,y=100)

        label_name=Label(window2, text="Name:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_name.place(x=80,y=130)

        label_email=Label(window2, text="Email:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_email.place(x=80,y=160)

        label_mno=Label(window2, text="Mobile no.:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_mno.place(x=80,y=190)

        label_JSV=Label(window2, text="Joined SV in the year:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_JSV.place(x=80,y=220)

        label_LSV=Label(window2, text="Left SV in the year:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_LSV.place(x=80,y=250)

        label_DOB=Label(window2, text="Date Of Birth:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_DOB.place(x=80,y=280)

        label_MS=Label(window2, text="Marital status:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_MS.place(x=80,y=310)

        label_Proff=Label(window2, text="Proffession",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_Proff.place(x=80,y=340)

        label_address=Label(window2, text="Address:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_address.place(x=80,y=370)


        label_LASV=Label(window2, text="Life after SV:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_LASV.place(x=80,y=455)

        label_FMSV=Label(window2, text="Fondest memory in SV:",bg="pale turquoise",fg="black",font=("Constantia",15))
        label_FMSV.place(x=80,y=485)

        
        for i in range(len(res1[0])):
            detail_list.insert(i,res1[0][i])

#function to add data in SQL(by submit button)
def confirm_register(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    query="insert into alumni_table (USER_ID,Name,E_mail,Mobile_no,Joined_SV,left_SV,DOB,Marital_status,Proffession,Address_line1,Address_line2,Address_line3,Life_After_SV,Memories_from_SV,Password,USER_TYPE) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
    cursor.execute(query,val)
    mycon.commit()

    window_reg=Tk()
    window_reg.geometry("770x700")
    window_reg.title("Thank You!")

    photo_thumb=PhotoImage(master=window_reg,file="thumb.png")
    label_thumb=Label(window_reg,image=photo_thumb)
    label_thumb.place(x=200,y=60)

    label_suc=Label(window_reg,text="Successfully Registered !",fg='red',font=("Georgia",20,"bold"))
    label_suc.place(x=140,y=300)

    label_acc=Label(window_reg,text="Your account has been created\nYou can use the following USER ID to login",fg='green',font=("Georgia",18))
    label_acc.place(x=120,y=345)

    label_us=Label(window_reg,text="USER ID : ",fg='dark blue',font=("Georgia",18,"bold"))
    label_usid=Label(window_reg,text=a,fg='dark blue',font=("Georgia",18,"bold"))
    label_us.place(x=170,y=420)
    label_usid.place(x=310,y=420)

    mainloop()
    
def storing_Rdetails():
    name=entry_1.get()
    email=entry_2.get()
    mno=entry_3.get()
    From=entry_5.get()
    to=entry_6.get()
    dob=entry_7.get()
    psswrd=entry_p.get()
    ms=entry_m.get()
    proff=entry_9.get()
    al1=entry_11.get()
    al2=entry_12.get()
    al3=entry_13.get()
    after=entry_14.get()
    memo=entry_15.get()
    i_am=c3.get()
    us_id=name[0:3]+dob[-2:]+"@"+i_am.lower()+".com"
    confirm_register(us_id,name,email,mno,From,to,dob,ms,proff,al1,al2,al3,after,memo,psswrd,i_am)

#function to register one's database
def Registration_form():
    window=Tk()
    window.geometry("3000x1000")
    window.title("Registration form")
    window.config(bg="pale turquoise")
    global entry_1
    global entry_2
    global entry_3
    global entry_p
    global entry_5
    global entry_6
    global entry_7
    global entry_9
    global entry_11
    global entry_12
    global entry_13
    global entry_14
    global entry_15
    global droplist3
    global sub_button
    global c3
    global entry_m

   
    label_0=Label(window,text="REGISTRATION FORM",fg="white",bg="black",relief="solid",font=("Copperplate Gothic",20,"bold"))
    label_0.place(x=600,y=35)
   
    label_1=Label(window,text="Full Name*",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_1.place(x=120,y=120)
    fname=StringVar()
    entry_1=Entry(window, font=("Constantia",20),textvar=fname)
    entry_1.place(x=310,y=120)
   

    label_2=Label(window, text="Email*",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_2.place(x=120,y=220)
    email=StringVar()
    entry_2=Entry(window, font=("Constantia",20),textvar=email)
    entry_2.place(x=310,y=220)

    label_3=Label(window, text="Mobile no.*",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_3.place(x=120,y=320)
    mn=StringVar()
    entry_3=Entry(window, font=("Constantia",20),textvar=mn)
    entry_3.place(x=310,y=320)

    label_p=Label(window,text="Set Password*",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_p.place(x=850,y=120)
    sp=StringVar()
    entry_p=Entry(window, font=("Constantia",20),textvar=sp)
    entry_p.place(x=1050,y=120)

    label_4=Label(window, text="Years spent in SV",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_4.place(x=120,y=420)
   

    label_5=Label(window, text="Joined SV in the year",fg="black",bg="pale turquoise",font=("Constantia",16))
    label_5.place(x=120,y=470)
    From=IntVar()
    entry_5=Entry(window, font=("Constantia",16),textvar=From)
    entry_5.place(x=315,y=470)

    label_6=Label(window, text="Left SV in the year",fg="black",bg="pale turquoise",font=("Constantia",16))
    label_6.place(x=120,y=520)
    to=IntVar()
    entry_6=Entry(window, font=("Constantia",16),textvar=to)
    entry_6.place(x=315,y=520)


    label_7=Label(window, text="Date Of Birth*",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_7.place(x=120,y=575)
    dobirth=IntVar()
    entry_7=Entry(window,font=("Constantia",20),textvar=dobirth)
    entry_7.place(x=310,y=575)

 
    label_8=Label(window, text="Marital Status",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_8.place(x=120,y=675)
    mar=StringVar()
    entry_m=Entry(window,font=("Constantia",20),textvar=mar)
    entry_m.place(x=310,y=675)

    label_9=Label(window,text="Profession*",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_9.place(x=850,y=220)
    prof=StringVar()
    entry_9=Entry(window,font=("Constantia",20),textvar=prof)
    entry_9.place(x=1050,y=220)

    label_10=Label(window,text="Address",fg="black",bg="pale turquoise",font=("Constantia",20))
    label_10.place(x=850,y=320)
   
    label_11=Label(window,text="Address Line 1*",bg="pale turquoise",fg="black",font=("Constantia",20))
    label_11.place(x=850,y=360)
    alone=StringVar()
    entry_11=Entry(window,font=("Constantia",20),textvar=alone)
    entry_11.place(x=1050,y=360)

    label_12=Label(window,text="Address Line 2*",bg="pale turquoise",fg="black",font=("Constantia",20))
    label_12.place(x=850,y=400)
    altwo=StringVar()
    entry_12=Entry(window,font=("Constantia",20),textvar=altwo)
    entry_12.place(x=1050,y=400)

    label_13=Label(window,text="Address Line 3",bg="pale turquoise",fg="black",font=("Constantia",20))
    label_13.place(x=850,y=440)
    althree=StringVar()
    entry_13=Entry(window,font=("Constantia",20),textvar=althree)
    entry_13.place(x=1050,y=440)

    label_14=Label(window,text="Where did life take you, after SV",fg="black",bg="pale turquoise",font=("Constantia",16))
    label_14.place(x=850,y=540)
    wdltyas=StringVar()
    entry_14=Entry(window,font=("Constantia",20),textvar=wdltyas)
    entry_14.place(x=850,y=580)

    label_15=Label(window,text="Fondest memory of life at SV",fg="black",bg="pale turquoise",font=("Constantia",16))
    label_15.place(x=1200,y=540)
    fmolas=StringVar()
    entry_15=Entry(window,font=("Constantia",20),textvar=fmolas)
    entry_15.place(x=1200,y=580)

    label_ch=Label(window, text="I am a ",fg="red",bg="pale turquoise",font=("Constantia",20))
    label_ch.place(x=10,y=10)
    list3=['Alumni','Student']
    c3=StringVar()
    droplist3=OptionMenu(window,c3, *list3)
    c3.set('...')
    droplist3.config(width=20,font=("Constantia",16))
    droplist3.place(x=90,y=10)

    label_info=Label(window,text="IF YOU ARE A STUDENT YOU NEED NOT FILL \n 'Years spent in SV','Marital Status',\n 'Proffesion', 'Where did life take you, after SV',\n 'Fondest memory of life at SV' ",fg="red",bg="pale turquoise",font=("Constantia",15))
    label_info.place(x=1000,y=10)
       
    sub_button=Button(window,text="Submit",font=("Constantia",20),width=20,bg="black",fg="white",command =storing_Rdetails)
    sub_button.place(x=850,y=680)

#function to check whether user exists and opens its corresponding window
def proceed_nextWindow(a,b):
    global windowF
    query = """select USER_ID,Password from alumni_table where USER_ID=%s"""
    cursor.execute(query,(a,)) 
    res=cursor.fetchall()
    if a!="":
        if res==[(a,b)]:
            #if user exists,their home page will be opened            
            global window1
            window1=Tk()
            window1.geometry("3000x1000")
            window1.title("Alumni window")

            #adding a background colour(image)
            photo_pb2=PhotoImage(master=window1,file="violet.png")
            label_pb2=Label(window1, image=photo_pb2)
            label_pb2.pack()

            #adding a welcome message on the top.
            welcome_label=Label(window1,text="Hello",fg="black",bg="white",font=("Times New Roman",20,"bold"))
            welcome_label.place(x=600,y=30)
            query_name="select name from alumni_table where USER_ID=%s"
            cursor.execute(query_name,(a,))
            w_name=cursor.fetchall()
            welcomename_label=Label(window1, text=w_name, fg="black",bg="white",font=("Times New Roman",20,"bold"))
            welcomename_label.place(x=665,y=30)

            #message that shows there login is success.
            logSuccess_label=Label(window1,text="Login success !",bg="medium purple",fg='black',font=("arial",14,"bold"))
            logSuccess_label.place(x=20,y=10)

            #button for logout option.
            button_logout=Button(window1,text="Logout",fg='white',bg='brown',relief=RIDGE,font=("arial",13,"bold"),width=10,command=logout)
            button_logout.place(x=1415,y=15)

            #contact admin window for accepting user's values.
            def con_adm():                    
                windowC=Tk()
                windowC.geometry("500x300")
                windowC.title("Contact admin")
                windowC.configure(bg="light yellow")
                
                getusid_label=Label(windowC,text="User id:",bg="light yellow",fg='black',font=("arial",15))
                getusid_label.place(x=20,y=40)
                Cus=StringVar()
                getusid_entry=Entry(windowC,width=23,font=("Verdena",15),textvar=Cus)
                getusid_entry.place(x=200,y=40)

                comment_label=Label(windowC,text="COMMENT:",bg="light yellow",fg='black',font=("arial",15))
                comment_label.place(x=20,y=100)
                commentt=StringVar()
                comment_entry=Entry(windowC,width=23,font=("Verdena",15),textvar=commentt)
                comment_entry.place(x=200,y=100)

                #function for sending the message through g-mail.
                def confirm_con():
                    import smtplib as sb
                    user = getusid_entry.get()
                    coment = comment_entry.get()
                    s=sb.SMTP('smtp.gmail.com',587)
                    s.starttls()
                    s.login('*****@gmail.com','*****')
                    msg = "Hey,\n --ALUMNI INFORMATION SYSTEM--\n My USER ID is "+user+"\n"+coment+"\nThanks"
                    
                    receiver_list = ["*******@gmail.com","*******@gmail.com"]
                    for receivers in receiver_list:
                        s.sendmail('*******@gmail.com',receivers,msg)
                    s.quit()
                    label_currdel=Label(windowC,text="Message sent Successfully",fg="black",font=("Copperplate Gothic",12,"bold"))
                    label_currdel.place(x=100,y=230)
                    
                #button used to send the message to admin.
                button_contact=Button(windowC,text="Enquire",fg='red',bg='light yellow',relief=RIDGE,font=("arial",16,"bold"),width=10,command=confirm_con)
                button_contact.place(x=170,y=170)
                
            #contact user window for accepting admin's values.
            def con_user():
                windowE=Tk()
                windowE.geometry("500x300")
                windowE.title("Message users")
                windowE.configure(bg="light yellow")
                
                msg_label=Label(windowE,text="Message :",bg="light yellow",fg='black',font=("arial",15))
                msg_label.place(x=20,y=40)
                Cus=StringVar()
                msg_entry=Entry(windowE,width=23,font=("Verdena",15),textvar=Cus)
                msg_entry.place(x=200,y=40)

                def confirm_send():
                    import smtplib as sb
                    s=sb.SMTP('smtp.gmail.com',587)
                    s.starttls()
                    s.login('****@gmail.com','******')
                    msg = msg_entry.get()
                    
                    cursor.execute("select e_mail from alumni_table")
                    user_mailList=[]
                    for i in cursor:
                        user_mailList.append(i[0])
                    
                    for receivers in user_mailList:
                        s.sendmail('********@gmail.com',receivers,msg)
                    s.quit()
                    label_currdel=Label(windowE,text="Message sent Successfully",fg="black",font=("Copperplate Gothic",12,"bold"))
                    label_currdel.place(x=100,y=230)
                

                button_contact=Button(windowE,text="Send",fg='red',bg='light yellow',relief=RIDGE,font=("arial",16,"bold"),width=10,command=confirm_send)
                button_contact.place(x=170,y=170)
                
           #this function is to get the entry to search for an alumni.
            def store_search():
                search=search_entry.get()
                search_alumni(search)

            search_entry=Entry(window1,width=26,font=(259))
            search_entry.place(x=960,y=18)
            
            #button to search for the user.
            search_button=Button(window1,text="Search",fg='black',bg='grey',relief=RIDGE,width=13,font=("arial",13,"bold"),command=store_search)
            search_button.place(x=1255,y=15)

            #school name title
            schname_label=Label(window1,text="SARASWATHI VIDYALAYA",fg="brown",font=("arial",30,"bold"))
            schname_label.place(x=500,y=110)

            #function which is used to display the ongoing event.
            def find_Event():
                query="select * from event"
                cursor.execute(query)
                res1=cursor.fetchall()
                if res1!=[]:
                    windowF=Tk()
                    windowF.geometry("900x600")
                    windowF.title("Find Events")
                    windowF.configure(bg="light yellow")
                    label_0=Label(windowF,text="ALUMNI MEET",fg="blue",bg="light yellow",font=("Copperplate Gothic",25,"bold"))
                    label_0.place(x=380,y=35)

                    label_o=Label(windowF,text="Details of the event :",fg="blue",bg="light yellow",font=("Copperplate Gothic",18,"bold"))
                    label_o.place(x=30,y=100)

                    label_1=Label(windowF,text="Name of the organiser :",fg="black",bg="light yellow",font=("Verdana",15))
                    label_1.place(x=50,y=150)

                    label_2=Label(windowF,text="Batch :",fg="black",bg="light yellow",font=("Verdana",15))
                    label_2.place(x=50,y=190)

                    label_3=Label(windowF,text="Date :",fg="black",bg="light yellow",font=("Verdana",15))
                    label_3.place(x=50,y=230)

                    label_4=Label(windowF,text="Timings :",fg="black",bg="light yellow",font=("Verdana",15))
                    label_4.place(x=50,y=270)

                    label_5=Label(windowF,text="Venue :",fg="black",bg="light yellow",font=("Verdana",15))
                    label_5.place(x=50,y=310)

                    label_6=Label(windowF,text="Contact:",fg="black",bg="light yellow",font=("Verdana",15))
                    label_6.place(x=50,y=350)

                    eve_list=Listbox(windowF,height=8,width=30, font=("Verdana",20))
                    for i in range(len(res1[0])):
                        eve_list.insert(i,res1[0][i])
                        eve_list.place(x=400,y=150)
                        
                #if there is no event,this part will get executed
                else:
                    messagebox.showinfo("Check later !","No events organised . Pls check later or you can also organize using the schedule event option")                    

            #function used to add the event details to database and display in find event button.
            def conf_sch():
                query="select Name from event"
                cursor.execute(query)
                l=list(cursor)
                n=len(l)
                
                if n>=1:
                    messagebox.showinfo("Error","There is an existing event Pls schedule once it expires")
                else:
                    namme=entry_1SE.get()
                    batch=entry_2SE.get()
                    date=entry_3SE.get()
                    time=entry_4SE.get()
                    ven=entry_5SE.get()
                    cont=entry_6SE.get()
                    if namme=="" or batch=="" or date=="" or time=="" or ven=="" or cont=="":
                        messagebox.showinfo("Error","Pls fill in all the details")
                    else:
                        query = "insert into event(name,batch,date,time,venue,contact) values(%s,%s,%s,%s,%s,%s)"
                        val=(namme,batch,date,time,ven,cont)
                        cursor.execute(query,val)
                        mycon.commit()
                        messagebox.showinfo("ok","Event created successfully")
                
            #function which is used to check for any ongoing event.
            findE_button=Button(window1,text="FIND EVENT",fg='red',bg='light yellow',font=("arial",18,"bold"),width=18,command=find_Event)
            findE_button.place(x=50,y=640)
              
            #function that displays a window to accept details for scheduling an event.
            def schedule_eve():
                global entry_1SE
                global entry_2SE
                global entry_3SE
                global entry_4SE
                global entry_5SE
                global entry_6SE

                windowSE=Tk()
                windowSE.geometry("900x600")
                windowSE.title("Schedule Events")
                windowSE.configure(bg="light yellow")
                label_0=Label(windowSE,text="ALUMNI MEET",fg="blue",bg="light yellow",font=("Copperplate Gothic",25,"bold"))
                label_0.place(x=380,y=35)

                label_o=Label(windowSE,text="Provide some details to schedule an event:",fg="blue",bg="light yellow",font=("Copperplate Gothic",18,"bold"))
                label_o.place(x=30,y=100)

                label_1=Label(windowSE,text="Name:",fg="black",bg="light yellow",font=("Verdana",15))
                label_1.place(x=50,y=150)

                nameSE=StringVar()
                entry_1SE=Entry(windowSE, font=("Constantia",17),textvar=nameSE)
                entry_1SE.place(x=240,y=150)

                label_2=Label(windowSE,text="Batch :",fg="black",bg="light yellow",font=("Verdana",15))
                label_2.place(x=50,y=200)

                batchSE=StringVar()
                entry_2SE=Entry(windowSE, font=("Constantia",17),textvar=batchSE)
                entry_2SE.place(x=240,y=200)

                label_3=Label(windowSE,text="Date :",fg="black",bg="light yellow",font=("Verdana",15))
                label_3.place(x=50,y=250)

                dateSE=StringVar()
                entry_3SE=Entry(windowSE, font=("Constantia",17),textvar=dateSE)
                entry_3SE.place(x=240,y=250)

                label_4=Label(windowSE,text="Timings :",fg="black",bg="light yellow",font=("Verdana",15))
                label_4.place(x=50,y=300)

                timeSE=StringVar()
                entry_4SE=Entry(windowSE, font=("Constantia",17),textvar=timeSE)
                entry_4SE.place(x=240,y=300)

                label_5=Label(windowSE,text="Venue :",fg="black",bg="light yellow",font=("Verdana",15))
                label_5.place(x=50,y=350)

                venSE=StringVar()
                entry_5SE=Entry(windowSE, font=("Constantia",17),textvar=venSE)
                entry_5SE.place(x=240,y=350)

                label_6=Label(windowSE,text="Contact:",fg="black",bg="light yellow",font=("Verdana",15))
                label_6.place(x=50,y=400)

                conSE=StringVar()
                entry_6SE=Entry(windowSE, font=("Constantia",17),textvar=conSE)
                entry_6SE.place(x=240,y=400)
                
                #button used to add the event details to the database and siplay in find event button.
                conf_eve_button = Button(windowSE,text="SUBMIT",fg='blue',bg='light yellow',font=("arial",18,"bold"),command=conf_sch)
                conf_eve_button.place(x=240,y=450)

            #function which displays all the comments and replies and also allows the alumnis and students to connect.
            def forum():
                forum_window = Tk() 
                forum_window.title("FORUM")
                h = Scrollbar(forum_window, orient = 'horizontal') 
                h.pack(side = BOTTOM, fill = X) 
                v = Scrollbar(forum_window) 
                v.pack(side = RIGHT, fill = Y) 
                t = Text(forum_window,  background = 'white', foreground = 'blue', font = ('Verdena', 11),width = 100, height = 40, wrap = NONE,
                         xscrollcommand = h.set,  
                         yscrollcommand = v.set)

                t.insert(END,"\n\n\n\n\n")

                cursor.execute("select * from forum")
                content1 = list(cursor)
                for i in range(len(content1)):
                    s_no1 = "Post "+"#"+str(content1[i][0])+"  "
                    u_id1 = "User id : "+ content1[i][1]+"\n"
                    mesg1="Comment : "+content1[i][2]
                    full_cont1=s_no1+u_id1+mesg1
                    t.insert(END,full_cont1)
                    t.insert(END,"\n\n")
                    
                cursor.execute("select * from reply_forum")
                content2 = list(cursor)
                for j in range(len(content2)):
                    s_no2 = "Reply "+"#"+str(content2[j][0])+"  "
                    u_id2 = "User id : "+ content2[j][1]+"\n"
                    mesg2="Message : "+content2[j][2]
                    full_cont2=s_no2+u_id2+mesg2
                    t.insert(END,full_cont2)
                    t.insert(END,"\n\n")
                
                t.pack(side=TOP, fill=X)
                h.config(command=t.xview) 
                v.config(command=t.yview)
                

                #function that accepts details for adding your comment.
                def createPost():
                    #global gettusid_entry
                    global msg_entry
                    Cp_window = Tk()
                    Cp_window.geometry("500x300")
                    Cp_window.title("Create a comment")

                    #gettusid_label=Label(Cp_window,text="User id:",bg="light yellow",fg='black',font=("arial",15))
                    #gettusid_label.place(x=20,y=40)

                    #gettusid_entry=Entry(Cp_window,width=23,font=("Verdena",15))
                    #gettusid_entry.place(x=200,y=40)

                    msg_label=Label(Cp_window,text="Comment:",bg="light yellow",fg='black',font=("arial",15))
                    msg_label.place(x=20,y=100)

                    msg_entry=Entry(Cp_window,width=23,font=("Verdena",15))
                    msg_entry.place(x=200,y=100)

                    #function used to add a comment in the forum window.
                    def confirm_post():
                        #user = gettusid_entry.get()
                        msgg = msg_entry.get()
                        query="insert into forum (user_id,comment) values (%s,%s)"
                        val=(us_id,msgg)
                        cursor.execute(query,val)
                        mycon.commit()
                        messagebox.showinfo("Done","Post Created!")

                    #button used to add a comment in the forum window.
                    post_button=Button(Cp_window,text="Post",fg='red',bg='light yellow',relief=RIDGE,font=("arial",16,"bold"),width=10,command=confirm_post)
                    post_button.place(x=170,y=170)

                #function that accepts details for adding your replies.
                def replyPost():
                    global id_entry
                    #global usId_entry
                    global rep_entry

                    Rp_window = Tk()
                    Rp_window.geometry("500x400")
                    Rp_window.title("Reply to a comment")

                    id_label=Label(Rp_window,text="Post ID:",bg="light yellow",fg='black',font=("arial",15))
                    id_label.place(x=20,y=40)

                    id_entry=Entry(Rp_window,width=23,font=("Verdena",15))
                    id_entry.place(x=200,y=40)

                    #usId_label=Label(Rp_window,text="User id:",bg="light yellow",fg='black',font=("arial",15))
                    #usId_label.place(x=20,y=100)

                    #usId_entry=Entry(Rp_window,width=23,font=("Verdena",15))
                    #usId_entry.place(x=200,y=100)

                    rep_label=Label(Rp_window,text="Reply :",bg="light yellow",fg='black',font=("arial",15))
                    rep_label.place(x=20,y=160)

                    rep_entry=Entry(Rp_window,width=23,font=("Verdena",15))
                    rep_entry.place(x=200,y=160)

                    #function used to add a reply in the forum window.
                    def confirm_reply():
                        pId = id_entry.get()
                        #usId = usId_entry.get()
                        rep = rep_entry.get()
                        query="insert into reply_forum (pId,usId,rep) values (%s,%s,%s)"
                        val=(pId,us_id,rep)
                        cursor.execute(query,val)
                        mycon.commit()
                        messagebox.showinfo("Done","Reply Post Created!")

                    #button used to add a reply in the forum window.
                    postR_button = Button(Rp_window,text="Post",fg='red',bg='light yellow',relief=RIDGE,font=("arial",16,"bold"),width=10,command=confirm_reply)
                    postR_button.place(x=170,y=250)
                    
                #button used for adding comments
                createPost_button = Button(forum_window,text="Create Post",fg='blue',bg='light yellow',font=("arial",15,"bold"),command=createPost)
                createPost_button.place(x=10,y=10)

                #button used for adding replies
                reply_button = Button(forum_window,text="Reply to a Post",fg='blue',bg='light yellow',font=("arial",15,"bold"),command=replyPost)
                reply_button.place(x=170,y=10)

            #button which displays all the comments and replies when clicked.
            forum_button=Button(window1,text="FORUM",fg='red',bg='light yellow',font=("arial",18,"bold"),width=25,command=forum)
            forum_button.place(x=740,y=640)


           # function for "A good deed a day"
            def GD():
                windowGD=Tk()
                windowGD.geometry("800x400")
                windowGD.title("A good deed a day")

                #Cloud Image
                photo_GD=PhotoImage(master=windowGD,file="Cloud.png")
                
                label_GD=Label(windowGD, image=photo_GD)
                label_GD.pack()
                
                #function which displays the task using random module.
                def display_GD():
                    import random
                    l=["Help a friend in need","Save electricity by unpluging your devices when not in use","Buy a gift for your parents or grandparents ","Plant a tree","Organize a family meal and appreciate being together","Take time to appreciate nature","Donate blood","Hold the door open for a stranger","Donate unneede things to a charitable organization","Teach an elderly person to surf the Internet"]
                    s=random.choice(l)
                    labelGD=Label(windowGD,text=s,fg="black",bg="pale turquoise",font=("arial",19))
                    labelGD.place(x=150,y=251)
                    

                label_msg=Label(windowGD,text="A good deed a day keeps the depression away",fg="black",bg="pale turquoise",font=("Monotype Corsiva",18))
                label_msg.place(x=170,y=100)

                #button which will display the task to be done.
                dGD_button=Button(windowGD,text="Click here to know",fg="black",bg="pale turquoise",font=("arial",13,"bold"),command=display_GD)
                dGD_button.place(x=150,y=250)
                
                mainloop()

           #Friendship calculator
            def Friend_calz():
                windowFC=Tk()
                windowFC.geometry("550x500")
                windowFC.title("Friendship calculator")

                #Image
                photo_FC=PhotoImage(master=windowFC,file="friends.png")
                
                label_FC=Label(windowFC, image=photo_FC)
                label_FC.pack()

                label_un=Label(windowFC,text="Enter your name",fg="pink",bg="black",font=("Constantia",14))
                label_un.place(x=35,y=80)
                ur_name=StringVar()    
                entry_un=Entry(windowFC, font=("Constantia",14),textvar=ur_name)
                entry_un.place(x=35,y=110)

                label_fn=Label(windowFC,text="Enter your friend's name",fg="pink",bg="black",font=("Constantia",14))
                label_fn.place(x=300,y=80)
                frnd_name=StringVar()   
                entry_fn=Entry(windowFC, font=("Constantia",14),textvar=frnd_name)
                entry_fn.place(x=300,y=110)

                def conf_calz():
                    name1=entry_un.get()
                    name2=entry_fn.get()
                    string=name1.lower()+name2.lower()
                    score=0
                    al="bcdfghjklmnpqrstvwxyz"
                    vo="aeiou"
                    f="friends"
                    b="best"
                    for i in string:
                        if i in al:
                            score+=al.find(i)
                        elif i in vo:
                            score+=4
                        if i in f:
                            score+=7
                        if i in b:
                            score+=7
                    import random
                    if score==0:
                        per=0
                        res="Please enter two names"
                    elif score>0 and score<=50:
                        per=random.randint(1,20)
                        res="Formal friends"
                    elif score>50 and score<=100:
                        per=random.randint(21,40)
                        res="Friends"
                    elif score>100 and score<=150:
                        per=random.randint(41,60)
                        res="Close friends"
                    elif score>150 and score<=600:
                        per=random.randint(61,80)
                        res="Best friends"
                    elif score>600:
                        per=random.randint(81,100)
                        res="Best friends forever"
                    
                    label_per=Label(windowFC,text=per,fg="pink",bg="black",font=("Constantia",14))
                    label_per.place(x=250,y=400)
                    label_sym=Label(windowFC,text="%",fg="pink",bg="black",font=("Constantia",14))
                    label_sym.place(x=290,y=400)

                    label_bff=Label(windowFC,text=res,fg="pink",bg="black",font=("Constantia",14))
                    label_bff.place(x=250,y=450)

                    
                dFC_button=Button(windowFC,text="Calculate",fg="pink",bg="black",font=("arial",14,"bold"),command=conf_calz)
                dFC_button.place(x=250,y=350)
                
                windowFC.mainloop()
            
           #this function is for managing users only by ADMIN
            def Manage_us():
                windowM=Tk()
                windowM.geometry("500x550")
                windowM.title("Manage Users")
                windowM.configure(bg="light yellow")

                label_0=Label(windowM,text="MANAGE USERS",fg="dark blue",relief="solid",font=("Copperplate Gothic",20,"bold"))
                label_0.place(x=120,y=18)

                label_info=Label(windowM,text="What do you want to do ?",fg="red",font=("Copperplate Gothic",15,"bold"))
                label_info.place(x=80,y=100)

                #this func is used to create a gui window for updating the information in the database(admin only)
                def manage_upd():
                    global entry_M
                    windowU=Tk()
                    windowU.geometry("1000x600")
                    windowU.configure(bg="light yellow")
                    windowU.title("Update")

                    label_0=Label(windowU,text="UPDATE USER",fg="dark blue",font=("Copperplate Gothic",20,"bold"))
                    label_0.place(x=250,y=20)

                    label_10=Label(windowU,text="User ID*",fg="black",font=("Constantia",20))
                    label_10.place(x=30,y=80)
                    use_id=StringVar()
                    
                    entry_M=Entry(windowU, font=("Constantia",17),textvar=use_id)
                    entry_M.place(x=220,y=80)
                   
                    #to update name
                    label_1=Label(windowU,text="Name",fg="black",font=("Constantia",20))
                    label_1.place(x=30,y=130)
                    fnameM=StringVar()
                    entry_1M=Entry(windowU, font=("Constantia",17),textvar=fnameM)
                    entry_1M.place(x=220,y=130)
                    
                    def Enameconf_upd():
                        usidupd=entry_M.get()
                        nametu=entry_1M.get()
                        if usidupd=="":
                            label_ptu1=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu1.place(x=530,y=80)   
                        elif nametu=="":
                            label_ptn=Label(windowU,text=" . . Please enter the name to be updated . . ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptn.place(x=530,y=80)   
                        else:
                            nameconf_upd()
                    def nameconf_upd():
                        usidupd=entry_M.get()
                        nametu=entry_1M.get()
                        query="update alumni_table set name=%s where user_id=%s"
                        val=(nametu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sn=Label(windowU,text="Name updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sn.place(x=630,y=130)
                    button1=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Enameconf_upd)
                    button1.place(x=520,y=130)

                    #to update email
                    label_2=Label(windowU,text="Email",fg="black",font=("Constantia",20))
                    label_2.place(x=30,y=180)
                    emailM=StringVar()
                    entry_2M=Entry(windowU, font=("Constantia",17),textvar=emailM)
                    entry_2M.place(x=220,y=180)

                    def Eemailconf_upd():
                        usidupd=entry_M.get()
                        emailtu=entry_2M.get()
                        if usidupd=="":
                            label_ptu2=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu2.place(x=530,y=80)   
                        elif emailtu=="":
                            label_pte=Label(windowU,text="Please enter the E-mail address to be updated",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_pte.place(x=530,y=80)   
                        else:
                            emailconf_upd()
                    def emailconf_upd():
                        usidupd=entry_M.get()
                        emailtu=entry_2M.get()
                        query="update alumni_table set e_mail=%s where user_id=%s"
                        val=(emailtu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_se=Label(windowU,text="E-mail ID updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_se.place(x=630,y=180)
                    button2=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Eemailconf_upd)
                    button2.place(x=520,y=180)

                    
                    #to udate phone no.
                    label_3=Label(windowU,text="Phone",fg="black",font=("Constantia",20))
                    label_3.place(x=30,y=230)
                    MobM=IntVar()
                    entry_3M=Entry(windowU, font=("Constantia",17),textvar=MobM)
                    entry_3M.place(x=220,y=230)
                    def Epnoconf_upd():
                        usidupd=entry_M.get()
                        pnotu=entry_3M.get()
                        if usidupd=="":
                            label_ptu3=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu3.place(x=530,y=80)   
                        elif pnotu=="":
                            label_ptpno=Label(windowU,text="Please enter the Phone number to be updated",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptpno.place(x=530,y=80)   
                        else:
                            pnoconf_upd()
                    def pnoconf_upd():
                        usidupd=entry_M.get()
                        pnotu=entry_3M.get()
                        query="update alumni_table set mobile_no=%s where user_id=%s"
                        val=(pnotu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_spn=Label(windowU,text="Phone no updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_spn.place(x=630,y=230)
                    button3=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Epnoconf_upd)
                    button3.place(x=520,y=230)

                    
                    #to update marital status
                    label_4=Label(windowU,text="Marital status",fg="black",font=("Constantia",20))
                    label_4.place(x=30,y=280)
                    marM=StringVar()
                    entry_4M=Entry(windowU, font=("Constantia",17),textvar=marM)
                    entry_4M.place(x=220,y=280)
                    def Emsconf_upd():
                        usidupd=entry_M.get()
                        mstu=entry_4M.get()
                        if usidupd=="":
                            label_ptu4=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu4.place(x=530,y=80)   
                        elif mstu=="":
                            label_ptms=Label(windowU,text="Please enter the marital status to be updated",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptms.place(x=530,y=80)   
                        else:
                            msconf_upd()
                    def msconf_upd():
                        usidupd=entry_M.get()
                        mstu=entry_4M.get()
                        query="update alumni_table set marital_status=%s where user_id=%s"
                        val=(mstu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sms=Label(windowU,text="Marital status updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sms.place(x=630,y=280)
                    button4=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Emsconf_upd)
                    button4.place(x=520,y=280)

                    
                    

                    #to update profession
                    label_5=Label(windowU,text="Profession",fg="black",font=("Constantia",20))
                    label_5.place(x=30,y=330)
                    proM=StringVar()
                    entry_5M=Entry(windowU, font=("Constantia",17),textvar=proM)
                    entry_5M.place(x=220,y=330)
                    def Eproffconf_upd():
                        usidupd=entry_M.get()
                        profftu=entry_5M.get()
                        if usidupd=="":
                            label_ptu5=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu5.place(x=530,y=80)   
                        elif profftu=="":
                            label_ptproff=Label(windowU,text=". Please enter the Profession to be updated .",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptproff.place(x=530,y=80)   
                        else:
                            proffconf_upd()
                    def proffconf_upd():
                        usidupd=entry_M.get()
                        profftu=entry_5M.get()
                        query="update alumni_table set proffession=%s where user_id=%s"
                        val=(profftu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sproff=Label(windowU,text="Profession updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sproff.place(x=630,y=330)
                    button5=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Eproffconf_upd)
                    button5.place(x=520,y=330)

                    

                    #to update address line 1
                    label_6=Label(windowU,text="Address l1",fg="black",font=("Constantia",20))
                    label_6.place(x=30,y=380)
                    al1=StringVar()
                    entry_6M=Entry(windowU, font=("Constantia",17),textvar=al1)
                    entry_6M.place(x=220,y=380)
                    def Eal1conf_upd():
                        usidupd=entry_M.get()
                        al1tu=entry_6M.get()
                        if usidupd=="":
                            label_ptu6=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu6.place(x=530,y=80)   
                        elif al1tu=="":
                            label_ptal1=Label(windowU,text=".Please enter the Adressline-1 to be updated.",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptal1.place(x=530,y=80)   
                        else:
                            al1conf_upd()
                    def al1conf_upd():
                        usidupd=entry_M.get()
                        al1tu=entry_6M.get()
                        query="update alumni_table set address_line1=%s where user_id=%s"
                        val=(al1tu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sal1=Label(windowU,text="Adress line-1 updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sal1.place(x=630,y=380)
                    button6=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Eal1conf_upd)
                    button6.place(x=520,y=380)



                    #to update address line 2
                    label_7=Label(windowU,text="Address l2",fg="black",font=("Constantia",20))
                    label_7.place(x=30,y=430)
                    al2=StringVar()
                    entry_7M=Entry(windowU, font=("Constantia",17),textvar=al2)
                    entry_7M.place(x=220,y=430)
                    def Eal2conf_upd():
                        usidupd=entry_M.get()
                        al2tu=entry_7M.get()
                        if usidupd=="":
                            label_ptu7=Label(windowU,text=" . Please the enter user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu7.place(x=530,y=80)   
                        elif al2tu=="":
                            label_ptal2=Label(windowU,text=".Please enter the Adressline-2 to be updated.",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptal2.place(x=530,y=80)   
                        else:
                            al2conf_upd()
                    def al2conf_upd():
                        usidupd=entry_M.get()
                        al2tu=entry_7M.get()
                        query="update alumni_table set address_line2=%s where user_id=%s"
                        val=(al2tu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sal2=Label(windowU,text="Adress line-2 updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sal2.place(x=630,y=430)
                    button7=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Eal2conf_upd)
                    button7.place(x=520,y=430)



                    #to update address line 3
                    label_8=Label(windowU,text="Address l3",fg="black",font=("Constantia",20))
                    label_8.place(x=30,y=480)
                    al3=StringVar()
                    entry_8M=Entry(windowU, font=("Constantia",17),textvar=al3)
                    entry_8M.place(x=220,y=480)
                    def Eal3conf_upd():
                        usidupd=entry_M.get()
                        al3tu=entry_8M.get()
                        if usidupd=="":
                            label_ptu8=Label(windowU,text=" . Please the enter user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu8.place(x=530,y=80)   
                        elif al3tu=="":
                            label_ptal3=Label(windowU,text=".Please enter the Adressline-3 to be updated.",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptal3.place(x=530,y=80)   
                        else:
                            al3conf_upd()
                    def al3conf_upd():
                        usidupd=entry_M.get()
                        al3tu=entry_8M.get()
                        query="update alumni_table set address_line3=%s where user_id=%s"
                        val=(al3tu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sal3=Label(windowU,text="Adress line-3 updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sal3.place(x=630,y=430)
                    button8=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Eal3conf_upd)
                    button8.place(x=520,y=480)



                    #to update user type                    
                    label_9=Label(windowU,text="User Type",fg="black",font=("Constantia",20))
                    label_9.place(x=30,y=530)
                    us_ty=StringVar()
                    entry_9M=Entry(windowU, font=("Constantia",17),textvar=us_ty)
                    entry_9M.place(x=220,y=530)
                    def Eutconf_upd():
                        usidupd=entry_M.get()
                        uttu=entry_9M.get()
                        if usidupd=="":
                            label_ptu9=Label(windowU,text=" . Please the enter user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu9.place(x=530,y=80)   
                        elif uttu=="":
                            label_ptut=Label(windowU,text=". Please enter the User type to be updated . ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptut.place(x=530,y=80)   
                        else:
                            utconf_upd()
                    def utconf_upd():
                        usidupd=entry_M.get()
                        uttu=entry_9M.get()
                        query="update alumni_table set user_type=%s where user_id=%s"
                        val=(uttu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_sut=Label(windowU,text="User type updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_sut.place(x=630,y=530)
                    button9=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Eutconf_upd)
                    button9.place(x=520,y=530)


                    #to update user id                    
                    label_10=Label(windowU,text="User ID (New)",fg="black",font=("Constantia",20))
                    label_10.place(x=30,y=580)
                    us_tyid=StringVar()
                    entry_10M=Entry(windowU, font=("Constantia",17),textvar=us_tyid)
                    entry_10M.place(x=220,y=580)
                    def Euidconf_upd():
                        usidupd=entry_M.get()
                        uidtu=entry_10M.get()
                        if usidupd=="":
                            label_ptu10=Label(windowU,text=" . Please enter the user ID of the person .  ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptu10.place(x=530,y=80)   
                        elif uidtu=="":
                            label_ptut=Label(windowU,text=".Please enter the new User ID to be updated. ",fg="light yellow",bg="dark blue",font=("arial",15))
                            label_ptut.place(x=530,y=80)   
                        else:
                            uidconf_upd()
                    def uidconf_upd():
                        usidupd=entry_M.get()
                        uidtu=entry_10M.get()
                        query="update alumni_table set user_id=%s where user_id=%s"
                        val=(uidtu,usidupd)
                        cursor.execute(query,val)
                        mycon.commit()
                        label_suid=Label(windowU,text="User ID updated successfully",fg="light yellow",bg="dark blue",font=("arial",15))
                        label_suid.place(x=630,y=580)
                    button10=Button(windowU,text="Update",fg="black",bg="white",font=("Copperplate Gothic",12),width=10,command=Euidconf_upd)
                    button10.place(x=520,y=580)

                    


                upd_button = Button(windowM,text="UPDATE",fg='blue',bg='light yellow',font=("arial",18,"bold"),width=15,command=manage_upd)
                upd_button.place(x=120,y=170)

                #this func is used to remove the user from the AIS community(admin only)
                def manage_del():
                    windowD=Tk()
                    windowD.geometry("500x500")
                    windowD.configure(bg="light yellow")
                    windowD.title("Delete")

                    label_0=Label(windowD,text="DELETE USER",fg="dark blue",font=("Copperplate Gothic",20,"bold"))
                    label_0.place(x=120,y=18)
                    
                    label_del=Label(windowD,text="Enter the user ID:",fg="black",font=("Constantia",15))
                    label_del.place(x=100,y=150)

                    us_del=StringVar()
                    entry_D=Entry(windowD, font=("Constantia",17),textvar=us_del)
                    entry_D.place(x=100,y=230)

                    #this func is used to connect with database and delete the given user.
                    def conf_del():
                        user_del = entry_D.get()
                        query="delete from alumni_table where USER_ID=%s"
                        val=(user_del,)
                        sql=cursor.execute(query,val)
                        mycon.commit()

                        if user_del=="":
                            label_last=Label(windowD,text="Pls enter the user id",fg="black",font=("Copperplate Gothic",12,"bold"))
                            label_last.place(x=100,y=350)
                            
                        else:
                            label_last=Label(windowD,text="User deleted Successfully",fg="black",font=("Copperplate Gothic",12,"bold"))
                            label_last.place(x=100,y=350)

                    conf_del_button = Button(windowD,text="CONFIRM",fg='red',bg='light yellow',font=("arial",15,"bold"),command=conf_del)
                    conf_del_button.place(x=100,y=310)

                    

                del_button = Button(windowM,text="DELETE",fg='blue',bg='light yellow',font=("arial",18,"bold"),width=15,command=manage_del)
                del_button.place(x=120,y=270)

                #function which is used to delete the ongoing event.
                def del_currEve():
                    query="delete from event"
                    sql=cursor.execute(query)
                    mycon.commit()

                    label_currdel=Label(windowM,text="Current event deleted Successfully",fg="black",font=("Copperplate Gothic",12,"bold"))
                    label_currdel.place(x=120,y=400)

                delE_button = Button(windowM,text="DELETE EVENT",fg='blue',bg='light yellow',font=("arial",18,"bold"),width=15,command=del_currEve)
                delE_button.place(x=120,y=370)

            if a[-9:]=="admin.com":
                manageDB_button=Button(window1,text="MANAGE USERS",fg='red',bg='light yellow',font=("arial",18,"bold"),width=18,command=Manage_us)
                manageDB_button.place(x=1210,y=640)

                conUsers_butt=Button(window1,text="E mail Users",fg='red',bg="white",font=("arial",16,"bold"),command=con_user)
                conUsers_butt.place(x=210,y=10)
                
            if a[-10:]=="alumni.com" or a[-11:]=="student.com":
                conAdmin_butt=Button(window1,text="Contact Admin",fg='red',bg="white",font=("arial",16,"bold"),command=con_adm)
                conAdmin_butt.place(x=210,y=10)

                GD_button=Button(window1,text="DO SOMETHING GOOD TODAY",fg="red",bg="light yellow",font=("arial",17,"bold"),width=25,command=GD)
                GD_button.place(x=1160,y=640)
            
            if a[-11:]=="student.com":
                Friend_button=Button(window1,text="FRIENDSHIP CALCULATOR",fg='red',bg='light yellow',font=("arial",17,"bold"),width=25,command=Friend_calz)
                Friend_button.place(x=360,y=640)

            if a[-10:]=="alumni.com" or a[-9:]=="admin.com":
                schedE_button=Button(window1,text="SCHEDULE EVENT",fg='red',bg='light yellow',font=("arial",18,"bold"),width=18,command=schedule_eve)
                schedE_button.place(x=390,y=640)

            #center picture in the window
            photo_p1=PhotoImage(master=window1,file="alumnistanding.png")
            label_p1=Label(window1, image=photo_p1)
            label_p1.place(x=160,y=220)
            
            #sv logo
            photo_p2=PhotoImage(master=window1,file="SV-logo.png")
            label_p2=Label(window1, image=photo_p2)
            label_p2.place(x=20,y=10)

            mainloop()
        #if the user does not exist,wrong pwd/id window will be opened in the login window
        else:
            window2=Tk()
            window2.geometry("500x100")
            window2.title("try again")
            label_2=Label(window2,text="Invalid username or password. Please try again or register",fg='red',font=("arial",12))
            label_2.place(x=26,y=34)

    #if the user does not enter anything,this window will be opened
    else:
        window2=Tk()
        window2.geometry("500x100")
        window2.title("try again")
        label_2=Label(window2,text="Please fill your details",fg='red',font=("arial",12))
        label_2.place(x=26,y=34)


#function to get login details and proceed
def storing_details():
    global us_id
    us_id=usid_entry.get()
    
    pwd=pwd_entry.get()
    proceed_nextWindow(us_id,pwd)

#button used to login to your AIS
login_button=Button(window,text="Login",fg='white',bg='brown',relief=RIDGE,font=("arial",12,"bold"),width=18,command=storing_details)
login_button.place(x=160,y=650)

#button used to register yourself to AIS community.
reg_button=Button(window,text="Register",fg='white',bg='brown',relief=RIDGE,font=("arial",12,"bold"),width=18,command=Registration_form)
reg_button.place(x=380,y=650)
