class Person:
	"""人类"""
	def __init__(self,name):
		self.name = name
		self.gun = None #人手里的枪
		self.xue = 100  #人血
	'''老王安装子弹到弹夹中'''	
	def putBullToClip(self,clip,bullet):
		#子弹保存到弹夹
		clip.baocunBullet(bullet)

	def putClipToGun(self,clip,gun):
		#保存弹夹到枪中
		gun.baocunClip(clip)

	def naqiang(self,gun):
		self.gun = gun	
	def koubanji(self,diren):
		#枪开火
		self.gun.fire(diren)	

	def diaoxue(self,typeBull):
		if self.xue>0:
			self.xue -= typeBull

	def __str__(self):
		if	self.gun:
			return "%s的血量为:%d,他有枪%s"%(self.name,self.xue,self.gun)

		else:
			if self.xue>0:
				return "%s的血量为%d,他没有枪"%(self.name,self.xue)
			else:
				return "%s  已挂... "%self.name	
class Gun:
	def __init__(self,name):
		self.name = name  #name  哪种枪
		self.baocun1 = None  #弹夹
	def baocunClip(self,clip):
		if not self.baocun1: #只保存一份
			self.baocun1 = clip	
	def fire(self,diren):
		zidan_temp = self.baocun1.jianshaozidian()

		if zidan_temp:  #开火成功  ----》  子弹打中敌人
			zidan_temp.dazhong(diren)


	def __str__(self):
		if self.baocun1:
			return "当前枪的信息为%s,当前有弹夹"%self.name		
		else:
			return "当前枪的信息为%s,当前没有有弹夹"%self.name	
class Clip:
	"""弹夹类"""
	def __init__(self,numMax):
		self.numMax = numMax
		self.baocun = []  #子弹
	def baocunBullet(self,bullet):
		self.baocun.append(bullet)

	def jianshaozidian(self):
		if self.baocun:
			return self.baocun.pop()  #弹出子弹对象
		else:
		 	return None

	def __str__(self):
		return "当前弹夹的状态为%d/%d"%(len(self.baocun),self.numMax)	

class Bullet:
	"""子弹类"""
	def __init__(self,typeBull):  #typeBull 杀伤力
		self.typeBull = typeBull


	def dazhong(self,diren):
		#敌人掉血
		diren.diaoxue(self.typeBull)	

def main():
	#1.有老王这个对象
	laowang = Person("老王")
	#2.枪对象
	qbz95 = Gun("qbz95")
	#3.弹夹对象
	clip = Clip(20)
	for i in range(10):
		#4.一堆子弹
		bullet = Bullet(10)
		#5.老王将子弹放到弹夹中
		laowang.putBullToClip(clip,bullet)

	# #6.老王将弹夹放到枪中
	laowang.putClipToGun(clip,qbz95)

	#7.有敌人
	gebilaowang = Person("隔壁老王")

	#8.老王拿枪
	laowang.naqiang(qbz95)

	#9.打敌人
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	

	print(laowang)
	print(gebilaowang)

if __name__ == '__main__':

	main()