def is_win(turns):
    win1 = [1, 2, 3]
    win2 = [4, 5, 6]
    win3 = [7, 8, 9]
    win4 = [1, 4, 7]
    win5 = [2, 5, 8]
    win6 = [3, 6, 9]
    win7 = [1, 5, 9]
    win8 = [3, 5, 8]

    all_win = [win1, win2, win3, win4, win5, win6, win7, win8, win8]

    for win in all_win:
        good_number = 0
        for num in win:
            if num in turns:
                good_number += 1
        if good_number == 3:
            return True
    return False

# mozna to rowniez zrobic:
#     for win in all_win:
#         if set(win) <= set(turns):
#             return True
#     return False