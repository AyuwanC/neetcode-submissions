class Solution {
public:
    vector<vector<int>> ans;
    vector<int> nums;
    int n;

    void dfs(vector<int>& res, vector<int>& vis) {
        if (res.size() == n) {
            ans.push_back(res);
            return;
        }

        for (int v = 0; v < n; v++) {
            if (!vis[v]) {
                res.push_back(nums[v]);
                vis[v] = 1;

                dfs(res, vis);

                res.pop_back();  
                vis[v] = 0;      
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        this->nums = nums;
        n = nums.size();
        ans.clear();

        for (int v = 0; v < n; v++) {
            vector<int> vis(n, 0);
            vis[v] = 1;

            vector<int> res;
            res.push_back(nums[v]);

            dfs(res, vis);
        }

        return ans;
    }
};