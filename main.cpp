#include <networkit/graph/Hypergraph.hpp>
#include <networkit/graph/HypergraphExpansions.hpp>
#include <networkit/graph/Graph.hpp>
#include <networkit/centrality/Betweenness.hpp>
#include <networkit/Globals.hpp>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>

int main( int argc,      // Number of strings in array argv
          char *argv[],   // Array of command-line argument strings
          char *envp[] )  // Array of environment variable strings
{
    bool firstline = true;
    NetworKit::Hypergraph hypergraph;
    std::ifstream file;
    file.open(argv[1]);
    if(file.is_open()) {
        while(file) {
            std::getline(file, line);
            std::cout << line << std::endl;
            if(firstline) {
                hypergraph.addNodes(line)
            } else {
                hypergraph.addEdge({line})
            }
        }
    }

    //print out hypergraph details
    std::cout << "Original Hypergraph:" << std::endl;
    std::cout << "Number of nodes: " << hypergraph.numberOfNodes() << std::endl;
    std::cout << "Number of hyperedges: " << hypergraph.numberOfEdges() << std::endl;
    
    return 0;
}
