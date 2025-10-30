/* 
  This version transform the adjacency matrix into an ajacency list
  so it's easier to understand and navigate, but it's slower due to
  the extra work, so it's better to just work with the adjacency matrix.
*/


class Solution {

private:

vector<vector<int>> transformMatrixToList(int n, vector<vector<int>> adjMatrix) { 

    vector<vector<int>> adjList(n);

    for (int i = 0; i<n; i++) {

        for (int j = 0; j<n; j++) {

            if (adjMatrix[i][j] == 1 && i != j) {
                
                adjList[i].push_back(j);
                adjList[j].push_back(i);

            }
        }
    }

    return adjList;
}

void dfs (int node, vector<int>& visited, vector<vector<int>>& adjList) {

    visited[node] = 1;

    for (auto it: adjList[node]) {

        if (visited[it] != 1) {

            dfs(it, visited, adjList);
        }
    }

}

public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        
        int n = isConnected.size();
        vector<vector<int>> adjList = transformMatrixToList(n, isConnected);
        vector<int> visited(n, 0);

        int count = 0;

        for (int i = 0; i<n; i++) {

            if (visited[i] != 1) {
                
                dfs(i, visited, adjList);
                count++;

            }
        
        } 

        return count;
    }
};
