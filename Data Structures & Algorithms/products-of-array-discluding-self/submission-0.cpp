class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        // Initialize the output array with 1s
        std::vector<int> output(n, 1);

        // Calculate left product and store it directly in the output array
        int left_product = 1;
        for (int i = 0; i < n; ++i) {
            output[i] = left_product;
            left_product *= nums[i];
        }

        // Calculate right product and multiply it with the corresponding left product in the output array
        int right_product = 1;
        for (int i = n - 1; i >= 0; --i) {
            output[i] *= right_product;
            right_product *= nums[i];
        }

        return output;
    }
};
