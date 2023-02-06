fn matrix_sum (nums: Vec<Vec<i32>>) -> i32 {
    let mut ret = 0;
    for i in 0..nums.len() {
        ret += nums[i][i];
    }
    return ret;
}

fn main() {
    println!("Hello, world!");
    //maybe not the fanciest way to define this, but i need a sample input you guys, sorry!
    let nums: Vec<Vec<i32>> = vec![vec![1,0,0],vec![0,1,0],vec![0,0,1]];
    println!("Matrix sum result is: {}", matrix_sum(nums));
}   
