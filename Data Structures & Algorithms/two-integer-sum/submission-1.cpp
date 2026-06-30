class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numMap; // Map to store the complement and its index
    
    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        
        // Check if the complement exists in the map
        if (numMap.find(complement) != numMap.end()) {
            return {numMap[complement], i}; // Return the indices of the two numbers
        }
        
        // Store the current number and its index in the map
        numMap[nums[i]] = i;
    }
    
    // If no solution is found, return an empty vector
    return {};
}
};
