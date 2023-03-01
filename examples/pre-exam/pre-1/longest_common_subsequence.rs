//primera versión divide and conquer, excede tiempo
impl Solution {
    pub fn get_subsequences(text: String, out: String, ret: &mut Vec<std::string::String>) {
        if text.len() == 0 {
            ret.push(out);
        } else {
        let mut alt = out.clone();
        alt.push(text.chars().next().unwrap());
        Solution::get_subsequences(text[1..text.len()].to_string(),alt,ret);
        Solution::get_subsequences(text[1..text.len()].to_string(),out,ret);
        }

        return;
    }

    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let mut ret = 0;
        
        let mut vec1 = Vec::new();
        let mut vec2 = Vec::new();

        Solution::get_subsequences(text1,String::new(),&mut vec1);
        Solution::get_subsequences(text2,String::new(),&mut vec2);

        for i in vec1 {
            if vec2.contains(&i) {
                if i.len() > ret {
                    ret = i.len()};
                }
            }
        return ret as i32;
    }
}