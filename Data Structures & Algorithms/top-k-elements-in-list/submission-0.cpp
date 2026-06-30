class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //track numbers and their freq
        unordered_map<int, int> myMap;
        for (int num: nums){
            myMap[num]++;
        }
        //used to compare frequencies
        auto myLambda = [](const pair<int, int>& a, const pair<int,int>& b){
            return a.second > b.second;
        };

        vector<pair<int,int>> myVec(myMap.begin(), myMap.end());
        sort(myVec.begin(), myVec.end(), myLambda);

        vector<int> result;
        for (int i=0; i<k; ++i){
            result.push_back(myVec[i].first);
        }
        return result;
    }
};
