class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        same = []
        diff = []
        
        for equation in equations:
            left = equation[0]
            right = equation[3]
            op = equation[1]
            
            if op == '=':
                if left != right:
                    same.append((left, right))
                    
            if op == '!':
                diff.append((left, right))
            
        parent = {}
        def merge(a, b):
            rootA = root(a)
            rootB = root(b)
            
            parent[rootA] = rootB
            
        def root(a):
            if a not in parent:
                parent[a] = a
            
            if parent[a] == a:
                return a
            
            return root(parent[a])
            
        for (left, right) in same:
            merge(left, right)
            
        for (left, right) in diff:
            if root(left) == root(right):
                return False
            
        return True