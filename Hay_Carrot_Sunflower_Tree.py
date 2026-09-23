#change_hat(Hats.Brown_Hat)
#do_a_flip()
#pet_the_piggy()
#print("piggy pet complete")
#change_hat(Hats.Carrot_Hat)
#do_a_flip()
#print("initieting farming sequence")
#pet_the_piggy()
#print("piggy pet 2 complete")
#change_hat(Hats.Traffic_Cone)
#do_a_flip()
#print("initieting farming sequence for real this time")
#do_a_flip()
#print(get_pos_x(), get_pos_y())
#do_a_flip()
#print(num_items(Items.Carrot))
#do_a_flip()
#print(num_unlocked(Unlocks.Speed))
#do_a_flip()
some_list = [2, True, Items.Hay]
for x in some_list:
	print(x)
for i in range(10, 0, 8):
	print(i)
change_hat(Hats.Tree_Hat)
do_a_flip()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if(get_pos_x()<get_world_size()/3 and get_pos_y()<get_world_size()/2):
				if can_harvest():
					harvest()
				if can_harvest()==False and get_ground_type()==Grounds.Soil:
					till()
			else:
				if (get_pos_x()%2==0 and get_pos_y()%2!=0):
					if can_harvest():
						harvest()
						plant(Entities.Tree)
						#use_item(Items.Water)
						#print(get_water())
					if can_harvest()==False and get_ground_type()==Grounds.Grassland:
						till()
						plant(Entities.Sunflower)
					if can_harvest()==False and get_ground_type()==Grounds.Soil:
						plant(Entities.Tree)
				if (get_pos_x()%2!=0 and get_pos_y()%2==0):
					if can_harvest():
						harvest()
						plant(Entities.Sunflower)
						use_item(Items.Water)
					if can_harvest()==False and get_ground_type()==Grounds.Grassland:
						till()
						plant(Entities.Tree)
					if can_harvest()==False and get_ground_type()==Grounds.Soil:
						plant(Entities.Tree)
				if (get_pos_x()%2==0 and get_pos_y()%2==0):
					if can_harvest():
						harvest()
					if can_harvest()==False and get_ground_type()==Grounds.Soil:
						plant(Entities.Carrot)
					if can_harvest()==False and get_ground_type()==Grounds.Grassland:
						till()
						plant(Entities.Carrot)
				if (get_pos_x()%2!=0 and get_pos_y()%2!=0):
					if can_harvest():
						harvest()
					if can_harvest()==False and get_ground_type()==Grounds.Soil:
						plant(Entities.Carrot)
					if can_harvest()==False and get_ground_type()==Grounds.Grassland:
						till()
						plant(Entities.Carrot)
			move(South)
		if can_harvest():
			harvest()
		move(East)
	
	
	
	
	#if(get_pos_y()>=get_world_size()/2):
			#	if (get_pos_x()%2==0 and get_pos_y()%2!=0):
			#		if can_harvest():
			#			harvest()
			#			use_item(Items.Water)
			#			print(get_water())
			#			plant(Entities.Tree)
			#		if can_harvest()==False and get_ground_type()==Grounds.Soil:
			#			till()
			#			plant(Entities.Tree)
			#		if can_harvest()==False and get_ground_type()==Grounds.Grassland:
			#			plant(Entities.Tree)
			#	if (get_pos_x()%2==0 and get_pos_y()%2==0):
			#		if can_harvest():
			#			harvest()
			#		if can_harvest()==False and get_ground_type()==Grounds.Soil:
			#			plant(Entities.Carrot)
			#		if can_harvest()==False and get_ground_type()==Grounds.Grassland:
			#			till()
			#			plant(Entities.Carrot)
			#	if (get_pos_x()%2!=0):
			#		if can_harvest():
			#			harvest()
			#		if can_harvest()==False and get_ground_type()==Grounds.Soil:
			#			plant(Entities.Carrot)
			#		if can_harvest()==False and get_ground_type()==Grounds.Grassland:
			#			till()
			#			plant(Entities.Carrot)
	
	
	#for i in range(get_world_size()):
	#	for j in range(get_world_size()):
	#		if can_harvest():
	#			harvest()
	#			if(get_ground_type()==Grounds.Soil):
	#				plant(Entities.Carrot)
	#			move(South)
	#			if(get_entity_type()!=Entities.Tree):
	#				till()
	#			if can_harvest():
	#				harvest()
	#			plant(Entities.Tree)
	#			move(South)
	#		elif can_harvest()!=True:
	#			plant(Entities.Carrot)
	#			move(South)
	#			if can_harvest() and get_entity_type()==Entities.Grass:
	#				harvest()
	#				till()
	#				plant(Entities.Carrot)
	#	move(East)
	#	plant(Entities.Bush)
		
#for i in range(get_world_size()):
#	if can_harvest():
#		harvest()
#		move(South)
#		plant(Entities.Bush)
#	elif can_harvest()!=True:
#		move(South)
#		if can_harvest():
#			harvest()
#		elif can_harvest()!=True:
#			move(East)
#		plant(Entities.Bush)
