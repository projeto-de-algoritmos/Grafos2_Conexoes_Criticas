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

"""
class Solution {
    int timer = 1;
    vector<vector<int>> ans;
    // low = lowest time
    // tin = time in
    void dfsSolve(int node, int parent, vector<vector<int>>& adj, vector<int> &low, vector<int> &tin){
        tin[node] = low[node] = timer++;
        for(auto it: adj[node]){
            if(it == parent)
                continue;
            else if(tin[it] == -1){
                dfsSolve(it,node,adj,low,tin);
                low[node] = min(low[it],low[node]);
                if(low[it] > tin[node]){
                    ans.push_back({node,it});
                }
                
            }
            else {
                low[node] = min(low[it],low[node]);
            }
        }
    }
    
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> adj(n);
        for(auto it : connections){
            adj[it[0]].push_back(it[1]);
            adj[it[1]].push_back(it[0]);
        }
        vector<int> low(n,-1), tin(n,-1);
        int mn = 1;
        dfsSolve(0,-1,adj, low, tin);
        return ans;
    }
};




class Solution:
    
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

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.timer = 1
        self.connections = []
        adj = [[0]] * n

        for iter in connections:
            adj[iter[0]].append(iter[1])
            adj[iter[1]].append(iter[0])

        low = [-1] * n
        tin = [-1] * n

        mn = 1

        self.dfs_solve(0, -1, adj, low, tin)
        return self.connections
"""