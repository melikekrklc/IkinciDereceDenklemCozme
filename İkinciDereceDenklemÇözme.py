
def denklemÇözümü(a,b,c):#parantez içindeki abc ye gerek yok . Python kitabı sayfa 50 alıştırma 3 öyle istediği için yaptık .
    #yani sayıları önce argüman olarak gönderdik sonra ise bu sayıları kullanıcıdan isteyecek şekilde değiştirdik.
    b=input("b sayısı:")
    a=input("a sayısı:")
    c=input("c sayısı:")
    b_float=float(b)
    a_float=float(a)
    c_float=float(c)
    delta=(b_float**2)-(4*a_float*c_float)
    if delta>0:
       kök_1=((-(b_float))+(delta**(1/2)))/(2*(a_float))
       kök_2=((-(b_float))-(delta**(1/2)))/(2*(a_float))
       return kök_1,kök_2
    elif delta==0:
        Tek_kök=((-(b_float))+(delta**(1/2)))/(2*(a_float))
        return Tek_kök
    else:
       cevap= print("Denklemin reel çözümü yoktur.")
       return cevap

sonuc=denklemÇözümü(2,-5,-12)#parantez içindeki sayılar olmasada olur. Normal denklem çözümünde.
print("Denklemin çözümü:",sonuc)







