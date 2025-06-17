extends Control

var card = load("res://Scenes/card_pos.tscn")


func _ready() -> void:
	for i in range(0,3) :
		var inst=card.instantiate()
		inst.transform.origin=Vector2(200+i*200,200+i*200)
		add_child(inst)
		inst.good_x=100+i*600

func _on_button_button_up() -> void:
	print_debug("Button has been clicked")
	var cards = get_tree().get_nodes_in_group("cards")
	for instance in cards :
		var tween=get_tree().create_tween()
		tween.tween_property(instance,"position",Vector2(instance.good_x,instance.transform.origin.y),1).set_ease(Tween.EASE_OUT)
	#print_debug($card_pos.good_x)
	#print_debug($card_pos.transform.origin)
	#var meh = Vector2(200,$card_pos.transform.origin.y)
	#var tween=get_tree().create_tween()
	#tween.tween_property($card_pos,"position",meh,0.5).set_ease(Tween.EASE_OUT)
	
	
