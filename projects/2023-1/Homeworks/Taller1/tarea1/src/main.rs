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

fn number_search(nums: Vec<i32>, begin:i32, end:i32, target: i32) {
    if target == nums[begin] {
        return begin;
    } 
    if target == nums[end] {
        return end;
    }
    number_search(nums, begin+1, end-1, target);
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
    let nums4: Vec<i32> = vec![1, 23, 44, 12, 90, 16];
    println!("recursive number position search for vector {} for number {} is: {}",nums4,90,number_search(nums4, 0, nums4.len(),90))
}   
