/*
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000
*/



bool sortcol( const vector<double>& v1, 
               const vector<double>& v2 ) { 
        return v1[0] < v2[0]; 
    }
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        int n = points.size();
        if(n == K){
            return points;
        }
        vector<vector<double> > v( n , vector<double> (2));
        for(int i=0;i<n;i++){
           //cout<<sqrt(pow(points[i][0],2)+pow(points[i][1],2))<<endl;
            v[i][0] = sqrt(pow(points[i][0],2)+pow(points[i][1],2));
            v[i][1] =  i;
        }
        sort(v.begin(),v.end(),sortcol);
        vector<vector<int> > result(K,vector<int> (2));
        // for(int i=0;i<n;i++){
        //     cout<<v[i][0] <<" "<<v[i][1]<<endl;
        // }
        int i=0;
        while(K--){
            result[i][0] = points[(int)v[i][1]][0];
            result[i][1] = points[(int)v[i][1]][1];
                i++;
        }
        return result;
    }
};