class Solution {
public:
    int fillCups(vector<int>& amount) {
        int second = 0;

        while (true) {
            sort(amount.begin(), amount.end(), greater<int>());
            if(amount[0]==0){
                break;
            }
            if(amount[1]>0){
                amount[0]--;
                amount[1]--;
            }else{
                amount[0]--;
            }
            second++;
        }
        return second;
    }
};