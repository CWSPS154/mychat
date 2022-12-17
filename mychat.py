from flask import Flask,render_template,request,session,redirect
from DBConnection import Db
from datetime import datetime

app = Flask(__name__)
app.secret_key="xyss"
# <-------------------------------------------------------------------------Register & Login------------------------------------------------------------------------------------->
@app.route('/')
def home():
    return render_template("Login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        gndr=request.form['gender']
        dob = request.form['dob']
        mob = request.form['mob']
        email=request.form['email']
        bio = request.form['bio']
        pswd=request.form['pass']

        q = "select email from login where email='" + str(email) + "'"
        ob = Db()
        em = ob.selectOne(q)

        q = "select mobil from profile where mobil='" + str(mob) + "'"
        ob = Db()
        mo = ob.selectOne(q)

        if em and mo is not None:
            return '''<script>alert('This email id and mobile number are already exiting');window.location='/register'</script>'''
        elif em is not None:
            return '''<script>alert('This email id is already exiting');window.location='/register'</script>'''
        elif mo is not None:
            return '''<script>alert('This mobile number is already exiting');window.location='/register'</script>'''

        ob=Db()
        id=ob.insert("insert into login values(null,'"+email+"','"+pswd+"','Ofline')")
        ob.insert("insert into user values('"+str(id)+"','"+name+"','"+gndr+"','"+email+"')")
        ob.insert("insert into profile values('"+str(id)+"','pending','"+email+"','"+mob+"','"+dob+"','"+bio+"')")
        return '''<script>alert('Your account is created,you can now login');window.location='/'</script>'''
    else:
        return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        pswd=request.form['pass']
        ob=Db()
        res=ob.selectOne("select * from login where email='"+email+"' and pswd='"+pswd+"'")
        if res is not None:
            session['lid'] = res['lid']
            return redirect('home')
        else:
            return '''<script>alert('Incorect email id or password');window.location='/'</script>'''
    else:
        return redirect('home')

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect('/')

@app.route('/home')
def home1():
    ob=Db()
    res = ob.selectOne("select * from user where lid='" + str(session['lid']) + "'")
    return render_template("home.html",res=res)

@app.route('/forget')
def forget():
    email=request.args.get('email')
    q="select mail from profile where mail='"+email+"'"
    ob=Db()
    un=ob.selectOne(q)
    if un is not None:
        session['email'] = un['mail']
        return '''<script>
        var mb = prompt("Enter your ragisterd Mobile Number"," "); 
        if (mb!=null)
        {
        window.location='/cgpsd3?mob='+mb;
        }
        else
        {
        alert("Cancelled");window.location='/';
        }
             </script>'''
    else:
        return '''<script> 
        var email = prompt("Incorect Email ID ,please enter your registerd Email ID", " ");
         if (email != null) 
            {
                window.location='/forget?email='+email;
            }
            else
            {
                alert("Cancelled");window.location='/';
            }
            </script>'''

@app.route('/cgpsd3')
def cgpsd3():
    mob = request.args.get('mob')
    q = "select mobil from profile where mobil='" + mob + "'"
    ob = Db()
    un = ob.selectOne(q)
    if un is not None:
        return '''<script>
        alert("Your account is found,you can set new password now");
            var npsd = prompt("Enter new Password", "Minimum 8 character is required");window.location='/';
            var n=npsd.length;
            if (n ==0 ) 
                {
                     alert("Please enter new password");window.location='/';
                }
            else if (n<8)
                {
                      alert("Minimum 8 charater required");window.location='/';
                      alert("Password is not changed");window.location='/';
                }
            else
                {
                    var rpsd = prompt("Retype new Password", " ");
                    if (npsd == rpsd)
                    {
                            window.location='/cgpsd2?npsd='+rpsd;
                    }
                    else
                    {
                            alert("Password is mismatch");window.location='/';
                            alert("Password is not changed");window.location='/';
                    }
                }
                </script>'''
    else:
        return '''<script>alert("Incorect Mobile Number");window.location = '/';</script>'''


@app.route('/cgpsd2')
def cgpsd2():
    npsd = request.args.get('npsd')
    ob=Db()
    ob.update("update login set pswd='"+npsd+"' where email='"+str(session['email'])+"'")
    return '''<script>alert("Password is changed");window.location='/';</script>'''

# <------------------------------------------------------------Profile----------------------------------------------------------------------------------------------->
@app.route('/profile')
def profile():
    ob=Db()
    res = ob.selectOne("select * from user,profile where user.lid='" + str(session['lid']) + "' and profile.uid=user.lid")
    return render_template("profile.html",res=res)
@app.route('/updatepic',methods=['GET','POST'])
def updatepic():
    if request.method == 'POST':
        img=request.files['img']
        import time
        fname = time.strftime("%Y%m%d_%H%M%S") + ".jpg"
        img.save(r"C:\Users\hiran\PycharmProjects\mychat\static\propic\\" + fname)
        ob=Db()
        ob.update("update profile set propic='"+fname+"' where uid='"+str(session['lid'])+"'")
        return redirect('profile')
    else:
        return redirect('profile')

@app.route('/dltpic')
def dltpic():
    ob=Db()
    ob.update("update profile set propic='pending' where uid='"+str(session['lid'])+"'")
    return redirect('profile')

@app.route('/updatebio',methods=['GET','POST'])
def updatebio():
    if request.method == 'POST':
        bio=request.form['about']
        ob=Db()
        ob.update("update profile set bio='"+bio+"' where uid='"+str(session['lid'])+"'")
        return redirect('profile')
    else:
        return redirect('profile')

@app.route('/cgpsd')
def cgpsd():
    q="select pswd from login where lid='"+str(session['lid'])+"'"
    ob=Db()
    un=ob.selectOne(q)
    if un['pswd']==request.args.get('psd'):
        return '''<script> 
        var npsd = prompt("Enter new Password", "Minimum 8 character is required");
        var n=npsd.length;
         if (n ==0 ) 
            {
                 alert("Please enter new password");window.location='/profile';
            }
            else if (n<8)
            {
                  alert("Minimum 8 charater required");window.location='/profile';
                  alert("Password is not changed");window.location='/profile';
            }
         else
            {
                var rpsd = prompt("Retype new Password", " ");
                if (npsd == rpsd)
                {
                        window.location='/cgpsd1?npsd='+rpsd;
                }
                else
                {
                        alert("Password is mismatch");window.location='/profile';
                        alert("Password is not changed");window.location='/profile';
                }
            }
             </script>'''
    else:
        return '''<script> 
        var psd = prompt("Incorect password ,please enter current Password", " ");
         if (psd != null) 
            {
                window.location='/cgpsd?psd='+psd;
            }
            else
            {
                alert("Password is not changed");window.location='/profile';
            }
            </script>'''

@app.route('/cgpsd1')
def cgpsd1():
    npsd = request.args.get('npsd')
    ob=Db()
    ob.update("update login set pswd='"+npsd+"' where lid='"+str(session['lid'])+"'")
    return '''<script>alert("Password is changed");window.location='/profile';</script>'''

# <-----------------------------------------------------------------------------Friends------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

@app.route('/friends')
def friends():
    ob = Db()
    frds = ob.select("select user.*,frds.*,profile.propic,profile.bio,year(profile.dob),month(profile.dob),day(profile.dob) from profile,frds left join user on  frds.mid='" + str(session['lid']) + "' and frds.uid=user.lid or frds.uid='" + str(session['lid']) + "' and frds.mid=user.lid where user.lid!='" + str(session['lid']) + "' and profile.uid=user.lid order by frds.status desc")
    import time
    year = time.strftime("%Y")
    month =time.strftime("%m")
    date = time.strftime("%d")
    ln = 0
    if len(frds) == 0:
        ln = 1
    return render_template("friends.html",frds=frds,ln=ln,y=int(year),m=int(month),d=int(date))

@app.route('/allfriends')
def allfriends():
    ob = Db()
    frds = ob.select("select user.*,frds.*,profile.* from profile,user left join frds on  frds.mid='" + str(session['lid']) + "' and frds.uid=user.lid or frds.uid='" + str(session['lid']) + "' and frds.mid=user.lid where user.lid!='" + str(session['lid']) + "' and profile.uid=user.lid order by frds.status")
    ln = 0
    if len(frds) == 0:
        ln = 1
    return render_template("allfriends.html",frds=frds,ln=ln)

@app.route('/frds')
def frds():
    uid=request.args.get('uid')
    ob=Db()
    ob.insert("insert into frds values(Null,'"+str(session['lid'])+"','"+uid+"','pending')")
    return redirect('friends')

@app.route('/unfrds')
def unfrds():
    uid = request.args.get('uid')
    ob = Db()
    ob.delete("delete from frds where mid='"+str(session['lid'])+"' and uid='"+uid+"' or  uid='"+str(session['lid'])+"' and mid='"+uid+"' ")
    return redirect('friends')

@app.route('/acptfrds')
def acptfrds():
    uid = request.args.get('uid')
    ob = Db()
    ob.update("update frds set status='friend' where uid='"+str(session['lid'])+"' and mid='"+uid+"' ")
    return redirect('friends')

@app.route('/chat')
def chat():
    ob = Db()
    frds = ob.select("select user.*,frds.*,profile.propic from profile,frds left join user on  frds.mid='" + str(session['lid']) + "' and frds.uid=user.lid or frds.uid='" + str(session['lid']) + "' and frds.mid=user.lid and frds.status='friend' where user.lid!='" + str(session['lid']) + "' and profile.uid=user.lid")
    res = ob.selectOne("select user.*,profile.propic from user,profile where user.lid='" + str(session['lid']) + "' and profile.uid=user.lid")
    msg='none'
    snd='none'
    ln = 0
    if len(frds) == 0:
        ln = 1
    return render_template("chat.html",frds=frds,res=res,ln=ln ,msg=msg,snd=snd)

@app.route('/msgs',methods=['GET','POST'])
def msgs():
        uid = request.args.get('uid')
        session['uid']=uid
        if request.method == 'POST':
            msg = request.form['msg']
            ob = Db()
            ob.insert("insert into msg VALUES (Null,'" + str(session['lid']) + "','" + str(session['uid']) + "','" + msg + "',CURRENT_TIMESTAMP())")
            msg = ob.select("select * from msg where msg_frm='" + str(session['lid']) + "' and msg_to='" + str(session['uid']) + "' or msg_frm='" + str(session['uid']) + "' and msg_to='" + str(session['lid']) + "'")
            snd = ob.selectOne("select user.*,profile.propic from profile,user where user.lid='" + str(session['uid']) + "' and profile.uid=user.lid")
            frds = ob.select("select user.*,frds.*,profile.propic from profile,frds left join user on  frds.mid='" + str(session['lid']) + "' and frds.uid=user.lid or frds.uid='" + str(session['lid']) + "' and frds.mid=user.lid and frds.status='friend' where user.lid!='" + str(session['lid']) + "' and profile.uid=user.lid")
            res = ob.selectOne("select user.*,profile.propic from profile,user where user.lid='" + str(session['lid']) + "' and profile.uid=user.lid")
            ln = 0
            if len(frds) == 0:
                ln = 1
        else:
            ob = Db()
            msg = ob.select("select * from msg where msg_frm='" + str(session['lid']) + "' and msg_to='" + str(session['uid']) + "' or msg_frm='" + str(session['uid']) + "' and msg_to='" + str(session['lid']) + "'")
            snd = ob.selectOne("select user.*,profile.propic from profile,user where user.lid='" + str(session['uid']) + "' and profile.uid=user.lid")
            frds = ob.select("select user.*,frds.*,profile.propic from profile, frds left join user on  frds.mid='" + str(session['lid']) + "' and frds.uid=user.lid or frds.uid='" + str(session['lid']) + "' and frds.mid=user.lid and frds.status='friend' where user.lid!='" + str(session['lid']) + "' and profile.uid=user.lid")
            res = ob.selectOne("select user.*,profile.propic from profile,user where lid='" + str(session['lid']) + "' and profile.uid=user.lid")
            ln = 0
            if len(frds) == 0:
                ln = 1
        return render_template("chat.html", frds=frds, res=res, msg=msg, snd=snd, ln=ln)

# @app.route('/msgs1',methods=['POST'])
# def msgs1():
#         msg=request.form['msg']
#         ob=Db()
#         ob.insert("insert into msg VALUES (Null,'"+str(session['lid'])+"','"+str(session['uid'])+"','"+msg+"',CURRENT_TIMESTAMP())")
#         return redirect('msgs')
if __name__ == '__main__':
    app.run(debug=True)
