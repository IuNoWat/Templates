extends Node2D

var img = "Fichier1.png"
var good_x=200
var text = "Default Text"

var dragging = false
var of = Vector2(0,0)

func _ready() -> void :
	creation()

func _process(delta: float) -> void:
	if dragging:
		position = get_global_mouse_position()-of
	

func creation() -> void :
	$info_text.text = text
	var path_img= "res://Assets/temp/"+img
	$Sprite2D.texture = load(path_img)

func _on_button_button_down() -> void:
	dragging=true
	of=get_global_mouse_position()-global_position

func _on_button_button_up() -> void:
	dragging=false
