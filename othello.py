# -----------------------------------------------------------------------------
# othello.py
# 横だけオセロ
# 
# -----------------------------------------------------------------------------
# 番号      更新履歴                                    日付        氏名
# -----------------------------------------------------------------------------
# 000000    新規作成                                    2018/04/18  中田　桂介
# -----------------------------------------------------------------------------
flag = 0
while flag == 0:                                 #プログラム全体のループ
# 初期化 ----------------------------------------------------------------------
    map = [2]*15                                #マップの初期化
    player = 0                                  #手番プレイヤーのコマ
    next_player = 1                             #次の手番プレイヤーのコマ
    pieces = ['●', '〇']                        #コマ
    val = 0
    white_piece = 0                             #白のコマの数
    black_piece = 0                             #黒のコマの数
# 1ゲーム開始 ------------------------------------------------------------------
    while 1:                                    #1ゲーム全体用のループ
# 表示部 ----------------------------------------------------------------------
        print('  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15')
        print('----------------------------------------------')
        for loop_count in range(15):
            if map[loop_count] == 2:
                print('|  ',end='')
            elif map[loop_count] == 0:
                print('|● ',end='')
            elif map[loop_count] == 1:
                print('|〇',end='')
        print('|')
        print('----------------------------------------------')
# 入力部 ----------------------------------------------------------------------
        print(pieces[player] + "さんの番です。何処にコマを置きますか？")
        while 1:
            input_pointer = input('→')
            pointer = int(input_pointer) - 1
            if pointer >= 0 and pointer <= 14:
                if map[pointer] == 2:
                    map[pointer] = player
                    break
                elif map[pointer] == 0 or map[pointer] == 1:
                    print("既に" + pieces[player] + 'が配置されています。再入力して下さい。')
            else:
                print("入力にミスがありました。再入力して下さい。")
# 左の石の状況を調べ、ひっくり返す ----------------------------------------------
        if pointer - 1 >= 0:
            if map[pointer - 1] == next_player:
                check = pointer - 2
                while 1:
                    if check < 0:
                        break
                    if map[check] == player:
                        while map[check + 1] == next_player:
                            map[check + 1] = player
                            check += 1
                        break
                    elif map[check] == next_player:
                        check -=1
                    else:
                        break
# 右の石の状況を調べ、ひっくり返す ----------------------------------------------
        if pointer + 1 < 14:
            if map[pointer + 1] == next_player:
                check = pointer + 2
                while 1:
                    if check > 14:
                        break
                    if map[check] == player:
                        while map[check - 1] == next_player:
                            map[check - 1] = player
                            check -= 1
                        break
                    elif map[check] == next_player:
                        check +=1
                    else:
                        break
# プレイヤーの手番変更 ---------------------------------------------------------
        val = player
        player = next_player
        next_player = val
# ゲーム終了するかの判定 -------------------------------------------------------
        white_piece = 0
        black_piece = 0
        for loop_count in range(15):
            if map[loop_count] == 0:
                white_piece += 1
            elif map[loop_count] == 1:
                black_piece += 1
        if (white_piece + black_piece) >= 15:
            break
# 表示部 ----------------------------------------------------------------------
    print('  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15')
    print('----------------------------------------------')
    for loop_count in range(15):
        if map[loop_count] == 2:
            print('|  ',end='')
        elif map[loop_count] == 0:
            print('|● ',end='')
        elif map[loop_count] == 1:
            print('|〇',end='')
    print('|')
    print('----------------------------------------------')
    if (white_piece + black_piece) >= 15:
        if white_piece > black_piece:
            print("●の勝ち！")
        else:
            print("〇の勝ち！")
# ゲームを続けるのか判定 -------------------------------------------------------
    print("ゲームを続けますか？")
    print("Y : YES / N : NO")
    while 1:
        choice = input("→")
        if choice == 'Y' or choice == 'y':
            break
        elif choice == 'N' or choice == 'n':
            flag = 1
            break
        else:
            print("入力にミスがありました。再入力して下さい。")
# ----------------------------------------------------------------------------
#              Copyright HAL College of Technology & Design
# ----------------------------------------------------------------------------