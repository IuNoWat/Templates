extends Control

var QCM = preload("res://Scenes/Panneaux/QCM.tscn")
var POS = preload("res://Scenes/Panneaux/POS.tscn")
var PANEL = preload("res://Scenes/Panneaux/PANEL.tscn")

var data_path = "res://Data/TestData.csv"
var file = FileAccess.open(data_path,FileAccess.READ)
var slides = []
var new_slide

var QUEUE = []

func _ready() -> void :
	slides = load_data(file)
	var count = 0
	for dict in slides :
		match dict["type"] :
			"QCM" :
				new_slide=QCM_constructor(dict,count)
			"PANEL" :
				new_slide=PANEL_constructor(dict,count)
			"POS" :
				new_slide=POS_constructor(dict,count)
		QUEUE.append(new_slide)
		count+=1
	print(QUEUE)
	#for i in range(0,10) :
		#QUEUE.append(QCM.instantiate())
		#QUEUE[i].id = i
		#QUEUE[i].title = "QCM"
	for entry in QUEUE :
		entry.QUEUE=QUEUE
	add_child(QUEUE[0])

func load_data(file) :
	while !file.eof_reached() :
		var csv_line=file.get_csv_line(";")
		print(csv_line)
		if str(csv_line[0])!="" :
			if csv_line[0]=="ID" :
				pass
			else :
				if int(csv_line[0])==len(slides) :
					slides.append({csv_line[1]:csv_line[2]})
				else :
					slides[int(csv_line[0])][csv_line[1]] = csv_line[2]
	print(slides)
	return slides

func QCM_constructor(dict,id) :
	print("Constructing QCM Panel with values :")
	print(dict)
	var to_return=QCM.instantiate()
	to_return.id=id
	to_return.title=dict["titre"]
	to_return.answers=[]
	for i in range(0,int(dict["nb"])) :
		to_return.answers.append(dict["Q_texte_"+str(i)])
	to_return.good=int(dict["win"])
	return to_return

func PANEL_constructor(dict,id) :
	print("Constructing PANEL Panel with values :")
	print(dict)
	var to_return=PANEL.instantiate()
	to_return.id=id
	to_return.title=dict["titre"]
	to_return.text=dict["texte"]
	return to_return

func POS_constructor(dict,id) :
	print("Constructing POS Panel with values :")
	print(dict)
	return "POS"
