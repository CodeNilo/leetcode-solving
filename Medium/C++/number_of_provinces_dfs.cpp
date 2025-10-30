class Solution {
private:

void dfs(int node, vector<int>& visited, vector<vector<int>>& adjMatrix) {

    visited[node] = 1;

    for (int i=0; i<adjMatrix.size(); i++) {

        if (adjMatrix[node][i] == 1 && visited[i] != 1) {

            dfs(i, visited, adjMatrix);
        }
    }

}


public:
    int findCircleNum(vector<vector<int>>& isConnected) {

        int n = isConnected.size();

        vector<int> visited(n, 0);

        int province_count = 0;

        for (int i = 0; i<n; i++) { // Disjoin graph so we iterate from the outside

            if (visited[i] != 1) {

                province_count++;
                dfs(i, visited, isConnected);
            }

        }
        
        return province_count;
    }
};
