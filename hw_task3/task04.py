class Apple:
    _ID = 0
    stages = ['bloom', 'green', 'red']

    def __init__(self, index: int, stage: str = stages[0]):
        if type(self) is Apple:
            self._ID = index
            self.stage = stage
            print(f"{self._ID}: stage '{self.stage}'")

    def maturation(self):
        stg_index = Apple.stages.index(self.stage)
        if stg_index < len(Apple.stages) - 1:
            self.stage = Apple.stages[stg_index + 1]
            print(f"{self._ID}: new stage is '{self.stage}'")

    def is_red(self):
        if self.stage == 'red':
            return True
        else:
            return False


class Tree:

    def __init__(self, *args: Apple):
        if type(self) is Tree:
            self.apples = []
            for arg in args:
                if type(arg) is Apple:
                    self.apples.append(arg)

    def grow(self):
        for apple in self.apples:
            apple.maturation()

    def all_red(self):
        for apple in self.apples:
            if not apple.is_red():
                return False
        return True

    def harvest(self):
        self.apples = []  # ???????
        print('No more apples on this tree.')


class Gardener:

    def __init__(self, name, *args: Tree):
        self.name = name
        print(f'Hi! My name is {self.name}. I am a gardener.')
        self.trees = list(args)

    def care(self):
        for tree in self.trees:
            tree.grow()

    def harvest(self):
        for tree in self.trees:
            if not tree.all_red():
                print("I can't harvest.")
                return
        for tree in self.trees:
            tree.harvest()
        print('The harvest has been collected.')


t = Tree(Apple(1, 'red'),
         Apple(2, 'green'),
         Apple(3, 'bloom'),
         Apple(4),
         Apple(5)
         )
g = Gardener('Anna', t)
g.care()
g.harvest()
g.care()
g.harvest()




