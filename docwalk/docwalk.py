import ast
from collections import deque

class DocWalker:
    def __init__(self, filename):
        with open(filename) as f:
            self._root = ast.parse(f.read(), filename=filename)

    def run(self):
        return list(self._walk_breadth_first(self._root))

    def _walk_depth_first(self, node, path=()):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.ClassDef) or isinstance(child, ast.FunctionDef):
                new_path = path + (child.name,)
                yield ".".join(new_path)
                for path_name in self._walk_depth_first(child, new_path):
                    yield path_name

    def _walk_breadth_first(self, root):
        queue = deque()
        queue.append((root, ()))
        while(queue):
            node, path = queue.popleft()
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.ClassDef) or isinstance(child, ast.FunctionDef):
                    new_path = path + (child.name, )
                    yield ".".join(new_path)
                    queue.append((child, new_path))