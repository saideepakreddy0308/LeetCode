class Solution:
    def simplifyPath(self, path: str) -> str:
        # split the path into a list of directories
        dirs = path.split('/')
        # initialize a stack to store the directories
        stack = []
        for dir in dirs:
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(dir)
        # join the directories in the stack and add a leading slash
        return '/' + '/'.join(stack)
