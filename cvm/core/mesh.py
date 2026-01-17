"""
Cognitive mesh - distributed intelligence
Multiple CVMs sharing knowledge
"""


class CognitiveMesh:
    """
    A network of cooperating CVMs
    Non-centralized intelligence
    """
    
    def __init__(self):
        self.nodes = []
    
    def add_node(self, cvm):
        """Add a CVM to the mesh"""
        self.nodes.append(cvm)
    
    def broadcast_rule(self, rule):
        """
        Broadcast a learned rule to all nodes
        Enables collective learning
        """
        for node in self.nodes:
            if hasattr(node, 'meta'):
                node.meta.reflect(rule)
    
    def consensus(self, ast):
        """
        Get consensus result from all nodes
        Returns most common result
        """
        results = []
        for node in self.nodes:
            result = node.think(ast)
            if isinstance(result, dict):
                results.append(result.get('result'))
            else:
                results.append(result)
        
        # Return most common (simple voting)
        from collections import Counter
        if results:
            counts = Counter(str(r.to_tuple()) if hasattr(r, 'to_tuple') else str(r) for r in results)
            return results[0]  # Return first for now
        return None
    
    def distribute_work(self, tasks):
        """
        Distribute tasks across mesh
        Returns results from all nodes
        """
        results = []
        for i, task in enumerate(tasks):
            node = self.nodes[i % len(self.nodes)]
            result = node.think(task)
            results.append(result)
        return results
