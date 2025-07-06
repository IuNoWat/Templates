extends Control

var id = 0
var title = "Default Title"
var text = "Default text"
var QUEUE

func _ready() -> void:
	print("PANEL alive with id : "+str(id))

func _process(delta: float) -> void :
	get_node("Titre").text=title+" n°"+str(id)
	get_node("Texte").text=text

func _on_button_pressed() -> void:
	print("Here is next scene :")
	print(QUEUE[id+1])
	add_child(QUEUE[id+1])
	pass # Replace with function body.
