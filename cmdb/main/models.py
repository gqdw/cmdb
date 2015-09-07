from django.db import models

# Create your models here.

class Hostgroup(models.Model):
	groupname = models.CharField(max_length=30)
	def __unicode__(self):
		return self.groupname

class Region(models.Model):
	regionname = models.CharField(max_length=30,default='cn-hangzhou')
	def __unicode__(self):
		return self.regionname
class Search(models.Model):
	times = models.IntegerField()	
	def __unicode__(self):
		return str(self.times)
	def add(self):
		self.times += 1
		self.save()
class Os(models.Model):
	osname = models.CharField(max_length=10,default='Centos6',blank=True )
	def __unicode__(self):
		return self.osname
class Dbtype(models.Model):
#	dbname = models.CharField(max_length=20,unique=True)
	mem = models.CharField(max_length=20,unique=True)
	connections = models.IntegerField()
	iops = models.IntegerField()

class Rds(models.Model):
	group = models.ForeignKey(Hostgroup)
	dns = models.URLField(max_length=50)
	dbtype = models.ForeignKey(Dbtype)
#type ,mem,connections,iops
	Region = models.ForeignKey(Region,default=6)
	
class Host(models.Model):
	CRegions = (
		('hz','cn-hangzhou'),
		('ss','cn-shenzhen'),
		('qd','cn-qingdao'),
		('bj','cn-beijing'),
		('sh','cn-shanghai'),
		('hk','cn-hongkong'),
		('us1','us-west-1'),
	)
	group = models.ForeignKey(Hostgroup)
	os = models.ForeignKey(Os,default=1)
	hostname = models.CharField(max_length=30,unique=True)
	eth0 = models.GenericIPAddressField(unique=True)
	eth1 = models.GenericIPAddressField( blank=True,null=True )
	beizhu = models.TextField(blank=True)
#	Region = models.CharField(max_length=3,choices=CRegions)
	Region = models.ForeignKey(Region,default=6)
#	test = models.TextField()
#	test2 = models.TextField()
	def __unicode__(self):
		return '%s %s %s %s' % (self.hostname,self.eth0, self.eth1 ,self.group )

#	RegionID = 
#	os = 
#	cpu = 
#	memory = 
	


	
	
