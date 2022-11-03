
class User:
    def __init__(self, sex): # required value
        print("Create additional user...")
        self.sex = sex
        self.followers = 0 # default value
        self.following = 0 # default value


    def follow(self, user):
        user.followers += 1
        self.following += 1

def main():
    man = User(sex="m")
    print(type(man))
    man.id = "001" # custom value
    man.Name = "Tommy"  # custom value

    print(man.Name)

    girl = User(sex="w")

    girl.id = "007"  # custom value
    girl.username = "Anna"  # custom value
    # girl.sex = "w"
    print(girl.sex)
    girl.follow(man)
    print(girl.followers)
    print(girl.following)



if __name__ == '__main__':
    main()