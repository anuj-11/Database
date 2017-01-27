import re
import MySQLdb

dict1={}
mac1=[]
db = MySQLdb.connect("localhost", "root", "root", "testdb")
cursor = db.cursor()

list1 =[]
with open('diag.out','rt') as in_file:
	#list1 =[]
	for line in in_file:
		matchObj = re.match("----- APmgr info: apmgrinfo -a",line, re.M|re.I)
		if matchObj:
			for line in in_file:
				list1.append(line)
				matchObj2 = re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3",line, re.M|re.I)
				if matchObj2:
					break
for link in list1:
	mac = re.findall(r'(?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2}', link, re.I)	
	if mac:
		m1=mac
		mac1.append(mac)
#		print mac

	ip4 = re.findall(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',link)
	if ip4:
		i4=ip4
#		ipv4_1.append(ip4)
#		print ip4

	ip6 = re.findall(r'([\da-fA-F]{4}::[\d])', link, re.I)
	if ip6:
		i6=ip6
#		ipv6_1.append(ip6)
#		print ip6

	dname = re.findall(r'\s.*Name\s.*:\s*(.*)', link)
	if dname:
		n1=dname
#		name1.append(dname)
#		print dname

	dstate = re.findall(r'\s.*State\s.*:\s*(.*)', link)
	if dstate:
		s1=dstate
#		state1.append(dstate)
#		print dstate

	dmesh = re.findall(r'\s.*Mesh Role\s.*:\s*(.*)', link)
	if dmesh:
		me1=dmesh
#		mesh_role1.append(dmesh)
#		print dmesh
		
	dpsk = re.findall(r'\s.*PSK\s.*:\s*(.*)', link)
	if dpsk:
		ps1=dpsk
#		psk1.append(dpsk)
#		print dpsk

	dtimer = re.findall(r'\s.*Timer\s.*:\s*(.*)', link)
	if dtimer:
		ti1=dtimer
#		timer1.append(dtimer)
#		print dtimer

	dtunnel = re.findall(r'\s.*Tunnel/Sec\s.*:\s*(.*)/', link)
	if dtunnel:
		tl1=dtunnel
#		tunnel1.append(dtunnel)
#		print dtunnel

	dsec = re.match(r'\s.*Tunnel/Sec\s.*:\s*(.*)', link)
	if dsec:
		s = dsec.group(1)
		d = s.split('/')
		se = d[1]
		se1=se
#		sec_mode1.append(se)

	dhw = re.findall(r'\s.*HW/SW Version\s.*:\s*(.*)/', link)
	if dhw:
		dh1=dhw
#		hw1.append(dhw)
#		print dhw

	dsw = re.match(r'\s.*HW/SW Version\s.*:\s*(.*)', link)
	if dsw:
		a = dsw.group(1)
		b = a.split('/')
		sw = b[1]
		sw1=sw
#		sw1.append(sw)

	dmodel = re.findall(r'\s.*Model/Serial Num\s.*:\s*(.*)/', link)
	if dmodel:
		mo1=dmodel
#		model1.append(dmodel)
#		print dmodel

	dserial = re.match(r'\s.*Model/Serial Num\s.*:\s*(.*)', link)
	if dserial:
		e = dserial.group(1)
		f = e.split('/')
		ser = f[1]
		ser1=ser
#		serial_num1.append(ser)

		dict1[m1[0]]= [m1[0],i4[0],i6[0],n1[0],s1[0],tl1[0],se1[0],me1[0],ps1[0],ti1[0],dh1[0],sw1[0],mo1[0],ser1[0]]

for i in mac1:
	a=i[0]
	if a in dict1:
		l=dict1[a]
		cursor.execute("""insert into tabledb values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13]))



#res1= ("insert into tabledb values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(mac[0],ip4[1],ip6[2],dname[3],dtunnel[4],se[5],dstate[6],dmesh[7],dpsk[8],dtimer[9],dhw[10],sw[11],dmodel[12],ser[13]))
	
		#cursor.execute(res1)
db.commit()
	
