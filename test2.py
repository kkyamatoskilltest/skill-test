"""
スキルテスト2. 第一正規化の逆変換

コマンドライン引数は第一引数が入力ファイル名、第二引数が出力ファイル名とする。
"""

import csv
import sys

def check_args():
    """
    コマンドライン引数のチェックを行う
    """
    if len(sys.argv) != 3:
        print("次の形式で引数が必要です。\n $ python test1.py <input_file> <output_file>")
        exit(1)

if __name__ == '__main__':
    # コマンドライン引数のチェック
    check_args()
    # 標準入力から入出力ファイル名を受け取る
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # 入出力ファイルストリームを開く
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        reader = csv.reader(input_f, delimiter='\t')
        input_dict = {}
        # 入力された各行について、キーと値から辞書を作成する
        for input_row in reader:
            key = input_row[0]
            value = input_row[1]
            # すでにキーが存在している場合は辞書のキーに対応するリストに値を追加する
            if key in input_dict:
                input_dict[key].append(value)
            # キーが存在していない場合は入力された値を要素とするリストを辞書に追加する
            else:
                input_dict[key] = [value]
        # 辞書から出力するタブ区切りの文字列を作成し、ファイルに出力する
        for k, v in input_dict.items():
            output_row = "%s\t%s\n" % (k, ':'.join(v))
            output_f.write(output_row)
