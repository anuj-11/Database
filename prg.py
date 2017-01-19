import re
import MySQLdb

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
		print mac
		result=("insert into tabledb (MACAdddres) values('%s');" %mac[0])
                cursor.execute(result)
                db.commit()
	ip4 = re.findall(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',link)
	if ip4:
		print ip4
		result=("insert into tabledb (IPv4Address) values('%s');" %ip4[0])
                cursor.execute(result)
                db.commit()
	ip6 = re.findall(r'([\da-fA-F]{4}::[\d])', link, re.I)
	if ip6:
		print ip6
		result=("insert into tabledb (IPv6Address) values('%s');"% ip6[0])
                cursor.execute(result)
                db.commit()
	dname = re.findall(r'\s.*Name\s.*:\s*(.*)', link)
	if dname:
		print dname
		result=("insert into tabledb (Name) values('%s');"% dname[0])
                cursor.execute(result)
                db.commit()
	dstate = re.findall(r'\s.*State\s.*:\s*(.*)', link)
	if dstate:
		print dstate
		result=("insert into tabledb (State) values('%s');"% dstate[0])
                cursor.execute(result)
                db.commit()
	dmesh = re.findall(r'\s.*Mesh Role\s.*:\s*(.*)', link)
	if dmesh:
		print dmesh
		result=("insert into tabledb (Mesh_Role) values('%s');"% dmesh[0])
                cursor.execute(result)
                db.commit()			
	dpsk = re.findall(r'\s.*PSK\s.*:\s*(.*)', link)
	if dpsk:
		print dpsk
		result=("insert into tabledb (PSk) values('%s');"% dpsk[0])
                cursor.execute(result)
                db.commit()
	dtimer = re.findall(r'\s.*Timer\s.*:\s*(.*)', link)
	if dtimer:
		print dtimer
		result=("insert into tabledb (Timer) values('%s');"% dtimer[0])
                cursor.execute(result)
                db.commit()
	dtunnel = re.findall(r'\s.*Tunnel/Sec\s.*:\s*(.*)/', link)
	if dtunnel:
		print dtunnel
		result=("insert into tabledb (Tunnel) values('%s');"% dtunnel[0])
                cursor.execute(result)
                db.commit()
	dsec = re.match(r'\s.*Tunnel/Sec\s.*:\s*(.*)', link)
	if dsec:
		s = dsec.group(1)
		d = s.split('/')
		se = d[1]
		result=("insert into tabledb (sec_mode) values('%s');"% se[0])
                cursor.execute(result)
                db.commit()
	dhw = re.findall(r'\s.*HW/SW Version\s.*:\s*(.*)/', link)
	if dhw:
		print dhw
		result=("insert into tabledb (HW_Version) values('%s');"% dhw[0])
                cursor.execute(result)
                db.commit()
	dsw = re.match(r'\s.*HW/SW Version\s.*:\s*(.*)', link)
	if dsw:
		a = dsw.group(1)
		b = a.split('/')
		sw = b[1]
		result=("insert into tabledb (SW_Version) values('%s');"% sw[0])
                cursor.execute(result)
                db.commit()
	dmodel = re.findall(r'\s.*Model/Serial Num\s.*:\s*(.*)/', link)
	if dmodel:
		print dmodel
		result=("insert into tabledb (Model) values('%s');"% dmodel[0])
                cursor.execute(result)
                db.commit()
	dserial = re.match(r'\s.*Model/Serial Num\s.*:\s*(.*)', link)
	if dserial:
		e = dserial.group(1)
		f = e.split('/')
		ser = f[1]
		result=("insert into tabledb (Serial_number) values('%s');"% ser[0])
                cursor.execute(result)
                db.commit()


#if len(mac)==len(ip4)==len(ip6)==len(dname)==len(dstate)==len(dmesh)==len(dpsk)==len(dtimer)==len(dtunnel)==len(dsec)==len(dhw)==len(dsw)==len(dmodel)==len(dserial):
	#for i in range(len(mac)):
#res1= ("insert into tabledb values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(mac[0],ip4[1],ip6[2],dname[3],dtunnel[4],se[5],dstate[6],dmesh[7],dpsk[8],dtimer[9],dhw[10],sw[11],dmodel[12],ser[13]))
	
#cursor.execute(res1)
#db.commit()
	
