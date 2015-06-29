import subprocess
import json

# ecs.py DescribeRegions
ecsfile = '/Users/aca/cmdb/ecs.py'
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

def get_ecs( reg ):
#	RegionID=cn-hangzhou
	str_reg="RegionID="+reg
	print str_reg
	clild1 = subprocess.Popen(["python",ecsfile,"DescribeInstances",str_reg],stdout=subprocess.PIPE)
	res = clild1.communicate()
	j = json.loads(res[0])

	arr = j["Instances"]["Instance"]
	for i in arr:
		print i["InstanceId"],i["InnerIpAddress"]["IpAddress"][0],i["PublicIpAddress"]["IpAddress"][0],i["ImageId"]
	

for i in regs:
	get_ecs(i)






