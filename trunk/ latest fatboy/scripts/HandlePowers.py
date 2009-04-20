import GameLogic, math

cont = GameLogic.getCurrentController()
owner = cont.getOwner()

#Get Sensors
G = cont.getSensor('G')


bodyArmProp = cont.getActuator('BodyArmatureProperty')
if(G.isPositive() and owner.gumball > 0) :
	owner.gumball = owner.gumball - 1
	owner.gumjump = True
	bodyArmProp.setProperty('Eat')
	bodyArmProp.set('False')
	GameLogic.addActiveActuator(bodyArmProp,1)
		
