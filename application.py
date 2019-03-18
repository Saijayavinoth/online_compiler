
from flask import Flask,render_template,request
import subprocess
from threading import Timer
application=Flask(__name__)

@application.route('/')
def fun():
	return render_template('index.html')

	
@application.route('/run',methods=['post'])
def run():
	cod=request.form['code']
	lang=request.form['lang']
	inp=request.form['input']
	p=''
	if lang=='c':
		f=open('cod.c','w')
		f.write(cod)
		f.close()
		c=subprocess.Popen(['gcc','cod.c','-o cod'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE).communicate()[1]
		if len(c)>0:
			return render_template('index.html',code=cod,input=inp,output=c.decode('utf-8'),lang=lang)
		p=subprocess.Popen(['./ cod'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	elif lang=='c++':
		f=open('cod.cpp','w')
		f.write(cod)
		f.close()
		c=subprocess.Popen(['g++','cod.cpp','-o cod'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE).communicate()[1]
		if len(c)>0:
			return render_template('index.html',code=cod,input=inp,output=c.decode('utf-8'),lang=lang)
		p=subprocess.Popen(['./ cod'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	elif lang=='java':
		f=open('cod.java','w')
		f.write(cod)
		f.close()
		c=subprocess.Popen(['javac','cod.java'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE).communicate()[1]
		if len(c)>0:
			return render_template('index.html',code=cod,input=inp,output=c.decode('utf-8'),lang=lang)
		p=subprocess.Popen(['java','cod'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	elif lang=='python':
		f=open('cod.py','w')
		f.write(cod)
		f.close()
		p=subprocess.Popen(['python','cod.py'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	elif lang=='python3':
		f=open('cod.py','w')
		f.write(cod)
		f.close()
		p=subprocess.Popen(['python3','cod.py'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

	out=''
	
	#t=Timer(5,kill,[p])
	#t.start()
	c=p.communicate(input=(inp).encode('utf-8'))
	#p.wait()
	#t.cancel()
	
	if len(c[0])==0:
		out=c[1]
	else:
		out=c[0]
	


	
	
	return render_template('index.html',code=cod,input=inp,output=out.decode('utf-8'),lang=lang)
@application.route('/runa',methods=['post'])
def fun1():
	cod=request.form['code']
	return cod
if __name__ == "__main__":  
    application.debug = True
    application.run()