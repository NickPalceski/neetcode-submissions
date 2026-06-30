class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::unordered_map<char, int> countMap;

        // Count characters in string s
        for (char c : s) {
            countMap[c]++;
        }

        // Subtract counts using characters in string t
        for (char c : t) {
            if (countMap.find(c) == countMap.end() || countMap[c] == 0) {
                return false;  // Character not found or count mismatch
            }
            countMap[c]--;
        }

        // All counts should be zero if they are anagrams
        for (const auto& entry : countMap) {
            if (entry.second != 0) {
                return false;
            }
        }

        return true;
    }
};
