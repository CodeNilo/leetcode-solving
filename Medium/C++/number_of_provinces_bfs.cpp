class Solution {

private:
    void bfs(int start, int& count, vector<int>& visited, int n, vector<vector<int>>& adjMatrix) {

        queue<int> q;
        q.push(start);
        visited[start] = 1;

        while (!q.empty()) {

            int node = q.front();
            
            q.pop();

            for (int i=0; i<n; i++) {
            
                if (adjMatrix[node][i] == 1 && visited[i]!=1) {
                    visited[i] = 1;
                    q.push(i);
                }
            }
        }
    }

public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        
        int count = 0;
        int n = isConnected.size();
        vector<int> visited(n,0);
        int start = 0;

        for (int i=0; i<n; i++) { // Disjoint graph, so we iterate outside too

            if (visited[i]!=1) {
                count++;
                bfs(i, count, visited, n, isConnected);
            }
        }
            

        return count;
    }
};
