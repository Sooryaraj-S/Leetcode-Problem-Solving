class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        List<String> line = new ArrayList<>();
        int len = 0;
        int i = 0;
        int n = words.length;
        
        while (i < n) {
            if (len + line.size() + words[i].length() > maxWidth) {
                int extraSpace = maxWidth - len;
                int slots = Math.max(1, line.size() - 1);
                int spaces = extraSpace / slots; 
                int remainder = extraSpace % slots;

                for (int j = 0; j < slots; j++) {
                    StringBuilder word = new StringBuilder(line.get(j));
                    word.append(" ".repeat(spaces));
                    if (remainder > 0) {
                        word.append(" ");
                        remainder--;
                    }
                    line.set(j, word.toString());
                }
                res.add(String.join("", line));
                line.clear();
                len = 0;
            }
            line.add(words[i]);
            len += words[i].length();
            i++;
        }

        String lastLine = String.join(" ", line);
        int trailSpace = maxWidth - lastLine.length();
        lastLine += " ".repeat(trailSpace);
        res.add(lastLine);
        return res;
    }
}