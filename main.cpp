#include <networkit/graph/Hypergraph.hpp>
#include <networkit/graph/HypergraphExpansions.hpp>
#include <networkit/graph/Graph.hpp>
#include <networkit/Globals.hpp>
#include <map>
#include <set>
#include <vector>
#include <iostream>

int main() {
    // Hypergraph with 4 nodes and 3 hyperedges
    // Hyperedge 0: {0, 1}
    // Hyperedge 1: {1, 2, 3}
    // Hyperedge 2: {0, 3}

    NetworKit::Hypergraph hypergraph1(4);
    hypergraph1.addEdge({0, 1});
    hypergraph1.addEdge({1, 2, 3});
    hypergraph1.addEdge({0, 3});
	
	NetworKit::Graph cliqueExpansionGraph = NetworKit::HypergraphExpansions::cliqueExpansion(hypergraph1);
	
	NetworKit::Hypergraph hypergraph2(11);
    hypergraph2.addEdge({0, 1, 8, 10});
    hypergraph2.addEdge({1, 6, 7});
    hypergraph2.addEdge({0, 3, 4, 9, 10});
	hypergraph2.addEdge({0, 2, 5, 6});
	hypergraph2.addEdge({1, 8});
	hypergraph2.addEdge({0, 2, 3, 7, 9});
	
	cliqueExpansionGraph = NetworKit::HypergraphExpansions::cliqueExpansion(hypergraph2);
	
	NetworKit::Hypergraph hypergraph3(6);
    hypergraph3.addEdge({1, 3, 4});
    hypergraph3.addEdge({0, 3, 4, 5});
	hypergraph3.addEdge({0, 2, 5});
	hypergraph3.addEdge({1, 5});
	hypergraph3.addEdge({0, 2, 3, 4});
	
	cliqueExpansionGraph = NetworKit::HypergraphExpansions::cliqueExpansion(hypergraph3);

	
	
	

    //print out hypergraph details
    std::cout << "Original Hypergraph:" << std::endl;
    std::cout << "Number of nodes: " << hypergraph3.numberOfNodes() << std::endl;
    std::cout << "Number of hyperedges: " << hypergraph3.numberOfEdges() << std::endl;

    // Print out the clique expansion details
    std::cout << "\nClique Expansion Graph:" << std::endl;
    std::cout << "Number of nodes: " << cliqueExpansionGraph.numberOfNodes() << std::endl;
    std::cout << "Number of edges: " << cliqueExpansionGraph.numberOfEdges() << std::endl;
	
    // Print edges in the clique expansion
    cliqueExpansionGraph.forEdges([&](NetworKit::node u, NetworKit::node v) {
        std::cout << "Edge: " << u << " - " << v << std::endl;
    });
/*	
    std::pair<NetworKit::Graph, std::map<NetworKit::node, std::pair<NetworKit::node, NetworKit::edgeid>>> lineExpansionPair = lineExpansion(hypergraph);
    NetworKit::Graph lineExpansionGraph = lineExpansionPair.first;
    std::map<NetworKit::node, std::pair<NetworKit::node, NetworKit::edgeid>> lineExpansionNodeMap = lineExpansionPair.second;

    // Print out the line expansion details
    std::cout << "\nLine Expansion Graph:" << std::endl;
    std::cout << "Number of nodes: " << lineExpansionGraph.numberOfNodes() << std::endl;
    std::cout << "Number of edges: " << lineExpansionGraph.numberOfEdges() << std::endl;

    // Print edges in the line expansion
    lineExpansionGraph.forEdges([&](NetworKit::node u, NetworKit::node v) {
        std::cout << "Edge: " << u << " - " << v << std::endl;
    });

    NetworKit::Hypergraph reconstructedHypergraph = reconstructHypergraphFromLineExpansion(lineExpansionGraph, lineExpansionNodeMap);

    // Print out the line expansion details
    std::cout << "\nReconstructed Hypergraph:" << std::endl;
    std::cout << "Number of nodes: " << reconstructedHypergraph.numberOfNodes() << std::endl;
    std::cout << "Number of edges: " << reconstructedHypergraph.numberOfEdges() << std::endl;
*/
    return 0;
}
