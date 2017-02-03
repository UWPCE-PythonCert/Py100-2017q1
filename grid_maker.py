
import sys

class Grid_Maker:
    """
    Create a user defined grid with error check
    Returns a formatted string
    Parameters are:
    - s (side character of grid)
    - t (top character of grid)
    - c (corner character of grid)
    - h (number of side characters)
    - w (number of top characters)
    - b (number of boxes)
    """
    # Initialize
    def __init__(self, s = '|', t = '-', c = '+', h = 5, w = 5, b = 2):
        self.s = s
        self.t = t
        self.c = c
        self.h = h
        self.w = w
        self.b = b
    # Create grid
    def draw_grid(self):
        """
        Creates a user defined grid
        """
        try:
            if self.b == 1:
                # Single box
                v1 = self.c + (self.t * self.w) + self.c + "\n"
                v2 = self.s + (" " * self.w) + self.s + "\n"
                return v1 + (v2 * self.h) + v1[:-1]
            else:
                # Left corner + top
                v1 = self.c + (self.t * self.w)
                # Left side + middle
                v2 = self.s + (" " * self.w)
                # Create string representing grid
                v3 = (v1 * self.b) + self.c + "\n"
                for x in range(self.h):
                    v3 = v3 + (v2 * self.b) + self.s + "\n"
                # Return string
                return (v3 * self.b) + (self.b * v1) + self.c
        except:
            return "Please check arguments.\nThey must be 3 single characters & 3 integers."
            
if __name__ == "__main__":
    gm = Grid_Maker()
    print(gm.draw_grid())