def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    L = 0 #左端    
    R = len(sorted_array) - 1#右端
    
    while R >= L:    
        half = (L + R)//2#中央値取得
        if sorted_array[half]== target_number:
            return half
        elif sorted_array[half] > target_number:
            R = half-1
        else:
            L = half + 1

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()


# def binary_search(data, value):
#     left = 0            # 探索する範囲の左端を設定
#     right = len(data) - 1            # 探索する範囲の右端を設定
#     while left <= right:
#         mid = (left + right) // 2            # 探索する範囲の中央を計算
#         if data[mid] == value:
#             # 中央の値と一致した場合は位置を返す
#             return mid
#         elif data[mid] < value:
#             # 中央の値より大きい場合は探索範囲の左を変える
#             left = mid + 1
#         else:
#             # 中央の値より小さい場合は探索範囲の右を変える
#             right = mid - 1
#     return -1            # 見つからなかった場合

# data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(binary_search(data, 90))