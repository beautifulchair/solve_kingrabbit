from enum import Enum
import numpy as np


class MoveDirection(Enum):
    RIGHT = [0, 1]
    DOWN = [1, 0]
    LEFT = [0, -1]
    UP = [-1, 0]


class Object(Enum):
    EMPTY = 0
    RABBIT = 1
    BOX = 2
    # BOARD = 3
    WALL = 4

    def char(o):
        if o == Object.EMPTY:
            return " "
        elif o == Object.RABBIT:
            return "@"
        elif o == Object.BOX:
            return "$"
        # elif o == Object.BOARD:
        #     return "o"
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
        self.table = np.array(self.table)
        # ステージの高さと幅
        self.height = len(self.table)
        self.width = len(self.table[0])
        # rabbitの位置
        self.rabbit_position = None
        for r in range(self.height):
            for c in range(self.width):
                if self.table[r][c] == Object.RABBIT:
                    self.rabbit_position = np.array([r, c])

    def equal_to(self, stage):
        return np.array_equal(self.table, stage.table)

    def show(self):
        for row in self.table:
            for x in row:
                print(Object.char(x), end="")
            print()

    def get_object(self, position: np.ndarray):
        """
        ステージ外のpositionを指定した場合はNoneを返す
        """
        assert len(position) == 2
        if np.all(np.array([0, 0]) <= position) and np.all(
            position < np.array([self.height, self.width])
        ):
            return self.table[*position]
        else:
            return None

    def move_rabbit(self, move_direction: MoveDirection):
        """
        移動できる場合はTrue, できない場合はFalseを返す
        """
        next_position = self.rabbit_position + np.array(move_direction.value)
        next_next_position = next_position + np.array(move_direction.value)

        next_object = self.get_object(next_position)
        next_next_object = self.get_object(next_next_position)

        if next_object == Object.EMPTY:
            self.table[*self.rabbit_position] = Object.EMPTY
            self.table[*next_position] = Object.RABBIT
            self.rabbit_position = next_position
            return True
        elif next_object == Object.WALL:
            return False
        elif next_object == Object.BOX:
            if next_next_object in [Object.WALL, Object.BOX]:
                return False
            elif next_next_object in [Object.EMPTY]:
                self.table[*self.rabbit_position] = Object.EMPTY
                self.table[*next_position] = Object.RABBIT
                self.table[*next_next_position] = Object.BOX
                self.rabbit_position = next_position
                return True
            elif next_next_object in [None]:
                self.table[*self.rabbit_position] = Object.EMPTY
                self.table[*next_position] = Object.RABBIT
                self.rabbit_position = next_position
                return True
            else:
                raise AssertionError
        elif next_object == None:
            return False
        else:
            raise AssertionError


if __name__ == "__main__":
    stage = Stage("input/stage1.txt")
    stage.show()
