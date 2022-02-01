def pattern(n):
    ans = []
    trays = "()"
    stage_check = n
    for i in range(n):
        # starter = ""
        if stage_check == n:
            # Block that generates the first part of the results "(((..)))"
            # for j in range(stage_check):
            #     starter += '('
            starter_1 = ""
            # y = [(lambda start: start + '(')(starter_1) for j in range(stage_check)]
            starter_1 = starter_1.join([(lambda start: start + '(')(starter_1) for j in range(stage_check)])
            # for k in range(stage_check):
            #     starter += ')'
            starter_2 = ""
            # z = [(lambda start: start + ')')(starter_2) for k in range(stage_check)]
            starter_2 = starter_2.join([(lambda start: start + ')')(starter_2) for k in range(stage_check)])
            starter = starter_1 + starter_2
            ans.append(starter)
            stage_check -= 1
        # Block that generates the middle part of the results "((()))()", "(())()()"
        if stage_check < n and not stage_check <= 1:
            starter = ""
            stage_check_1 = n - stage_check
            # for l in range(stage_check):
            #     starter += '('
            y1 = [(lambda start: start + '(')(starter) for l in range(stage_check)]
            # for k in range(stage_check):
            #     starter += ')'
            y2 = [(lambda start: start + ')')(starter) for k in range(stage_check)]
            y3 = "".join(y1) + "".join(y2)
            # for m in range(stage_check_1):
            #     y3 += trays
            y4 = [(lambda start: start + "")(trays) for m in range(stage_check_1)]
            y5 = y3 + "".join(y4)
            ans.append(y5)
            stage_check -= 1
        # if stage_check < n and not stage_check <= 1:
        #     starter = ""
        #     stage_check_1 = n - stage_check
        #     for l in range(1):
        #         starter += '('
        #         for o in range(stage_check - 1):
        #             starter += trays
        #     for k in range(1):
        #         starter += ')'
        #     for m in range(stage_check_1):
        #         starter += trays
        #     ans.append(starter)
        #     stage_check -= 1
        # Block that adds the '()' to the results
        if stage_check == 1:
            # for n in range(n):
            #     starter += trays
            y1 = [(lambda start: start + "")(trays) for n in range(n)]
            ans.append("".join(y1))
            stage_check -= 1
        # Returns the final results
        if stage_check == 0:
            return ans


print(pattern(5))
