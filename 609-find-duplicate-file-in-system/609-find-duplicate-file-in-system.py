class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = {}
        
        for path in paths:
            p = path.split(" ")
            
            folder = p[0]
            files = p[1:]
        
            for file in files:
                f = file.split("(")
                file_path = folder + "/" + f[0]
                file_content = f[1][:-1]
                
                if file_content not in res:
                    res[file_content] = []
                    
                res[file_content].append(file_path)
        
        ans = []
        for k in res.keys():
            if len(res[k]) > 1:
                ans.append(res[k])
            
        return ans
        