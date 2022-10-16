
class car():
    def __init__(self, **kwargs):
        self.model = kwargs["model"]
        # get method allow us to pass without error of empty declaration. Use 'None' by default
        self.color = kwargs.get("color")
        self.speed = kwargs.get("speed")


def main():
    custom_car = car(model="Audi", color="red")
    print(custom_car.speed)

if __name__ == '__main__':
    main()