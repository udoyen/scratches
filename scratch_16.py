def pattern(n):
    ans = []
    trays = "()"
    stage_check = n
    for i in range(n):
        starter = ""
        if stage_check == n:
            for j in range(stage_check):
                starter += '('
            for k in range(stage_check):
                starter += ')'
            ans.append(starter)
            stage_check -= 1
        if stage_check < n and not stage_check <= 1:
            starter = ""
            stage_check_1 = n - stage_check
            for l in range(stage_check):
                starter += '('
            for k in range(stage_check):
                starter += ')'
            for m in range(stage_check_1):
                starter += trays
            ans.append(starter)
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
        if stage_check == 1:
            starter = ""
            for n in range(n):
                starter += trays
            ans.append(starter)
            stage_check -= 1
        if stage_check == 0:
            return ans


print(pattern(4))
