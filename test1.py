"""
スキルテスト1. 第一正規化

コマンドライン引数は第一引数が入力ファイル名、第二引数が出力ファイル名とする。
"""

import copy
import csv
import sys

def check_args():
    """
    コマンドライン引数のチェックを行う
    """
    if len(sys.argv) != 3:
        print("次の形式で引数が必要です。\n $ python test1.py <input_file> <output_file>")
        exit(1)

def first_normalize(done, columns, res):
    """
    再帰を利用して第一正規化を行う

    Parameters
    ----------
    done: list
        正規化済みのデータ列
    columns: list
        正規化前のデータ列
    res: list
        最終的な正規化済みのデータ列の集合
    """
    # Pythonではリストは参照渡しとなるため、値の内容をコピーして使用する
    done_local = copy.deepcopy(done)
    columns_local = copy.deepcopy(columns)
    # 最終列まで正規化が終了した場合はresに追加し、それ以外は処理を継続する
    if len(columns) == 0:
        res.append(done_local)
    else:
        values = columns_local[0].split(':')
        columns_local.pop(0)
        # 1つのセルに複数の値が入っている場合は、それぞれについて再帰処理で正規化を行う
        for v in values:
            done_local.append(v)
            first_normalize(done_local, columns_local, res)
            # 現在注目している値の処理が終了したら配列から削除する
            done_local.pop(-1)

if __name__ == '__main__':
    # コマンドライン引数のチェック
    check_args()
    # 標準入力から入出力ファイル名を受け取る
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # 入出力ファイルストリームを開く
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        reader = csv.reader(input_f, delimiter='\t')
        writer = csv.writer(output_f, delimiter='\t')
        # TSVデータを各行ごとに第一正規化を行い、ファイルにTSV形式で出力する
        for input_row in reader:
            res = []
            first_normalize([], input_row, res)
            writer.writerows(res)
