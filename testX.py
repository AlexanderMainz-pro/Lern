def road_display(z):
    if z < 2:
        return "No roads displayed"
    elif 2 <= z < 5:
        return "Roads fk=1 displayed (normal), Roads fk=7 displayed (pink)"
    elif 5 <= z < 8:
        return "Roads fk=1 displayed (purple), Roads fk=7 displayed (pink)"
    elif 8 <= z < 9:
        return "Roads fk=1 displayed (yellow), Roads fk=7 displayed (pink)"
    elif 9 <= z < 12:
        return "Roads fk=1 displayed (green), Roads fk=7 displayed (pink)"
    elif 12 <= z < 15:
        return "Roads fk=1 displayed (green, bold outline), Roads fk=9 displayed"
    else:  # z ≥ 15
        return "Roads fk=1 displayed (green, bold outline, translucent), Roads fk=9 displayed"

# Тестирование
test_values = [-1, 0, 2, 4, 5, 8, 9, 12, 15, 20]
for z in test_values:
    print(f"z={z}: {road_display(z)}")