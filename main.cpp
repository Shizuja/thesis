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
#include <sstream>
#include <string>

NetworKit::Hypergraph readHypergraphFromFile(char* data) {
    bool firstline = true;
    NetworKit::Hypergraph hypergraph;
    std::ifstream file;
    file.open(data);
    if(file.is_open()) {
        std::string line;
        while(std::getline(file, line)) {
            if(firstline) {
                hypergraph.addNodes(std::stoi(line));
                firstline = false;
            } else {
                std::stringstream ss(line);
                NetworKit::node node;
                std::vector<NetworKit::node> nodes;
                while (ss >> node) {
                    nodes.push_back(node);
                }
                hypergraph.addEdge(nodes);
            }
        }
    }
    return hypergraph;
}

int main( int argc,      // Number of strings in array argv
          char *argv[],   // Array of command-line argument strings
          char *envp[] )  // Array of environment variable strings
{
    
    NetworKit::Hypergraph hypergraph = readHypergraphFromFile(argv[1]);
    //print out hypergraph details
    std::cout << "Original Hypergraph:" << std::endl;
    std::cout << "Number of nodes: " << hypergraph.numberOfNodes() << std::endl;
    std::cout << "Number of hyperedges: " << hypergraph.numberOfEdges() << std::endl;
    
    return 0;
}
