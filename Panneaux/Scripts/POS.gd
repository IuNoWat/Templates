extends Control

#Core variables
var card = load("res://Scenes/card_pos.tscn")
var QUEUE
var total_dist=0
var checked=false
@onready var finish_button = $VBoxContainer/Control/Button

#Default values
var id = 0
var title = "Default Title"
var card_pos = [200,700,1300]
var card_text = ["meh 1","meh 2","meh 3"]
var card_img = ["Fichier1.png","Fichier1.png","Fichier1.png"]
var cards = [card.instantiate(),card.instantiate(),card.instantiate()]

func _ready() -> void:
	print("POS ready with id : "+str(id))
	print("Creating Cards")
	create()
	print("")

func create() -> void :
	cards = []
	for i in range(0,len(card_pos)) :
		cards.append(card.instantiate())
		cards[i].text=card_text[i]
		cards[i].img=card_img[i]
		cards[i].good_x=card_pos[i]
		cards[i].position=Vector2(500*i,500*i)
		add_child(cards[i])

func _on_button_button_up() -> void:
	#Check if button clicked is for verification or for next scene
	if checked==false :
		var cards = get_tree().get_nodes_in_group("cards")
		#Animate re-positionning of cards with tweens
		var last_tween
		for instance in cards :
			total_dist+=abs(instance.transform.origin.x-instance.good_x)
			var tween=get_tree().create_tween()
			tween.tween_property(instance,"position",Vector2(instance.good_x,instance.transform.origin.y),1).set_ease(Tween.EASE_OUT)
			last_tween=tween
		await last_tween.finished
		#Show information texts from Data
		for card in cards :
			card.get_node("info_text").visible=true
		#Change button for next scene
		finish_button.text = "SUIVANT"
		checked=true
	else :
		print("Button pressed, going to scene n°"+str(id+1))
		print("")
		if len(QUEUE)==id+1 :
			get_tree().reload_current_scene()
		else :
			add_child(QUEUE[id+1])
	
	
