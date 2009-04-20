import GameLogic, math

cont = GameLogic.getCurrentController()
owner = cont.getOwner()

#Get Sensors
Jump = cont.getSensor('UP')
Left = cont.getSensor('LEFT')
Right = cont.getSensor('RIGHT')
ForwardCheck =  cont.getSensor('Forward Check').isPositive() & cont.getSensor('Forward Check1').isPositive() & cont.getSensor('Forward Check2').isPositive() & cont.getSensor('Forward Check3').isPositive()& cont.getSensor('Forward Check4').isPositive() & cont.getSensor('Forward Check5').isPositive() & cont.getSensor('Forward Check6').isPositive()
BackwardCheck =  cont.getSensor('Backward Check').isPositive() & cont.getSensor('Backward Check1').isPositive() & cont.getSensor('Backward Check2').isPositive() & cont.getSensor('Backward Check3').isPositive()& cont.getSensor('Backward Check4').isPositive() & cont.getSensor('Backward Check5').isPositive() & cont.getSensor('Backward Check6').isPositive()
groundCollision = cont.getSensor('groundCollision')

#Get Actuators
movement = cont.getActuator('Movement')

#initialize Variables
jumpforce = 0
move = 0
rot = 0
turn = owner.turn

#movement logic
if Left.isPositive()  and BackwardCheck :
	move = -3
elif Right.isPositive() and ForwardCheck :
	move = -3
if Jump.isPositive() and groundCollision.isPositive():
	jumpforce = 200
	if owner.gumjump == True :
		jumpforce =600
if Left.isPositive() and turn == True :
	rot = math.pi
	owner.turn = False
elif Right.isPositive() and turn == False :	
	rot = -math.pi
	owner.turn = True

#set movement Actuator
movement.setDRot(0,0,rot,0)
movement.setForce(0,0,jumpforce,0)
movement.setLinearVelocity(0,move,owner.getLinearVelocity()[2],1)


#Activate Actuator

GameLogic.addActiveActuator(movement,1)