import math 

#cho đơn vị cm

try:
    A =    int(input('Nhập tạo độ Ax: ')) , int(input('Ay: '))    
    B =    int(input('Nhập tạo độ Bx: ')) , int(input('By: '))    
    C =    int(input('Nhập tạo độ Cx: ')) , int(input('Cy: '))    

    print('Tạo độ A: ',(A))
    print('Tạo độ B: ',(B))
    print('Tạo độ C: ',(C))

    #vector:
    AB =   (B[0]-A[0], B[1]-A[1]) 
    CA =   (A[0]-C[0], A[1]-C[1]) 
    AC =   ( A[0]-C[0], -(A[1]-C[1]) ) 
    BC =   (C[0]-B[0], C[1]-B[1]) 

    print("Vector AB: ",AB)
    print("Vector AC: ",AC)
    print("Vector BC: ",BC)

    #Độ dài cạnh:
    c = math.sqrt(  (AB[0]) **2 + (AB [1]) **2  )
    a = math.sqrt(  (BC[0]) **2 + (BC [1])**2   )
    b = math.sqrt(  (CA[0]) **2 + (CA [1]) **2  )
except:
    print("ERROR! Try it later.") 
    exit()
value = []
tt_tam = []
H=[]
G=[]
G_H = []

def kiem_tra_tamgiac ():
    # CT: |b-c|  < a <  b + c

    if abs(b - c) < a < b + c :                                                                            
        print ("A: TRUE! A,B,C hợp thành 1 tam giác")                           
    else:
        print(" A: FALSE! A,B,C không hợp thành 1 tam giác")   
        exit()
    pass

def  canh_tamgiac():
    
    print(f"- Độ dài cạnh AB: {round(c,2)} cm")
    print(f"- Độ dài cạnh BC: {round(a,2)} cm")
    print(f"- Độ dài cạnh AC: {round(b,2)} cm")

    value.extend([int(c),int(a),int(b)])
 
def goc_tamgiac(toado_a, toado_b, toado_c):

    ang = math.degrees(math.atan2(toado_b[1]-toado_a[1], toado_b[0]-toado_a[0]) - math.atan2(toado_c[1]-toado_a[1], toado_c[0]-toado_a[0]))
    goc_a= ang + 360 if ang < 0 else ang
    if goc_a >=180:
            goc_a= goc_a - 180
    print("- Góc a: ", round(goc_a,2))   

    ang = math.degrees(math.atan2(toado_c[1]-toado_b[1], toado_c[0]-toado_b[0]) - math.atan2(toado_a[1]-toado_b[1], toado_a[0]-toado_b[0]))
    goc_b= ang + 360 if ang < 0 else ang
    if goc_a >=180:
            goc_b= goc_b - 180
    print("- Góc b: ", round(goc_b,2))   

    ang = math.degrees(math.atan2(toado_a[1]-toado_c[1], toado_a[0]-toado_c[0]) - math.atan2(toado_b[1]-toado_c[1], toado_b[0]-toado_c[0]))
    goc_c= ang + 360 if ang < 0 else ang
    if goc_c >=180:
            goc_c= goc_c - 180
    print("- Góc c: ", round(goc_c,2))  

    value.extend([goc_a,goc_b,goc_c])

def check_tamgiac():
 #Kiểm tra điều kiện tam giác:
    if abs(b - c) < a < b + c :
        # ĐK tam giác vuông - cân:      a^2 = b^2 + c^2
        if value[3] == 90 or value[4]==90 or value[5] == 90:
            loaiTamGiac = "- Tam giác vuông"
            if value[3] == 90:
                print("- Tam giác vuông tại: A")
            elif value[3] == 90 and a == b or a== c or c==b:
                    print('- Tam giác vuông cân tại: A')

            elif value[4]==90:
                print("- Tam giác vuông tại: B")
            elif value[4]==90 and a == b or a== c or c==b:
                print('- Tam giác vuông cân tại: B')    

            elif value[5] == 90:
                print('- Tam giác vuông tại: C')
            else:
                print('- Tam giác vuông cân tại: C')
        #ĐK tam giác đều:
        elif a==b and b==c:
            loaiTamGiac = '- Tam giác abc đều'
        #Đk tam giác cân:
        elif a==b or a==c or b==c:
            loaiTamGiac = '- Tam giác abc cân'
            if a==b:
                print("- Tam giác cân với đỉnh tại: C")
            elif a==c:
                print('- Tam giác cân với đỉnh tại: B')
            else:
                print('- Tam giác cân với đỉnh tại: A')
        #ĐK tam giác tù:         a^2 > b^2 + c^2
        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
            loaiTamGiac = '- Tam giác abc tù'
            if a*a > b*b+c*c:
                print('- Tam giác tù với đỉnh tại: A')
            elif b*b > a*a+c*c :
                print('- Tam giác tù với đỉnh tại: B')
            else:
                print('- Tam giác tù với đỉnh tại: A')
                
        #Các trường hợp còn tại là tam giác thường
        else:
            loaiTamGiac = '- Tam giác abc thường'
        #Xuat thong bao theo yeu cau
        print(f'- Ta có số đo: {a}, {b}, {c} là 3 cạnh 1 tam giác {loaiTamGiac}')

