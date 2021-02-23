import random
class ItemValue: 

	def __init__(self, wt, val): 
		self.wt = wt 
		self.val = val 
		self.cost = val // wt 

	def __lt__(self, other): 
		return self.cost < other.cost 

# Greedy Approach 
class Knapsack:
	def GreedyKnapsack(self, wt, val, capacity, final_items, remaining): 
		iVal = [] 
		for i in range(len(wt)): 
			iVal.append(ItemValue(wt[i], val[i])) 

		iVal.sort(reverse=True) 
		remaining = iVal
		totalValue = 0
		for i in iVal: 
			curWt = i.wt 
			curVal = i.val 
			if capacity - curWt >= 0: 
				capacity -= curWt 
				totalValue += curVal 
				final_items.append(i)
		remaining = [i for i in iVal if i not in final_items]
		return totalValue, remaining 

	def randomized(self, maxValue,final_items,remaining, capacity):
		flag = 0
		for x in range(5):
			random_pick = random.choice(final_items)
			if(maxValue -random_pick.val + remaining[0].val > maxValue and capacity + random_pick.wt - remaining[0].wt >=0):
				maxValue = maxValue -random_pick.val + remaining[0].val 
				capacity = capacity + random_pick.wt - remaining[0].wt
				
				final_items.remove(random_pick)
				final_items.append(remaining[0])
				flag = 1

		if(flag == 1):
			return maxValue

		else:
			return None


if __name__ == "__main__": 
	wt = [10, 40, 20, 30] 
	val = [60, 40, 100, 120] 
	capacity = 50
	final_items =[]
	remaining = []
	k = Knapsack()
	maxValue,remaining = k.GreedyKnapsack(wt, val, capacity, final_items, remaining) 
	print("Maximum value in Knapsack =", maxValue) 

	new_maxValue = k.randomized(maxValue, final_items, remaining, capacity)
	if(new_maxValue!= None):
		print("Improved maximum value in Knapsack through randomization =", new_maxValue)
	else:
		print("No improvement :(")
