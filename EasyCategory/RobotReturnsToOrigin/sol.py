class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #simple check, we can easily just count instances of R, L, U, D if R - L = 0 and U - D = 0, we can say it ends up at the origin

        #thats boring, lets do something funny
        
        #we make a 2d map, real plane for R L , imaginary for U D (the imaginary part is solely to isolate vertical moves)
        #completely impractical, slow and uses more memory than usual
        
        dir_map = {"R": 1, "L":-1, "U": 1j, "D": -1j}
        #then we just use sum, with the map
        return sum(dir_map[m] for m in moves) == 0
