POINTS = {
    "Plastic": 10,
    "Paper": 5,
    "Glass": 8,
    "Metal": 12,
    "Food Waste": 6,
    "E-Waste": 25,
    "Hazardous Waste": 20
}

def calculate_points(waste_type):
    return POINTS.get(waste_type, 0)
