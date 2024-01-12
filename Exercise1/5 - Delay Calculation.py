s = input().split()

a = int(s[0])
b = int(s[1])
l = int(s[2])

number_of_a = (l // 2) + l % 2
number_of_b = (l // 2)

time_elapsed = number_of_a * a + number_of_b * b

print(time_elapsed)
