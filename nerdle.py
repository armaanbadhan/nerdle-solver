from back import check_equation

def fetch_array():
    f = open("words.txt", mode='r')
    arr = list(f)
    arr = list(map(lambda s: s.strip(), arr))
    f.close()
    return arr

correct = {}             # once green, always green
contains = set()         # reject ones with dont contain chars which are supposed to be in
wrong_pos = {}           # dictionary containing wrong pos {char: [list where not valid]}
checked = set()          # reject equation already checked, TODO: can impliment better ways which reduce the search space
doesnt = set()


if __name__ == "__main__":
    arr = fetch_array()
    ans = "12+35=47"
    ret = check_equation(ans)

    while ret != "cccccccc":
        print(ans, ret)
        checked.add(ans.strip())
        for i in range(8):
            if ret[i] == "c":
                correct[i] = ans[i]
                contains.add(ans[i])
            if ret[i] == "w":
                contains.add(ans[i])
                if ans[i] in wrong_pos:
                    wrong_pos[ans[i]].add(i)
                else:
                    wrong_pos[ans[i]] = {i}
            if ret[i] == "n":
                doesnt.add(ans[i])
                if ans[i] in wrong_pos:
                    wrong_pos[ans[i]].add(i)
                else:
                    wrong_pos[ans[i]] = {i}
            doesnt -= doesnt.intersection(contains)
        
        # print(checked, correct, contains, wrong_pos, doesnt)

        counter = 0

        for i in arr:
            possible = True
            if i in checked:
                possible = False
            for j in doesnt:
                if j in i:
                    possible = False
            for j in contains:
                if j not in i:
                    possible = False
            for j in correct:
                if correct[j] != i[j]:
                    possible = False
            
            chars_count = {}

            for itr in range(8):
                if i[itr] in chars_count:
                    chars_count[i[itr]].add(itr)
                else:
                    chars_count[i[itr]] = {itr}
            
            for j in wrong_pos:
                try:
                    s1 = chars_count[j]
                    s2 = wrong_pos[j]
                    if s1.intersection(s2):
                        possible = False
                except KeyError:
                    pass

            if possible:
                ans = i
                break
        ret = check_equation(ans)
    
    print(ans)
