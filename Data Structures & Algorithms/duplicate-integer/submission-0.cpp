class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        if (nums.size() == 0 || nums.size() == 1){
            return false;
        }

        int num1;
        int num2;
        int listSize = nums.size();

        for (int i = 0; i<= listSize-1; ++i){
            for (int j = i+1; j<=listSize-1; ++j){
                num1 = nums[i];
                num2 = nums[j];
                if (num1 == num2){
                    return true;
                }
            }
        }
        return false;
    }
};
