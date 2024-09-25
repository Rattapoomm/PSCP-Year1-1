'''Century'''
def twenty(num):
    '''sol'''
    for _ in range(num):
        txt = input().strip()

        if txt.startswith("B.E."):
            year = int(txt[5:])
            if year < 543:
                print("ERROR")
            else:
                # แปลงปี B.E. เป็นปี A.D.
                ad_year = year - 543
                # คำนวณศตวรรษ
                century = (ad_year + 99) // 100
                print(century)

        elif txt.startswith("A.D."):
            year = int(txt[5:])
            # คำนวณศตวรรษ
            century = (year + 99) // 100
            print(century)

        else:
            print("ERROR")

# รับจำนวนปีที่ต้องการประมวลผล
twenty(int(input()))
