//Dividir y conquistar, sale del tiempo establecido.
impl Solution {

    pub fn arr_product(nums: Vec<i32>) -> i32 {
        let mut ret = 1;
        for i in nums {
            ret *= i;
        }
        return ret
    }

    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut ret: i32 = i32::MIN;
        let mut prod: i32;
        for i in 0..nums.len() {
            for j in i+1..nums.len()+1 {
                prod = Solution::arr_product(nums[i..j].to_vec());
                if prod > ret {
                    ret = prod;
                }
            }
        }

        return ret;
    }
}