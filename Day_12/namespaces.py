
game_level = 0

def create_enemy():
    enemies = ["Skeleton", "zombie", "Ghost"]
    if game_level < 5:
        new_enemy = enemies[0]

    for i in enemies:
        last = i

    print(new_enemy)
    print(last)

def main():
    create_enemy()
    # if i < 5:
    #     new_var += i
    #     i += 1
    # print(new_var)



if __name__ == '__main__':
    main()