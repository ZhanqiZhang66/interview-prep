class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        class UnionFind:
            def __init__(self, n):
                self.parents = list(range(n))
                self.sizes = [0] * n

            def find(self, node):
                if self.parents[node] != node:
                    self.parents[node] = self.find(self.parents[node])
                return self.parents[node]
            def union(self, node1, node2):
                r1, r2 = self.find(node1), self.find(node2)
                if r1 == r2:
                    return False

    
                if self.sizes[r1] < self.sizes[r2]:
                    r1, r2 = r2, r1
                self.sizes[r1] += self.sizes[r2]
                self.parents[r2] = r1
                return True

        n = len(accounts)
        UF = UnionFind(n)
        email2idx = {}
        for i, account in enumerate(accounts):
            for email in account[1:]: 
                if email in email2idx:
                    UF.union(i, email2idx[email])
                else:
                    email2idx[email] = i
        res_dict = defaultdict(list)
        for email, i in email2idx.items():
            user = UF.find(i)
            res_dict[user].append(email)
        res = []
        for i, email in res_dict.items():
            user = accounts[i][0]
            res.append([user] + sorted(res_dict[i]))

        return res

        
                    
        
           



         