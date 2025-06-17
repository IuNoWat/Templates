extends Control

var card = load("res://Scenes/card_pos.tscn")
var cards = [card.instantiate(),card.instantiate(),card.instantiate()]
var total_dist=0

func _ready() -> void:
	start_game()

func start_game() -> void :
	for i in range(0,3) :
		cards[i].transform.origin=Vector2(200+i*200,200+i*200)
		add_child(cards[i])
		cards[i].good_x=100+i*600

func _on_button_button_up() -> void:
	print_debug("Button has been clicked")
	var cards = get_tree().get_nodes_in_group("cards")
	var last_tween
	for instance in cards :
		total_dist+=abs(instance.transform.origin.x-instance.good_x)
		var tween=get_tree().create_tween()
		tween.tween_property(instance,"position",Vector2(instance.good_x,instance.transform.origin.y),1).set_ease(Tween.EASE_OUT)
		last_tween=tween
	await last_tween.finished
	print_debug("TWEEN FINISHED")
	print_debug("Distance totale : "+str(total_dist))
	total_dist=0
	
	
	#print_debug($card_pos.good_x)
	#print_debug($card_pos.transform.origin)
	#var meh = Vector2(200,$card_pos.transform.origin.y)
	#var tween=get_tree().create_tween()
	#tween.tween_property($card_pos,"position",meh,0.5).set_ease(Tween.EASE_OUT)
	
	
