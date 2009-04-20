import GameLogic, math

cont = GameLogic.getCurrentController()
owner = cont.getOwner()

#getState 
State = owner.getState()

#Get Sensors
Init = owner.getSensor('Init')
G = owner.getSensor('G')
bubblepop = owner.getSensor('bubblepop')
gumCount = owner.getSensor('gumCount')

#Get Actuators
visible = cont.getActuator('SetVisibility')
SetJump = cont.getActuator('SetJump')

if(Init.isPositive()) :
	visibile.setVisible(0)

elif(G.isPositive() and gumCount.isPositive() and owner.blowBubble == False) :
	visible.setVisible(1)
 	owner.blowbubble = True
elif(bubblepop.isPositive() and owner.blowbubble = True) :
	visible.setVisible(1)
	owner.blowbubble = False
	SetJump.setProp(gumjump)
	SetJump.setValue(False)
