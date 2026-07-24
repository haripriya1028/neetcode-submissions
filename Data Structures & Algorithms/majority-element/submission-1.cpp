class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int k=(nums.size())/2;
        unordered_map<int, int> freq;
        for(int n:nums){
            freq[n]++;
        }
        for(auto &p:freq){
            if(p.second>k){
                return p.first;
            }
        }
    }
};