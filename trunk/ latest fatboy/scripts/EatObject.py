import GameLogic

cont = GameLogic.getCurrentController()
owner = cont.getOwner()
fatboy = 0
Scene = GameLogic.getCurrentScene()
for i in Scene.getObjectList() :
	if(i.getName() == "OBFatBoy Collision") :
		fatboy = i


#get Actuator 
collision = cont.getSensor('sensor')

if(fatboy.Eatting) :
	#if(isinstance(collision.getHitObject(), NoneType)) :
		property = collision.getHitObject().type
		if(property == 'addGum') :
			fatboy.gumball += 1
		collision.getHitObject().endObject()
		Increment = cont.getActuator(property)
		GameLogic.addActiveActuator(Increment,1)


