//recursive brute force, exceeds time limit.
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        if m==1 && n==1 {
            return 1;
        } if n == 1 {
            return Solution::unique_paths(m-1, n);
        } if m == 1 {
            return Solution::unique_paths(m, n-1);
        } else {
            return Solution::unique_paths(m-1, n) + Solution::unique_paths(m, n-1);
        }
    }
}
//Divide and Conquer
impl Solution {
    pub fn conquer() {

    }

    pub fn unique_paths(m: i32, n: i32) -> i32 {
        
    }
}

//DP
impl Solution {
    
    pub fn conquer() {

    }

    pub fn unique_paths(m: i32, n: i32) -> i32 {
        
    }
}