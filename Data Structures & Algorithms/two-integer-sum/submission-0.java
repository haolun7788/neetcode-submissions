class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] out = new int[2];
        int difference = target - nums[0];
        for (int i = 0; i < nums.length; i++) {
            difference = target - nums[i];
            if (map.containsKey(difference)) {
                out[0] = map.get(difference);
                out[1] = i;
                return out;
            } else {
                map.put(nums[i], i);
            }
        }
        return out;
    }
}
