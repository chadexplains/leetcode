class FileSharing:

    def __init__(self):
        self.groups = {}
        self.documents = {}
        self.next_id = 1

    def join(self, group_id: int, user_id: int) -> None:
        if group_id not in self.groups:
            self.groups[group_id] = set()
        self.groups[group_id].add(user_id)

    def share(self, owner_id: int, document_id: int) -> None:
        if owner_id not in self.groups:
            return
        if document_id not in self.documents:
            self.documents[document_id] = set()
        self.documents[document_id].add(owner_id)

    def unshare(self, owner_id: int, document_id: int) -> None:
        if document_id not in self.documents:
            return
        if owner_id in self.documents[document_id]:
            self.documents[document_id].remove(owner_id)

    def find_user(self, document_id: int) -> List[int]:
        if document_id not in self.documents:
            return []
        users = set()
        for group_id in self.documents[document_id]:
            if group_id in self.groups:
                users |= self.groups[group_id]
        return sorted(users)

    def find_document(self, user_id: int) -> List[int]:
        if user_id not in self.groups.values():
            return []
        documents = set()
        for document_id, groups in self.documents.items():
            if any(group_id in self.groups and user_id in self.groups[group_id] for group_id in groups):
                documents.add(document_id)
        return sorted(documents)