def GenerateBBSTArray(a):
    def calcul_len_arr(len_a):
        BBST_len = 0
        H = 0
        while True:
            BBST_len = 2 ** (H + 1) - 1
            if BBST_len >= len_a:
                return BBST_len
            H += 1
    
    def Add_Key_rec(BBST, a_sort, indexs, pred=0):
        indexs_len = len(indexs)
        if indexs_len == 0:
            return
        centr = indexs[0] + indexs_len // 2

        BBST[pred] = a_sort[centr] 
        Add_Key_rec(BBST, a_sort, range(indexs[0], centr), (pred*2+ 1))
        Add_Key_rec(BBST, a_sort, range(centr + 1, (indexs[0] + indexs_len)), (pred*2 + 2))

    a_sort = sorted(a)
    a_sort_len = len(a_sort)
    BBST = [None] * calcul_len_arr(len(a))
    Add_Key_rec(BBST, a_sort, range(0, len(a_sort)))

    return BBST