extends Control

#Default Values
var id = 0
var title = "Default Title"
var text = "Default text"
var QUEUE

func _ready() -> void:
	print("PANEL ready with id : "+str(id))
	print("")

func _process(delta: float) -> void :
	get_node("Titre").text=title
	get_node("Texte").text=text

func _on_button_pressed() -> void:
	print("Button pressed, going to scene n°"+str(id+1))
	print("")
	if len(QUEUE)==id+1 :
		get_tree().reload_current_scene()
	else :
		add_child(QUEUE[id+1])
	pass
