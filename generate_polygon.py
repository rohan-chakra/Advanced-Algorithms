import random
import math

class Helper:
	def clip(self,x,min,max):
		if(min > max):
			return x
		elif(x < min):
			return min
		elif(x >max):
			return max
		else:
			return x
	def generate_random_polygon(self, centreX, centreY, aveRadius, irregularity, spike_factor, numVerts):
		irregularity = self.clip(irregularity, 0, 1) * 2 * math.pi / numVerts
		spike_factor = self.clip(spike_factor, 0, 1) * aveRadius
		angleSteps = []
		lower = (2 * math.pi / numVerts) - irregularity
		upper = (2*math.pi / numVerts) + irregularity
		_sum = 0

		for i in range(numVerts):
			tmp = random.uniform(lower, upper)
			angleSteps.append(tmp)
			_sum += tmp

		k = _sum/(2*math.pi)
		for i in range(numVerts):
			angleSteps[i] = angleSteps[i]/k
		
		points = []
		angle = random.uniform(0, 2*math.pi)
		for i in range(numVerts) :
			r_i = self.clip( random.gauss(aveRadius, spike_factor), 0, 2*aveRadius )

			x = centreX + r_i*math.cos(angle)
			y = centreY + r_i*math.sin(angle)
			points.append( (int(x),int(y)) )
			
			angle = angle + angleSteps[i]
		
		return points

helper = Helper()
verts = helper.generate_random_polygon(centreX=150, centreY=150, aveRadius=100,\
irregularity=0.45, spike_factor=0.4, numVerts=15)

if __name__=='__main___':
	
	print(verts)