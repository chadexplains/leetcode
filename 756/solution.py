def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def build_row(row):
            if len(row) == 1:
                return True
            for i in range(len(row) - 1):
                pairs = [(row[i], row[i+1])] # all possible pairs of adjacent blocks
                if any(pair not in triples for pair in pairs):
                    return False
            next_row = []
            build_blocks(0, '', next_row)
            return build_row(next_row)
        def build_blocks(index, block, next_row):
            if index == len(bottom) - 1:
                next_row.append(block)
                return
            for triple in triples[(bottom[index], bottom[index+1])]:
                build_blocks(index+1, block+triple, next_row)
        triples = collections.defaultdict(list)
        for triple in allowed:
            triples[triple[:2]].append(triple[2])
        return build_row(bottom)