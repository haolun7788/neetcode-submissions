class Solution {
    public boolean isAnagram(String s, String t) {
        HashSet<String> string1 = new HashSet<String>();
        string1.add(sortIntoCharStrings(s));

        if (string1.contains(sortIntoCharStrings(t))) {
            return true;
        } else {
            return false;
        }
    }

    public String sortIntoCharStrings(String input) {
        char[] chars = input.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}
