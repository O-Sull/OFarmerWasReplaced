b=0
yZeroID = 0
yWorldID = 1
while True:
	a=0
	for i in range(get_world_size()):
		#if i==get_world_size()/2:
			#b+=1
		for j in range(get_world_size()):
			if(get_pos_y()==0):
				yZeroID = measure()
			if(get_pos_y()==get_world_size()-1):
				yWorldID = measure()
			if can_harvest():
				a+=1	
			if can_harvest() and yZeroID == yWorldID:
				harvest()
				#b=0
			if can_harvest()==False and get_ground_type()==Grounds.Soil or get_entity_type()!=Entities.Pumpkin and get_ground_type()==Grounds.Soil:
				plant(Entities.Pumpkin)
			if can_harvest()==False and get_ground_type()==Grounds.Grassland or get_entity_type()!=Entities.Pumpkin and get_ground_type()==Grounds.Grassland:
				till()
				plant(Entities.Pumpkin)
			move(South)
		if can_harvest()==False:
			plant(Entities.Pumpkin)
		if(a>(get_world_size()*2)):
			move(East)
