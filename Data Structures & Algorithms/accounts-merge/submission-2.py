class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}

        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)

            if root1 == root2:
                return

            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]


        email_set = {}

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in parent:
                    parent[account[i]] = account[i]
                    rank[account[i]] = 0
                email_set[account[i]] = name

        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                union(first_email, account[i])

        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        result = []
        for root in groups:
            name = email_set[root]
            emails = sorted(groups[root])
            result.append([name] + emails)

        return result
        