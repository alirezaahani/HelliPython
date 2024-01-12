nowruz_grade = int(input())
vacation_days = int(input())

if vacation_days == 0:
    nowruz_grade = 20
elif vacation_days != 7:
    nowruz_grade -= vacation_days
    nowruz_grade = 0 if nowruz_grade < 0 else nowruz_grade # Assusre that negetvie grade doesn't exist

print(nowruz_grade)
