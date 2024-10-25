_empty = 0
_rabbit = 1
_box = 2
_board = 3
_wall = 4


class Object:
    def __init__(self, v):
        self.v = v
        self.c = Object.char(self.v)

    def char(v):
        if v == _empty:
            return " "
        elif v == _rabbit:
            return "@"
        elif v == _box:
            return "$"
        elif v == _board:
            return "o"
        elif v == _wall:
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
                print(x.c, end="")
            print()


if __name__ == "__main__":
    stage = Stage("input/stage1.txt")
    stage.show()
