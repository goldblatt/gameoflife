#! /usr/bin/env python3

class GameOfLife():
    def run(self, input):
        parsed_input = self.parse(input)
        print(self.to_string(parsed_input))
    
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


if __name__ == "__main__":
    GameOfLife().run()
