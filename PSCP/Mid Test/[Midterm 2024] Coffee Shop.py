'''Coffee Shop'''
def store(a, b, c, d, e):
    '''sol'''
    #a ราคาต่อแก้ว
    #b ลดหลังจากซื้อแก้วแรก
    #c ลดราคา หาก ซื้อ d บาท
    #d ต้องซื้อถึงลด
    #e จำนวนที่ต้องการ
    total_b = 0
    percent_pro_a = b*0.01 #เปอร์เซนลด
    dis_a = a*percent_pro_a #ราคาที่ลด
    price_a = (a-dis_a)*(e-1)
    one_pro = price_a+a
    #ส่วนของ B
    percent_pro_b = c*0.01
    pro_b = e*a
    dis_b = pro_b*percent_pro_b
    if pro_b >= d:
        total_b = pro_b-dis_b
    else:
        total_b = pro_b
    if one_pro < total_b:
        print("1")
        print(f'{one_pro:.2f}')
    elif one_pro > total_b:
        print("2")
        print(f'{total_b:.2f}')
    elif one_pro == total_b:
        print("2")
        print(f'{total_b:.2f}')
store(float(input()),float(input()),float(input()),float(input()),int(input()))