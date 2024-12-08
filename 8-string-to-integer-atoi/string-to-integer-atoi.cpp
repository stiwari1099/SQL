class Solution {
public:
    int myAtoi(string s) {
        int res = 0;
        int sign = 1;
        int i = 0;
        int str = s.length();

        // Step 1: Handle leading whitespace
        while (i < str && s[i] == ' ') {
            i++;
        }
        // cheking signs
        if (i < str && (s[i] == '-' || s[i] == '+')) {
            if(i+1<str && (s[i+1] == '-' || s[i+1] == '+')){
                return 0;
            }
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
        while (i < str && isdigit(s[i])) {
            int digit = s[i] - '0';
            if (res > INT_MAX / 10 ||
                (res == INT_MAX / 10 && digit > INT_MAX % 10)) {
                
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            res = res * 10 + digit;
            i++;
        }
        return res * sign;
    }
};