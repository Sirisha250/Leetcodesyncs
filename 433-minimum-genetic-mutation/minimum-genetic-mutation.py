from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        
        bank = set(bank)
        queue = deque([(startGene, 0)])
        genes = {'A', 'C', 'G', 'T'}
        
        while queue:
            current, mutations = queue.popleft()
            if current == endGene:
                return mutations
            
            for i in range(len(current)):
                for g in genes:
                    if g != current[i]:
                        mutated = current[:i] + g + current[i+1:]
                        if mutated in bank:
                            queue.append((mutated, mutations + 1))
                            bank.remove(mutated)  # Avoid revisiting
        
        return -1
