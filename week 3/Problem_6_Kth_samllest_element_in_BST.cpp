/*
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


Constraints:
    The number of elements of the BST is between 1 to 10^4.
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// Time complexity O(h) where h is height of BST.
// The Approach is to inorder traverse the BST.

vector<int> v;
void inorder(TreeNode* root){
    if(root != nullptr){
        inorder(root->left);
        v.push_back(root->val);
        inorder(root->right);
    }
}
class Solution {
public:
    Solution(){
        v.clear(); // To empty the vector for each test case
    }
    int kthSmallest(TreeNode* root, int k) {
        inorder(root);
        // for(auto i: v){
        //     cout<<i<<" "; 
        // }
        return v[k-1];
    }
};