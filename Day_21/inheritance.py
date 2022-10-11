class Animal:
    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# Inherite the Animal class
class Fish(Animal):
    def __init__(self):
        # Inherite the Animal class
        super().__init__()

    # modify the method from parent class with the functionality inheritance
    def breathe(self):
        # keep entire method functionality from Animal.breathe()
        super().breathe()
        # add new functionality for Fish.breathe()
        print("Doing it under water...")

    def swim(self):
        print("Swimming in water.")

def main():
    roach = Fish()
    roach.swim()
    roach.breathe()
    print(roach.number_of_eyes)


if __name__ == '__main__':
    main()