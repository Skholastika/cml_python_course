import random as rnd


class Apple:
    ID = 0
    stages = ['bloom', 'green', 'red']

    def __init__(self, index: int, stage: str = stages[0]):
        # if type(self) is Apple:
        self.ID = index
        self.stage = stage
        self.age = stage.index(self.stage)
        print(f"{self.ID}: stage '{self.stage}'")

    def maturation(self):
        self.age += 1
        stg_index = Apple.stages.index(self.stage)
        if stg_index < len(Apple.stages) - 1:
            self.stage = Apple.stages[stg_index + 1]
            print(f"{self.ID}: new stage is '{self.stage}'")

    def is_red(self):
        if self.stage == 'red':
            return True
        else:
            return False


class Tree:

    def __init__(self, *args: Apple, age=1):
        # if type(self) is Tree:
        self.age = age
        self.apples = []
        if 2 < self.age < 10:
            for arg in args:
                if type(arg) is Apple:
                    self.apples.append(arg)
        else:
            print("Tree can't have apples.")

    def grow(self):
        self.age += 1
        if self.age >= 10:
            for apple in self.apples:
                del apple
        elif self.age > 2:
            for apple in self.apples:
                if apple.age < 5:
                    apple.maturation()
                else:
                    del self.apples[self.apples.index(apple)]
                    del apple

            if rnd.randint(0, 1) and 2 < self.age < 5:
                for i in range(rnd.randint(0, 5)):
                    new_apple = Apple(len(self.apples))
                    self.apples.append(new_apple)

    def all_red(self):
        for apple in self.apples:
            if not apple.is_red():
                return False
        return True

    def harvest(self):
        for apple in self.apples:
            if apple.is_red():
                del self.apples[self.apples.index(apple)]
                del apple  # ???????
        print('No more red apples on this tree.')


class Gardener:

    def __init__(self, name, *args: Tree):
        self.name = name
        print(f'Hi! My name is {self.name}. I am a gardener.')
        self.trees = list(args)

    def care(self):
        for tree in self.trees:
            tree.grow()

    def harvest(self):
        # for tree in self.trees:
        # if not tree.all_red():
        #     print("I can't harvest.")
        #     return
        for tree in self.trees:
            tree.harvest()
        print('The harvest has been collected.')

    def garden_info(self):
        print(f"Trees: {len(self.trees)}")
        for tree in self.trees:
            print(f"Tree {self.trees.index(tree)}: {len(tree.apples)} apple(s).")
            for apple in tree.apples:
                print(f"Apple {apple.ID} - {apple.stage}")


t = Tree(Apple(1, 'red'),
         Apple(2, 'green'),
         Apple(3, 'bloom'),
         Apple(4),
         Apple(5), age=4
         )
g = Gardener('Anna', t)
g.care()
g.care()
g.garden_info()
g.harvest()
g.care()
g.care()
g.care()
g.care()
g.care()
g.care()
g.care()
g.garden_info()
g.harvest()

