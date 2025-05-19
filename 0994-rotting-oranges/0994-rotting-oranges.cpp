class Solution {
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    bool visited[10][10];
    int second = 0;

public:
    int orangesRotting(vector<vector<int>>& grid) {
        memset(visited, false, sizeof(visited));
        queue<pair<int,int>> q;
        for(int i = 0; i < grid.size(); i++){
            for(int j  = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 2){
                     q.push({i,j});
                    visited[i][j] = true;
                }
            }
         }

        while(!q.empty()){
            int size = q.size();
            bool anyChange = false;
            for(int s = 0; s < size; s++){
                pair<int, int> cur = q.front();
                q.pop();
                for(int i = 0; i < 4; i++){
                    int nx = cur.first + dx[i];
                    int ny = cur.second + dy[i];
                    
                    if(nx >= grid.size() || nx < 0 || ny >= grid[0].size() || ny < 0){ //GRID가 항상 최대가 아니니까 vector라는 것에 집중
                        continue;
                    }
                    if(visited[nx][ny]){
                        continue;
                    }
                    if(grid[nx][ny] == 1){
                        grid[nx][ny] = 2;
                        visited[nx][ny] = true;
                        anyChange = true;
                        q.push({nx, ny});
                    }
                }
            }
             if(anyChange){
                second++;
            }
        }
        for(int i = 0; i < grid.size(); i++){
            for(int j  = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 1){
                    return -1;
                }
            }
         }
         return second;
    }
};
