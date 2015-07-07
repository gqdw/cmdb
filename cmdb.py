import subprocess
import json
#from xlwt import Workbook
import xlwt

# ecs.py DescribeRegions
ecsfile = '/Users/aca/github/cmdb/ecs.py'
regs=[]

def get_regions():
	child1 = subprocess.Popen(["python",ecsfile,"DescribeRegions"],stdout=subprocess.PIPE)
	#child1 = subprocess.Popen(["python","/Users/aca/cmdb/ecs.py DescribeRegions"],stdout=subprocess.PIPE)
	#child1 = subprocess.Popen(["cat","/Users/aca/cmdb/ecs.py"],stdout=subprocess.PIPE)
	res = child1.communicate()
	#print res[0]
	#print type(res[0])
	
	j = json.loads(res[0])
	
	#print type(j)
	arr = j["Regions"]["Region"]
	#print type(arr)
	for i in arr:
	#	print i["LocalName"],i["RegionId"]
		regs.append(i["RegionId"])  
		#print arr[i]["LocalName"]
get_regions()
#print regs

class c_ecs:
	InstanceId=''
	InnerIpAddress=''
	PublicIpAddress=''
	ImageId=''
	Status = ''
	ZoneId = '' 
	def p(self):
		print ("InstanceId=%s \n InnerIpAddress=%s \n PublicIpAddress=%s \n ImageId=%s \n Status=%s \n ZoneId=%s" %(self.InstanceId,self.InnerIpAddress,self.PublicIpAddress,self.ImageId,self.Status,self.ZoneId))
	

#ecs arrays
arr_ecs = []

def get_ecs( reg ):
#	RegionID=cn-hangzhou
	str_reg="RegionID="+reg
#	print str_reg
	clild1 = subprocess.Popen(["python",ecsfile,"DescribeInstances",str_reg],stdout=subprocess.PIPE)
	res = clild1.communicate()
	j = json.loads(res[0])

	arr = j["Instances"]["Instance"]
	
	for i in arr:
#		print i["InstanceId"],i["InnerIpAddress"]["IpAddress"][0],i["PublicIpAddress"]["IpAddress"][0],i["ImageId"]
		e = c_ecs()
		e.InstanceId = i["InstanceId"]
		e.InnerIpAddress = i["InnerIpAddress"]["IpAddress"][0]
		e.PublicIpAddress = i["PublicIpAddress"]["IpAddress"][0]
		e.ImageId = i["ImageId"]
		e.Status = i["Status"]
		e.ZoneId = i["ZoneId"]
		arr_ecs.append(e)
#	return e
	
def save_to_file( filename ):
	wb = xlwt.Workbook()
	for i in regs:
		get_ecs(i)
		#wb.add_sheet(i)
	#	e = c_ecs()
	#	e = get_ecs(i)
	#	e.p()
		
	ws = wb.add_sheet('ecs')
	ws.write(0,0,'InstanceId')
	ws.write(0,1,'InnerIpAddress')
	ws.write(0,2,'PublicIpAddress')
	ws.write(0,3,'ImageId')
	ws.write(0,4,'Status')
	ws.write(0,5,'ZoneId')
	j = 1
	for i in arr_ecs:
		i.p()
		ws.write(j,0,i.InstanceId)
		ws.write(j,1,i.InnerIpAddress)
		ws.write(j,2,i.PublicIpAddress)
		ws.write(j,3,i.ImageId)
		ws.write(j,4,i.Status)
		ws.write(j,5,i.ZoneId)
		j = j+1
		
	#wb.save('ecs.xls')	
	wb.save( filename )	
#	book.add_sheet(i)
save_to_file('ecs.xls')
	

#for i in regs:
#	sheet1 = book.add_sheet(i)





