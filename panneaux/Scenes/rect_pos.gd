extends TextureRect

func _get_drag_data(at_position: Vector2) :
	return texture
	
func _drop_data(at_position: Vector2, data: Variant) :
	texture=data
