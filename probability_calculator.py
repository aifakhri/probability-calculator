import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **marbles):
		contents = []
		for marble, count in marbles.items():
			for _ in range(count):
				contents.append(marble)
		self.contents = contents
		self.copy_contents = copy.copy(contents)

	def draw(self, number):
		marbles = []
		if number > len(self.contents):
			self.contents = copy.copy(self.copy_contents)
			return self.contents

		for _ in range(number):       
			marble = self.contents.pop(random.randint(0, len(self.contents)-1))
			marbles.append(marble)
		return marbles
  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	success = 0
	for _ in range(num_experiments):
		draw_marbles_count = {}
		draw_marbles = hat.draw(num_balls_drawn)

	#Redrawing the marbles after all the marbles returned to the hat
	if num_balls_drawn < len(draw_marbles):
		draw_marbles = hat.draw(num_balls_drawn)

	#Counting the drawn marbles
	for marble in draw_marbles:
		draw_marbles_count[marble] = draw_marbles_count.get(marble, 0) + 1

	validator = 0
	for expected_color, expected_count in expected_balls.items():
		try:
			if draw_marbles_count[expected_color] >= expected_count:
				validator = validator + 1
		except KeyError:
			continue

	if validator == len(expected_balls):
		success = success + 1
		
	probability = success/num_experiments
	return probability

if __name__ == "__main__":
	random.seed(95)
	hat = Hat(blue=4, red=2, green=6)
	probability = experiment(
		hat=hat,
		expected_balls={"blue": 4,
						"red": 2},
		num_balls_drawn=2,
		num_experiments=5000
	)
	print("Probability:", probability)
