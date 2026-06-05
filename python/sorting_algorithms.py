class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return (self.x < other.x and self.y < other.y)

class Map:
    def __init__(self, size = 5):
        self.map = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
    def set(self, pos: Vector, value):
        self.map[pos.x][pos.y] = value
        value.position = pos
    def remove(self, pos: Vector):
        self.map[pos.x][pos.y] = 0

game_map = Map()

class Player:
    global game_map
    def __init__(self, name):
        self.name = name
        self.spawn()
        self.position = Vector(None, None)
    def spawn(self):

        game_map.set((spawn_pos, spawn_pos), self)



if __name__ == '__main__':
    player = Player("Scape")
    print(player.name)