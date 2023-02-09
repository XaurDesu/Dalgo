fn matrix_sum (nums: Vec<Vec<i32>>) -> i32 {
    let mut ret = 0;
    for i in 0..nums.len() {
        ret += nums[i][i];
    }
    return ret;
}

fn matrix_search (nums: Vec<Vec<i32>>, target: i32) -> bool {
    for i in 0..nums.len() {
        for j in 0.. nums[i].len() {
            if nums[i][j] == target {return true;}
        }
    }
    return false;
}

fn number_search(nums: Vec<i32>, target: i32) {
    
}


fn main() {
    println!("Hello, world!");
    //maybe not the fanciest way to define this, but i need a sample input you guys, sorry!
    let nums: Vec<Vec<i32>> = vec![vec![1,0,0],vec![0,1,0],vec![0,0,1]];
    println!("Matrix sum result is: {}", matrix_sum(nums));
    let nums2: Vec<Vec<i32>> = vec![vec![2,0,0],vec![0,2,0],vec![0,0,1]];
    println!("Matrix search result for 1 is: {}", matrix_search(nums2, 1));
    let nums3: Vec<Vec<i32>> = vec![vec![2,0,44444],vec![121221,2,232],vec![999999,123,1]];
    println!("Matrix search result for 680 is: {}", matrix_search(nums3, 680));
}   
