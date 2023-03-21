class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = {}
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1]
                full_path = directory + '/' + name
                if content in content_to_path:
                    content_to_path[content].append(full_path)
                else:
                    content_to_path[content] = [full_path]
        return [group for group in content_to_path.values() if len(group) > 1]