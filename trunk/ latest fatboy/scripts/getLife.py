import GameLogic

cont = GameLogic.getCurrentController()
owner = cont.getOwner()
fatboy = 0
Scene = GameLogic.getCurrentScene()
for i in Scene.getObjectList() :
	if(i.getName() == "OBFatBoy Collision") :
		fatboy = i


owner.Life = fatboy.FatLife
