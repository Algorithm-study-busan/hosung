class Solution {
    public Integer getInt(String time) {
        String[] timeSplited = time.split(":");
        Integer M = Integer.parseInt(timeSplited[0]);
        Integer S = Integer.parseInt(timeSplited[1]);
        
        return M*60 + S;
    }
    
    public String toTime(Integer time) {
        Integer H = time / 60;
        Integer M = time % 60;
        
        return String.format("%02d", H) + ":" + String.format("%02d", M);
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        Integer endTime = getInt(video_len);
        Integer cur = getInt(pos);
        Integer start_op = getInt(op_start);
        Integer end_op = getInt(op_end);
        
        if (cur >= start_op && cur <= end_op) {
            cur = end_op;
        }
        
        for (String command : commands) {
            if (command.equals("next")) {
                cur = Math.min(endTime, cur + 10);
            }
            else if (command.equals("prev")) {
                cur = Math.max(0, cur - 10);
            }
            
            if (cur >= start_op && cur <= end_op) {
                cur = end_op;
            }
        }
        
        return toTime(cur);
    }
}