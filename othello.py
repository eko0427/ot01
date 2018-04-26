# -----------------------------------------------------------------------------
# othello.py
# 横だけオセロ
# 
# -----------------------------------------------------------------------------
# 番号      更新履歴                                    日付        氏名
# -----------------------------------------------------------------------------
# 000000    新規作成                                    2018/04/18  中田　桂介
# 000001    関数化                                      2018/04/22  中田　桂介
# 000002    input時のValueError回避                     2018/04/23  中田　桂介
# 000003    定数の宣言、終了判定の変更、プレイヤーの入れ替えの変更
#                                                       2018/04/23　中田　桂介
# 000003    PIECESをdict型に変更
# -----------------------------------------------------------------------------

# 表示部 ----------------------------------------------------------------------
def othello_display(map, PIECES, MAP_SIZE):
    print('  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15')
    print('----------------------------------------------')
    for loop_count in range(15):            #コマ表示用に15回ループ
        print('|' + PIECES[map[loop_count]],end='')
    print('|')
    print('----------------------------------------------')
# 入力部 ----------------------------------------------------------------------
def othello_input(map, PIECES, player, game_flag, SPACE, SIZE):
    print(PIECES[player] + "さんの番です。何処にコマを置きますか？")
    while 1:                                #入力ミスした時用のループ
        input_pointer = input('→')          #数値を入力してもらう
        try:
            pointer = int(input_pointer) - 1
            if pointer >= SPACE and pointer <= SIZE:#入力された値がマップ内か判定
                if map[pointer] == SPACE:       #入力された場所が空白か判定
                    map[pointer] = player   #空白だった場合コマを配置
                    game_flag += player     #勝敗付のためにプレイヤーによって+か-する
                    break
                elif map[pointer] == -1 or map[pointer] == 1:#空白以外だった場合の判定
                    print("既に" + PIECES[player] + 'が配置されています。再入力して下さい。')
            else:                           #数値以外を入力した場合下記を表示する
                print("入力にミスがありました。再入力して下さい。")
        except ValueError:
            print("入力にミスがありました。再入力して下さい。")
    return map, pointer, game_flag
# 左の石の状況を調べ、ひっくり返す ----------------------------------------------
def othello_overturn(map, pointer, player, game_flag, SPACE, SIZE):
    if pointer - 1 >= SPACE:                    #マップ外に出ていないかを判定
        if map[pointer - 1] == player*-1:   #左の石が相手のコマを判定
            check = pointer - 2             #今どこにいるのかのポインタ
            while 1:                        #複数個ひっくり返すためのループ
                if check < SPACE:               #ポインタがマップ外に出ていないか判定
                    break
                if map[check] == player:    #次に自分が来たかを判定
                    while map[check + 1] == player*-1:#挟んだコマをひっくり返すまで回す
                        map[check + 1] = player#ポインタから一つ右のコマをひっくり返す
                        game_flag += player #勝敗付のためにプレイヤーによって+か-する
                        check += 1          #ポインタを進める
                    break
                elif map[check] == player*-1:#次に相手のコマが来たか判定
                    check -=1               #ポインタを進める
                else:                       #それ以外だった場合ループをやめる
                    break
# 右の石の状況を調べ、ひっくり返す ----------------------------------------------
    if pointer + 1 < SIZE:                    #マップ外に出ていないかを判定
        if map[pointer + 1] == player*-1:   #右の石が相手のコマを判定
            check = pointer + 2             #今どこにいるのかのポインタ
            while 1:                        #複数個ひっくり返すためのループ
                if check > SIZE:              #ポインタがマップ外に出ていないか判定
                    break
                if map[check] == player:    #次に自分が来たかを判定
                    while map[check - 1] == player*-1:#挟んだコマをひっくり返すまで回す
                        map[check - 1] = player#ポインタから一つ左のコマをひっくり返す
                        game_flag += player #勝敗付のためにプレイヤーによって+か-する
                        check -= 1          #ポインタを進める
                    break
                elif map[check] == player*-1:#次に相手のコマが来たか判定
                    check +=1               #ポインタを進める
                else:                       #それ以外だった場合ループをやめる
                    break
    return map, game_flag
# プレイヤーの手番変更 ---------------------------------------------------------
def player_change(player):
    player *= -1
    return player
# ゲームを続けるのか判定 -------------------------------------------------------
def othello_choice(flag):
    print("ゲームを続けますか？")
    print("Y : YES / N : NO")
    while 1:                                #入力ミスした時用のループ
        choice = input("→")
        if choice == 'Y' or choice == 'y':  #入力された値がYだった場合続行
            break
        elif choice == 'N' or choice == 'n':#入力された値がNだった場合終了
            flag = 1                        #全体のループの終了
            break
        else:                               #入力ミスした場合下記を表示
            print("入力にミスがありました。再入力して下さい。")
    return flag

if __name__ == "__main__":
# 定数の宣言 ------------------------------------------------------------------
    PIECES = {1:'● ', -1:'〇', 0:'　'}      #コマ表示用のリスト
    MAP_SIZE = 15                           #mapのサイズ
    SIZE = 14
    SPACE = 0
# ゲームスタート --------------------------------------------------------------
    flag = 0
    while flag == 0:                        #プログラム全体のループ
# 初期化 ----------------------------------------------------------------------
        map = [SPACE for loop_count in range(MAP_SIZE)]#マップの初期化
        player = 1                          #手番プレイヤーのコマ
        pointer = 0                         #探索中の自分の場所
        game_flag = 0                       #勝敗用のフラグ
# 1ゲーム開始 ------------------------------------------------------------------
        for loop_count in range(MAP_SIZE):  #1ゲーム全体用のループ
            othello_display(map, PIECES, MAP_SIZE)
            map, pointer, game_flag = othello_input(map, PIECES, player, game_flag, SPACE, SIZE)
            map, game_flag = othello_overturn(map, pointer, player, game_flag, SPACE, SIZE)
# プレイヤーの手番変更 ---------------------------------------------------------
            player = player_change(player)
# 表示部 ----------------------------------------------------------------------
        othello_display(map, PIECES, MAP_SIZE)
        if game_flag >= 1:                  #game_flagの数値によって勝敗の判定
            print("●の勝ち！")
        else:
            print("〇の勝ち！")
        flag = othello_choice(flag)
# ----------------------------------------------------------------------------
#              Copyright HAL College of Technology & Design
# ----------------------------------------------------------------------------