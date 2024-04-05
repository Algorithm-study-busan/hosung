class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for file in path.split('/') :
            if not file or file == '.' : continue
            if file == '..' : 
                if ans : ans.pop(-1)
                continue
            else : ans.append(file)
        
        return '/' + '/'.join(ans)