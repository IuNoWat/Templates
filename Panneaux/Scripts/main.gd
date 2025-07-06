extends Control

var QCM = preload("res://Scenes/Panneaux/QCM.tscn")
var POS = preload("res://Scenes/Panneaux/POS.tscn")
var PANEL = preload("res://Scenes/Panneaux/PANEL.tscn")

var QUEUE = []

func _ready() -> void :
	for i in range(0,10) :
		QUEUE.append(QCM.instantiate())
		QUEUE[i].id = i
		QUEUE[i].title = "QCM"
	for i in range(0,10) :
		QUEUE[i].QUEUE=QUEUE
		#add_child(QUEUE[i])
	add_child(QUEUE[0])
	#hide()
