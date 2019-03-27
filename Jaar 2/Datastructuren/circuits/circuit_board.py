import pandas as pd
import numpy as np
import os
import networkx as nx
from networkx.algorithms.shortest_paths.astar import astar_path

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
        self.wire_index = 1
        self.info()
        self.parse_gates()
        self.parse_links()
        self.board_init()
        self.update_nodes()

    def info(self):
        info = f'{self.folder}/info.csv'
        df = pd.read_csv(info, delimiter=',')
        self.xdim = df.iloc[0][0]
        self.ydim = df.iloc[0][1]

    def parse_gates(self): 
        gate_coordinates = f'{self.folder}/gate_coordinates.csv'
        df = pd.read_csv(gate_coordinates, index_col=0, delimiter=',')
        self.gates = {}        
        for index, row in df.iterrows():
            self.gates[index] = (row['x'], row['y'])

    def parse_links(self):
        gate_links = f'{self.folder}/{self.netlist}'
        df = pd.read_csv(gate_links, delimiter=',')
        self.links = {}
        for index, row in df.iterrows():
            self.links[index] = (row['1'], row['2'])

    def board_init(self):
        self.graph = nx.Graph()
        for z in range(7):
            for y in range(self.ydim):
                for x in range(self.xdim):
                    self.graph.add_node((x, y, z), repr='__')
        for gate in self.gates:
            coords = self.gates[gate]
            self.graph.node[coords + (0,)]['repr'] = 'GA'

    def neighbours(self, x, y, z):
        neighbours = [(x+1, y, z), (x, y+1, z), (x, y, z+1), 
                      (x-1, y, z), (x, y-1, z), (x, y, z-1)]
        cor_neighbours = []
        for neighbour in neighbours:
            if neighbour[0] >= self.xdim or neighbour[0] < 0:
                continue
            if neighbour[1] >= self.ydim or neighbour[1] < 0:
                continue
            if neighbour[2] >= 7 or neighbour[2] < 0:
                continue
            if self.graph.node[neighbour]['repr'] is not '__': 
                continue
            # if self.graph.node[(x, y, z)]['repr'] is 'GA':
            #     if self.graph.node[(neighbour[0], neighbour[1], neighbour[2])]['repr'] is 'GA':
            #         cor_neighbours.append(neighbour)
            else:
                cor_neighbours.append(neighbour)
        return cor_neighbours
        
    def clear_edge(self, tile):
        for edge in list(self.graph.edges(tile)):
            self.graph.remove_edge(*edge)

    def update_nodes(self):
        for z in range(7):
            for y in range(self.ydim):
                for x in range(self.xdim):
                    node = (x,y,z)
                    self.clear_edge(node)
                    neighbours = self.neighbours(*node)
                    for neighbour in neighbours:
                        self.graph.add_edge(node, neighbour)
    

    def create_path(self, gate_1, gate_2):
        gate_1 = self.gates[gate_1] + (0,)
        gate_2 = self.gates[gate_2] + (0,)
        path = nx.astar_path(self.graph, gate_1, gate_2)
        for tile in path[1:len(path) -1]:
            self.graph.node[tile]['repr'] = '{0:0=2d}'.format(self.wire_index)    
        self.update_nodes()
        self.wire_index += 1
        return path
    
    def __str__(self):
        string = ''
        for z in range(7):
            string += f'### Layer {z + 1} ###\n'
            for y in range(self.ydim):
                for x in range(self.xdim):
                    node = (x, y, z)
                    string += f'{self.graph.node[node]["repr"]}'
                    string += ' '
                string += '\n'
            string += '\n'
        return string
    
        
