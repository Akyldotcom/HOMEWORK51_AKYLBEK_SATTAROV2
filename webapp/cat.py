CAT_PHOTO_PATH_1 = "cat1.jpg"
CAT_PHOTO_PATH_2 = "cat2.jpg"


class Cat:
    name = ""
    age = 1
    is_sleeping = False
    satiety = 40
    happiness = 40
    avatar = CAT_PHOTO_PATH_1

    @classmethod
    def get_avatar(cls):
        if cls.happiness > 50:
            cls.avatar = CAT_PHOTO_PATH_2
        else:
            cls.avatar = CAT_PHOTO_PATH_1

    @classmethod
    def play(cls):
        cls.happiness += 15
        cls.satiety -= 10
        cls.get_avatar()

    @classmethod
    def food(cls):
        cls.satiety += 15
        cls.happiness -= 5
        cls.get_avatar()



