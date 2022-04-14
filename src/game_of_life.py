#! /usr/bin/env python3

class GameOfLife():
    def run(self, input):
        cells_array = self.parse(input)

        return_array = []

        for cell_pair in cells_array:
            neighbors = self.get_neighbors(cell_pair)
            count = 0

            for neighbor in neighbors:
                if (self.get_status(cells_array, neighbor)):
                    count += 1
            
            if (count >= 2 and count <= 3):
                return_array.append(cell_pair)


        print(self.to_string(return_array))
    
    def to_string(self, cells_array):
        output_string = ""
        for cell in cells_array:
            output_string += str(cell[0]) + "," + str(cell[1]) + " "
        return output_string.strip()
    
    def parse(self, input):
        pairs = input.split(" ")
        cells_array = []
        for pair in pairs:
            split_pair = pair.split(",")
            cells_array.append([int(split_pair[0]), int(split_pair[1])])
        return cells_array

    def get_neighbors(self, cell_pair):
        neighbors = []
        x = cell_pair[0]
        y = cell_pair[1]
        neighbors.append([x, y + 1])
        neighbors.append([x + 1, y + 1])
        neighbors.append([x + 1, y])
        neighbors.append([x + 1, y - 1])
        neighbors.append([x, y - 1])
        neighbors.append([x - 1, y - 1])
        neighbors.append([x - 1, y])
        neighbors.append([x - 1, y + 1])

        return neighbors

    def get_status(self, cells_array, cell_pair):
        return cell_pair in cells_array

if __name__ == "__main__":
    GameOfLife().run()
