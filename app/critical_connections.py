from typing import List

class CriticalConnections():

    def dfs_solve(self, node, parent, adj, low, tin):
        self.timer += 1
        tin[node] = low[node] = self.timer

        for iter in adj[node]:
            if iter == parent:
                continue
            elif tin[iter] == -1:
                self.dfs_solve(iter, node, adj, low, tin)
                low[node] = min(low[iter], low[node])

                if low[iter] > tin[node]:
                    self.connections.append((node, iter))

            else:
                low[node] = min(low[iter], low[node])

    def get_critical_connections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.timer = 1
        self.connections = []
        adj = []
        
        for i in range(n):
            adj.append([])

        for iter in connections:
            adj[iter[0]].append(iter[1])
            adj[iter[1]].append(iter[0])
            
        low = [-1] * n
        tin = [-1] * n

        mn = 1

        self.dfs_solve(0, -1, adj, low, tin)
        return self.connections