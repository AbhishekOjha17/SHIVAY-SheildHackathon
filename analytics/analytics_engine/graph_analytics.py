"""
Graph Analytics using NetworkX
"""
import networkx as nx
from typing import Dict, Any, List
from loguru import logger


class GraphAnalytics:
    """Graph analytics for incident networks"""
    
    def __init__(self):
        """Initialize graph analytics"""
        self.graph = nx.Graph()
    
    def build_incident_graph(self, incidents: List[Dict[str, Any]]):
        """Build graph from incidents"""
        self.graph.clear()
        
        for incident in incidents:
            incident_id = incident.get("incident_id")
            self.graph.add_node(incident_id, **incident)
            
            # Add edges based on relationships
            related = incident.get("related_incidents", [])
            for related_id in related:
                self.graph.add_edge(incident_id, related_id)
        
        logger.info(f"Built graph with {self.graph.number_of_nodes()} nodes")
    
    def analyze_network(self) -> Dict[str, Any]:
        """Analyze network structure"""
        if self.graph.number_of_nodes() == 0:
            return {}
        
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "density": nx.density(self.graph),
            "clusters": list(nx.connected_components(self.graph)),
        }
    
    def find_central_nodes(self, top_n: int = 10) -> List[str]:
        """Find most central nodes"""
        if self.graph.number_of_nodes() == 0:
            return []
        
        centrality = nx.degree_centrality(self.graph)
        sorted_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        return [node for node, _ in sorted_nodes[:top_n]]

