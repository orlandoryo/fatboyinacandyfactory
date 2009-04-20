import GameLogic, math

cont = GameLogic.getCurrentController()
owner = cont.getOwner()

#Get Sensors
EnemyCollision = cont.getSensor('EnemyCollision').isPositive()



#Get Actuators
move = cont.getActuator('enemyBounceBack')

if(EnemyCollision and owner.Eatting == False) :
	
	owner.FatLife -= cont.getSensor('EnemyCollision').getHitObject().enemydamage
	move.setLinearVelocity(0,15,0,1)
	GameLogic.addActiveActuator(move,1)
else :
	move.setLinearVelocity(0,0,0,1)
	GameLogic.addActiveActuator(move,1)