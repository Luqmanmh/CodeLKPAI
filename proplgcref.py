from utils import *
from logic import *

kb_wumpus = PropKB()

# simbol
P = {}  # Pit
B = {}  # Breeze
W = {}  # Wumpus
S = {}  # Stench
G = {}  # Gold

# simbol per cell
for x in range(1, 5):
    for y in range(1, 5):
        P[x, y] = Symbol(f"P[{x},{y}]")
        B[x, y] = Symbol(f"B[{x},{y}]")
        W[x, y] = Symbol(f"W[{x},{y}]")
        S[x, y] = Symbol(f"S[{x},{y}]")
        G[x, y] = Symbol(f"G[{x},{y}]")

# buat kb
# Pits
kb_wumpus.tell(~P[1, 1])
kb_wumpus.tell(P[1, 3])
kb_wumpus.tell(P[3, 3])
kb_wumpus.tell(P[4, 4])

# Wumpus
kb_wumpus.tell(W[3, 1])
kb_wumpus.tell(~W[1, 1])

# Gold
kb_wumpus.tell(G[3, 2])

# Breeze
kb_wumpus.tell(B[2, 1])
kb_wumpus.tell(B[2, 3])
kb_wumpus.tell(B[3, 2])
kb_wumpus.tell(B[3, 4])
kb_wumpus.tell(B[4, 1])
kb_wumpus.tell(B[4, 3])

# Stenche
kb_wumpus.tell(S[1, 2])
kb_wumpus.tell(S[1, 4])
kb_wumpus.tell(S[2, 3])

# Logic breze & stench
kb_wumpus.tell(equiv(B[2, 1], (P[1,1] | P[2,2] | P[3,1])))
kb_wumpus.tell(equiv(B[4, 1], (P[4,2] | P[3,1])))
kb_wumpus.tell(equiv(B[3, 2], (P[4,2] | P[2,2] | P[3,1] | P[3,3])))
kb_wumpus.tell(equiv(B[2, 3], (P[1,3] | P[2,2] | P[3,3] | P[2,4])))
kb_wumpus.tell(equiv(B[3, 4], (P[2,4] | P[4,4] | P[3,3])))
kb_wumpus.tell(equiv(B[4, 3], (P[4,2] | P[4,4] | P[3,3])))

kb_wumpus.tell(equiv(S[1, 2], (W[1,3] | W[2,2] | W[1,1])))
kb_wumpus.tell(equiv(S[2, 3], (W[1,3] | W[2,2] | W[2,4] | W[3,3])))
kb_wumpus.tell(equiv(S[1, 4], (W[1,3] | W[2,4])))

#class wumpus untuk travel
class wumpusag:
    def __init__(self, kb):
        self.kb = kb
        self.current_position = (1, 1)
        self.visited = [(1, 1)]
        self.deadnode = [[1, 1]]
        self.has_gold = False

    # menentukan jika sebuah node adjacent aman
    def safe_ch(self, x, y):
        return not self.kb.ask_if_true(P[x, y]) and not self.kb.ask_if_true(W[x, y])

    # pindah ke node selanjutnya
    def move_to(self, x, y):
        if self.safe_ch(x, y):
            self.current_position = (x, y)
            print(f"mov to {x}, {y}")
            if (x, y) not in self.visited:
                self.visited.append((x, y))
            return True
        else:
            return False

    #menentukan semua node adj yang aman
    def safe_adj(self):
        x, y = self.current_position
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 1 <= new_x <= 4 and 1 <= new_y <= 4 and (new_x, new_y) not in self.visited and self.safe_ch(new_x, new_y) and (new_x, new_y) not in self.deadnode:
                return new_x, new_y
        return None

    # fungsi utama menemukan gold
    def find_g(self):
        steps = []
        gold = []

        while True:
            x, y = self.current_position
            steps.append(self.current_position)

            if self.kb.ask_if_true(G[x, y]):
                self.has_gold = True
                gold.append([x, y])
                break 

            next = self.safe_adj()
            if next:
                n_x, n_y = next
                self.move_to(n_x, n_y)
            elif self.visited:
                self.deadnode.append(self.visited[-1])
                self.visited.pop()
                if self.visited:
                    tr_x, tr_y = self.visited[-1]
                    self.move_to(tr_x, tr_y)
                else:
                    print("out of moves")
                    break
            else:
                print("out of moves")
                break

        return gold, self.visited

wumpy = wumpusag(kb_wumpus)
print("Steps to find the gold:")
gold_coor, gold_steps = wumpy.find_g()
print(f"gold found in {gold_coor}")

print("steps to escape:")
for step in reversed(gold_steps):
    print(step)