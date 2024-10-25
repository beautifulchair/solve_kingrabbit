from enum import Enum


class Object(Enum):
    EMPTY = 0
    RABBIT = 1
    BOX = 2
    BOARD = 3
    WALL = 4

    def char(o):
        if o == Object.EMPTY:
            return " "
        elif o == Object.RABBIT:
            return "@"
        elif o == Object.BOX:
            return "$"
        elif o == Object.BOARD:
            return "o"
        elif o == Object.WALL:
            return "#"
        else:
            return "?"


class Stage:
    def __init__(self, filepath):
        self.table = []
        with open(filepath) as f:
            for line in f:
                # 改行を除く
                line = line.replace("\n", "")
                self.table.append(list(map(lambda x: Object(int(x)), line)))

    def show(self):
        for row in self.table:
            for x in row:
                print(Object.char(x), end="")
            print()


if __name__ == "__main__":
    stage = Stage("input/stage1.txt")
    stage.show()
