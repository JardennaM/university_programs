import pandas as pd
import numpy as np
import os
import networkx as nx

gate_coordinates = ['Circuits_1/gate_coordinates_18x13.csv', 'Circuits_2/gate_coordinates_18x17.csv']


# Gate_links are tuples of a gate num to another
# Gate_nums is a list of gate numbers
# Gate_coordinates is a dictionary with the gate_num as key 
# and a tuple of the coordinates
# dimenstions is a tuple of the dimentions of the board

class circuit_boards():
    def __init__(self, folder, netlist):
        self.netlist = netlist
        self.folder = folder 
        self.gates = self.parse_gates()
        self.gate_links = self.parse_links()
        self.board = self.board_init()
        
        # self.gates = gate_coordinates.keys
        # self.taken_nodes = 
        # self.taken_edges = 


    def parse_gates(self): 
        gate_coordinates = f'{self.folder}/gate_coordinates.csv'
        df = pd.read_csv(gate_coordinates, index_col=0, delimiter=',')
        self.gates = {}        
        for index, row in df.iterrows():
            self.gates[index] = (row['x'], row['y'])
        return self.gates

    def parse_links(self):
        gate_links = f'{self.folder}/{self.netlist}'
        df = pd.read_csv(gate_links, delimiter=',')
        self.links = {}
        for index, row in df.iterrows():
            self.links[index] = (row['1'], row['2'])
        return self.links
         
    def board_init(self):
        info = f'{self.folder}/info.csv'
        df = pd.read_csv(info, delimiter=',')
        dimensions = df.iloc[0]
        self.board = np.array([[0 for _ in range(dimensions['1'] + 1)] for _ in range(dimensions['0'] + 1)])
        for gate, coordinates in self.gates.items():
            self.board[coordinates[0]][coordinates[1]] = -1


    
    def __str__(self):
        # print("### Layer {} ###".format{})
        str_board = self.board
        for row in str_board:
            for column in row:
                if column == -1:
                    str_board[row][column] = 'GA'
                if column == 0:
                    str_board[row][column] = '__'
        
        for index, key, value in self.gate_links.items():
            gate_1 = self.gates[key]
            gate_2 = self.gates[value]
            postiion = gate_1
            while position != gate_2:
                x_direction_right = (position[0]+1, position[1])
                x_direction_left = (position[0]-1, position[1])
                y_direction_up = (position[0], position[1]-1)
                y_direction_down = (position[0], position[1]+1) 
                
            
            
            


            # x_direction = gate_1[0] - gate_2[0]
            # num = 0
            # for num in range(x_direction + 1):
            #     str_board[(gate_1[0])+ num][gate_1[1]] == index
            # y_direction = gate_1[1] - gate_2[1]
            
        

            print(str_board)    

    