def dientich_chuvi_tamgiac ():
            #chuvi-dientich:
    cv=a+b+c
    p=cv/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print (f"- Chu vi tam giác abc : {round(cv,2)} cm")
    print (f"- Diện tích tam giác abc : {round(dt,2)} cm^2")
    value.extend([dt])
    pass

#output: value = [c,a,b,goc_a,goc_b,goc_c,dt]

def duongcao():
    # h = 2* S    /  độ dài c.đáy
    h_a = 2* value[6] / value[1]
    h_b = 2* value[6] / value [2]
    h_c = 2* value[6] / value [0]

    print(f"- Đường cao của tam giác abc đi từ đỉnh A: {round(h_a,2)} cm")
    print(f"- Đường cao của tam giác abc đi từ đỉnh B: {round(h_b,2)} cm")
    print(f"- Đường cao của tam giác abc đi từ đỉnh C: {round(h_c,2)} cm")

def trungtuyen_tamgiac():
    #tính độ dài đường trung tuyến đến tâm của tam giác ABC:
    # CT:   m_a =  sqrt( (2(b^2+c^2) - a^2) /4 )
    m_a = math.sqrt(  (2*(b**2+c**2) - a**2 ) /4 )
    m_b = math.sqrt(  (2*(a**2+c**2) - b**2)  /4 )
    m_c = math.sqrt(  (2*(b**2+a**2) - c**2 ) /4 )

    # độ dài đường trung tuyên đi đến tâm tam giác ABC:
    m_a_tam = 2/3 * m_a
    m_b_tam = 2/3 * m_b
    m_c_tam = 2/3 * m_c

    tt_tam.extend([round(m_a_tam,2),round(m_b_tam,2),round(m_c_tam,2)])
    print("- Độ dài đường trung tuyến đi từ đỉnh A,B,C đến tâm lần lượt là: ",tt_tam)

    pass

def tam_tamgiac():

    G_x = (A[0]+B[0]+C[0]) / 3
    G_y = (A[1]+B[1]+C[1]) / 3
    G.extend([G_x, G_y])                             #trọng tâm G
    print("- Trọng tâm G(x,y) của tam giác ABC lần lượt là: ",G)
                                                # Trực tâm H
        #CT:  vector: AH * Bc = 0        và vector:     CH * AB = 0
    try:
        H_x=  float( -C[0]*AB[0]-C[1]*AB[1]+AB[1]*((A[0]*BC[0]+AC[1]*BC[1])/BC[1]) / ( BC[0]*AB[1]-AB[0]*BC[1]) /BC[1]  ) 
        H_y =   (H_x * AB[0] - C[0]*AB[0]-C[1]*AB[1]) / (AB[1] * (-1))
        
    except:
        H_x = ( A[0]+C[0] ) /2
        H_y =  ( A[1]+C[1] )/2
        H = [H_x,H_y]
        
        if value[3] == 90 or value[4]==90 or value[5] == 90:
            if value[3] == 90 and a == b or a== c or c==b:
                print('- Tam giác vuông cân tại: A  => H trung điểm của BC')
                print('- Trực tâm H(x,y) của tam giác ABC lần lượt là: ',H)

            elif value[4]==90 and a == b or a== c or c==b:
                print('- Tam giác vuông cân tại: B  => H trung điểm của AC')    
                print("- Trực tâm H(x,y) của tam giác ABC lần lượt là: ", H)

            else:
                print('- Tam giác vuông cân tại: C  => H trung điểm của AB' )
                print('- Trực tâm H(x,y) của tam giác ABC lần lượt là: ',H)
    else: 
        H = [H_x,H_y]
        print("- Trực tâm H(x,y) lần lượt là: ",H)


    G_H.extend([G,H])
    print('')
    print( "- Trọng tâm G và trực tâm H của tam giác ABC theo lần lượt [G_x,G_y], [H_x,H_y] là: ", G_H)

def giaima_tamgiac():
    print('    1.SỐ ĐO ĐƠN GIẢN CỦA 1 TAM GIÁC:')
    canh_tamgiac()
    goc_tamgiac(A,B,C)

    print('    2. DIỆN TÍCH VÀ CHU VI CỦA TAM GIÁC ABC: C.ABC & S.ABC')
    check_tamgiac()
    dientich_chuvi_tamgiac ()

    print('    3. SỐ ĐO NÂNG CAO CỦA TAM GIÁC ABC:')
    duongcao()
    trungtuyen_tamgiac()

    print('    4.TOẠ ĐỘ CỦA 1 SỐ ĐIỂM ĐẶC BIỆT CỦA TAM GIÁC ABC:')
    tam_tamgiac()
    pass

#OUTPUT:
print("=="*27)
print(" ")
print("Câu a:")
kiem_tra_tamgiac()

print(" ")
print('Câu b_1:')
canh_tamgiac()
print('Câu b_2:')
goc_tamgiac(A,B,C)

print(" ")
print("Câu c:")
check_tamgiac()

print(" ")
print('Câu d: ')
dientich_chuvi_tamgiac ()

print(" ")
print('Câu e:')
duongcao()

print(" ")
print('Câu f:')
trungtuyen_tamgiac()

print(" ")
print('Câu g:')
tam_tamgiac()

print("=="*27)
giaima_tamgiac()