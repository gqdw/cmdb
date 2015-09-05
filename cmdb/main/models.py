from django.db import models

# Create your models here.

class Hostgroup(models.Model):
	groupname = models.CharField(max_length=30)
	def __unicode__(self):
		return self.groupname

class Region(models.Model):
	regionname = models.CharField(max_length=30)
	def __unicode__(self):
		return self.regionname
class Search(models.Model):
	times = models.IntegerField()	
	def __unicode__(self):
		return str(self.times)
	def add(self):
		self.times += 1
		self.save()

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
	hostname = models.CharField(max_length=30)
	eth0 = models.GenericIPAddressField()
	eth1 = models.GenericIPAddressField( blank=True,null=True )
	beizhu = models.TextField(blank=True)
#	Region = models.CharField(max_length=3,choices=CRegions)
	Region = models.ForeignKey(Region)
#	test = models.TextField()
#	test2 = models.TextField()
	def __unicode__(self):
		return '%s %s %s %s' % (self.hostname,self.eth0, self.eth1 ,self.group )

#	RegionID = 
#	os = 
#	cpu = 
#	memory = 
	


	
	
