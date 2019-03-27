from circuit_board import circuit_boards
import networkx as nx

def main():
    for circuit in ['Circuits_1', 'Circuits_2']:
        for netlist in ['netlist_1.csv', 'netlist_2.csv', 'netlist_3.csv']:
            board = circuit_boards(circuit, netlist)
            succesful_indices, failed_indices = [], []
            for key in board.links:
                ga1, ga2 = board.links[key] 
                try:
                    board.create_path(ga1, ga2)
                    succesful_indices.append(key)
                except nx.NetworkXNoPath:
                    failed_indices.append(key)
                    continue
            print(board)

if __name__ == '__main__':
    main()