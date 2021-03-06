import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        if kwargs:
            for k, v in kwargs.items():
                for i in range(v):
                    self.contents.append(k)
        else:
            self.contents.append("colorless")

    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        else:
            balls = []

            # random.choice()
            for i in range(n):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                balls.append(ball)

            # one shuffle
            # random.shuffle(self.contents)
            # for i in range(n):
            #     balls.append(self.contents.pop())

            # many shuffles
            # for i in range(n):
            #     random.shuffle(self.contents)
            #     balls.append(self.contents.pop())

        return balls


def contents_to_dict(contents):
    dict = {}

    for ball in contents:
        # Catch key error.
        # try:
        #     dict[ball] = dict[ball] + 1
        # except KeyError:
        #     dict[ball] = 1

        # Use the ``in`` operator.
        if ball in dict:
            dict[ball] = dict[ball] + 1
        else:
            dict[ball] = 1

        # Use the ``.get()`` method.
        # val = dict.get(ball, None)
        # if val is None:
        #     dict[ball] = 1
        # else:
        #     dict[ball] = dict[ball] + 1

    return dict


def good_draw_p(draw, goal):
    for k, v in goal.items():
        # Catch the KeyError.
        # try:
        #     draw[k]
        # except KeyError:
        #     return False
        # if draw[k] < v:
        #     return False

        # Use the ``in`` operator.
        # if k in draw:
        #     if draw[k] < v:
        #         return False
        # else:
        #     return False

        # Use the ``.get()`` method.
        dv = draw.get(k, None)
        if dv is None:
            return False
        elif dv < v:
            return False

    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    good = 0

    for i in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        if good_draw_p(
            contents_to_dict(test_hat.draw(num_balls_drawn)), expected_balls
        ):
            good += 1

    return good / num_experiments
