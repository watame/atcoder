# B - Battle
t_hp, t_attack, a_hp, a_attack = map(int, input().split())

while True:
    a_hp -= t_attack
    if a_hp <= 0:
        print("Yes")
        exit()
    t_hp -= a_attack
    if t_hp <= 0:
        print("No")
        exit()
