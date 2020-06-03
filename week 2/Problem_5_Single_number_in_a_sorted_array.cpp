/*
You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one element which appears exactly once. 
Find this single element that appears only once.
*/

// Solution with O(n) time complexity using XOR operation.
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int a=0;
        for(int x=0;x<nums.size();x++){
            a = a^nums[x];
        }
        return a;
    }
};

// Can be solved in O(log n) using Binary Search.
