"""
Multi-step reasoning via search
Explores rewrite space to find optimal transformations
"""
from collections import deque


class Search:
    """
    Breadth-first search over the rewrite graph
    Finds sequences of transformations that preserve semantics
    """
    
    def __init__(self, rewriter, verifier, max_depth=5):
        self.rewriter = rewriter
        self.verifier = verifier
        self.max_depth = max_depth
    
    def run(self, root):
        """
        Search for a simplification path
        Returns list of AST nodes representing the proof chain
        """
        queue = deque([(root, [root])])
        visited = {root.to_tuple()}
        
        while queue:
            node, path = queue.popleft()
            
            # Stop if too deep
            if len(path) > self.max_depth:
                continue
            
            # Try all possible rewrites
            for candidate in self.rewriter.expand(node):
                # Skip if already visited
                if candidate.to_tuple() in visited:
                    continue
                
                # Verify transformation
                if self.verifier.verify(node, candidate):
                    new_path = path + [candidate]
                    
                    # If fully simplified (no more rewrites), return
                    if not self.rewriter.expand(candidate):
                        return new_path
                    
                    visited.add(candidate.to_tuple())
                    queue.append((candidate, new_path))
        
        # Return best path found
        return [root]
