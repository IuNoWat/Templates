extends Control

var id = 0
var title = "Default Title"
var answers = ["BOUTON 1","BOUTON 2","BOUTON 3"]
var answers_text = ["meh 1","meh 2","meh 3"]
var btns = []
var good = 2
var QUEUE



@onready var button = $Button
@onready var win_button = $msg_win/win_button
@onready var win_text = $msg_win/text
@onready var loose_button = $msg_loose/loose_button
@onready var loose_text = $msg_loose/text

func _ready() -> void :
	create()
	pass

func _process(delta: float) -> void :
	get_node("Titre").text=title

func create() -> void :
	for i in range(0,len(answers)) :
		btns.append(button.duplicate())
		btns[i].id=i
		btns[i].text=answers[i]
		btns[i].position=Vector2(-800+i*500,-400)
		add_child(btns[i])
	button.free()

func _on_button_pressed() -> void:
	var response = check_pressed_button()
	for btn in btns :
		btn.visible=false
	if response==good :
		win_text=answers_text[good]
		get_node("msg_win").visible=true
	else :
		get_node("msg_loose").visible=true
	pass # Replace with function body.

func check_pressed_button() -> int :
	for i in range(0,len(btns)) :
		print("Button "+str(i)+" is pressed : "+str(btns[i].is_pressed()))
		if btns[i].is_pressed() :
			return i
	return 0

func _on_loose_button_pressed() -> void:
	add_child(QUEUE[id+1])
	pass # Replace with function body.

func _on_win_button_pressed() -> void:
	add_child(QUEUE[id+1])
	pass # Replace with function body.
