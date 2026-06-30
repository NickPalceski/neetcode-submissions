class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedStr;

        for (const string& str: strs){
            encodedStr += to_string(str.size()) + "#" + str;
        }
        return encodedStr;
    }

    vector<string> decode(string s) {
        vector<string> decodedStrs;
        int i = 0;

        while (i <s.size()){
            int codePos = s.find('#', i);
            int length = stoi(s.substr(i, codePos - i));
            string str = s.substr(codePos + 1, length);
            decodedStrs.push_back(str);
            i = codePos + 1 + length;
        }
        return decodedStrs;

    }
};
