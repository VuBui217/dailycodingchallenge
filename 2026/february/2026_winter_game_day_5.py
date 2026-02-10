"""
Docstring for 2026.february.2026_winter_game_day_5
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-10
                    2026 Winter Games Day 5: Cross-Country Skiing
Given an array of finish times for a cross-country ski race, convert them into times behind the winner.

Given times are strings in "H:MM:SS" format.
Given times will be in order from fastest to slowest.
The winners time (fastest time) should correspond to "0".
Each other time should show the time behind the winner, in the format "+M:SS".
For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"].
"""
def get_relative_results(results):
    output = []
    output.append("0")
    f_hh_str, f_mm_str, f_ss_str = results[0].split(":")
    f_hh, f_mm, f_ss = int(f_hh_str), int(f_mm_str), int(f_ss_str)
    f_time = f_hh * 3600 + f_mm * 60 + f_ss
    for time in results[1:]:
        curr_hh, curr_mm, curr_ss = time.split(":")
        
        curr_time = int(curr_hh) * 3600 + int(curr_mm) * 60 + int(curr_ss)
        diff = curr_time - f_time

        output.append(f"+{diff // 60}:{diff % 60:02d}")        
    return output

print(get_relative_results(["1:25:32", "1:26:10", "1:27:05"])) # should return ["0", "+0:38", "+1:33"].
print(get_relative_results(["1:00:01", "1:00:05", "1:00:10"])) # should return ["0", "+0:04", "+0:09"].
print(get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"])) # should return ["0", "+0:17", "+0:42", "+2:05"].
print(get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"])) # should return ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"].
print(get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"])) # should return ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"].