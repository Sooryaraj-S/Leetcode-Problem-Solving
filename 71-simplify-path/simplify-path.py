class Solution:
    def simplifyPath(self, path: str) -> str:
        text   = path.split('/')
        stack=[]
        for i in text:
            if i=='' or i=='.':
                continue
            if i=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)   