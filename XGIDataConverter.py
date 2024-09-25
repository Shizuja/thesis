import xgi
import sys

def export_xgi_data_hypergraph_to_txt(hypergraph, file_name):
    """
    Export the hypergraph data to a .txt file in the desired format.
    The first line contains the number of nodes, each subsequent line contains
    the nodes of one hyperedge, each separated by a space.
    
    Input:
        hypergraph (xgi.Hypergraph):    The input hypergraph object.
        file_name (string):             The name of the output file.
    """
        # Get the list of nodes and create a mapping from original node labels to 0-based labels
    original_nodes = list(hypergraph.nodes)
    node_mapping = {node: i for i, node in enumerate(original_nodes)}

    with open(file_name, "w") as file:
        # Write the number of nodes in the first line
        file.write(f"{len(hypergraph.nodes)}")
        
        # Write each hyperedge in a new line with nodes mapped to 0-based labels
        for edge in hypergraph.edges.members():
            mapped_edge = [str(node_mapping[node]) for node in edge]
            file.write("\n" + " ".join(mapped_edge))
        file.close()
        
        

# main method
if __name__ == "__main__":
    #load the hypergraph data if a valid set was given
    try:
        hypergraph = xgi.load_xgi_data(sys.argv[1])
    except:
        raise ValueError("Please provide a valid xgi data set name as argv1, e.g. plant-pollinator-mpl-049")
    
    #put it into a file and notify the user if he did not choose a name for it
    try:
        export_xgi_data_hypergraph_to_txt(hypergraph, sys.argv[2]+".hypergraph")
    except:
        print("No name for output file was chosen as argv2. Therefor it will be named output")
        export_xgi_data_hypergraph_to_txt(hypergraph, "output.hypergraph")