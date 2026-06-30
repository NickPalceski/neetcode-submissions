class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //if in the constraints, continue.
        if (nums.size() >= 2 && nums.size() <= 1000){
            if (target >= -10000000 && target <= 10000000){
                //loop through nums with i and j+1 comparing values.
                for (int i=0; i<nums.size(); ++i){
                    for (int j=i+1; j<nums.size(); ++j){

                        if ((nums[i] + nums[j]) == target){
                            return {i,j};
                        }
                    }
                }
            }
        }
    }
};
