extends Control

var QCM = preload("res://Scenes/Panneaux/QCM.tscn")
var POS = preload("res://Scenes/Panneaux/POS.tscn")
var PANEL = preload("res://Scenes/Panneaux/PANEL.tscn")
var data_path = "res://Data/Data_ok.csv"

var file
var slides = []
var new_slide
var QUEUE = []

func _ready() -> void :
	#LOADING DATA
	print("Loading CSV file")
	file = get_file() # Get csv file from the editor or from the local folder if it's release mode
	print("")
	print("Loading CSV lines")
	slides = load_data(file) # Load the csv file as a list of dicts
	print("")
	
	#CREATING QUEUE
	print("Creating QUEUE")
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
		print("")
	#Charging the QUEUE itself in each scene
	for entry in QUEUE :
		entry.QUEUE=QUEUE
		
	#LAUNCHIN FIRST SCENE
	add_child(QUEUE[0])

func get_file() :
	if OS.has_feature("editor") :
		print("EDITOR MODE")
		file = FileAccess.open(data_path,FileAccess.READ)
	else :
		print("RELEASE MODE")
		var folder:= OS.get_executable_path().get_base_dir()
		print("Searching for LocalData.csv in game folder :")
		print(folder)
		var path_to_data=folder+"/LocalData.csv"
		file=FileAccess.open(path_to_data,FileAccess.READ)
	return file

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
	var to_return=POS.instantiate()
	to_return.id=id
	to_return.title=dict["titre"]
	to_return.card_pos = []
	to_return.card_text = []
	to_return.card_img = []
	for i in range(0,int(dict["nb"])) :
		to_return.card_pos.append(int(dict["C_pos_"+str(i)]))
		to_return.card_text.append(dict["C_texte_"+str(i)])
		to_return.card_img.append(dict["C_img_"+str(i)])
	return to_return
