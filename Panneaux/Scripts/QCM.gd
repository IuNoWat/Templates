extends Control

#Core variables
var btns = []
@onready var button = $Button
@onready var msg_button = $msg/msg_button
@onready var msg_rect = $msg/ColorRect
@onready var msg_title = $msg/msg_title
@onready var msg_text = $msg/msg_text

#Default values
var id = 0
var title = "Default Title"
var answers = ["BOUTON 1","BOUTON 2","BOUTON 3"]
var answers_text = ["meh 1","meh 2","meh 3"]
var good = 2
var QUEUE

func _ready() -> void :
	print("QCM ready with id : "+str(id))
	print("Creating Buttons")
	create()
	print("")
	pass

func _process(delta: float) -> void :
	get_node("Titre").text=title

func create() -> void :
	for i in range(0,len(answers)) :
		btns.append(button.duplicate())
		btns[i].text=answers[i]
		btns[i].position=Vector2(-800+i*500,-400)
		add_child(btns[i])
	button.free()

func _on_button_pressed() -> void:
	var pressed_button = check_pressed_button() #Check wich button has been pressed
	#Hide all buttons
	for btn in btns :
		btn.visible=false
	#Check for win or loose and show corresponfing message from Data
	if pressed_button==good :
		msg_title.text="Gagné !"
		msg_rect.color=Color("GREEN")
	else :
		msg_title.text="Perdu !"
		msg_rect.color=Color("RED")
	msg_text.text=answers_text[pressed_button] 
	get_node("msg").visible=true

func check_pressed_button() -> int :
	for i in range(0,len(btns)) :
		if btns[i].is_pressed() :
			return i
	return 0

func _on_msg_button_pressed() -> void:
	print("Button pressed, going to scene n°"+str(id+1))
	print("")
	if len(QUEUE)==id+1 :
		get_tree().reload_current_scene()
	else :
		add_child(QUEUE[id+1])
