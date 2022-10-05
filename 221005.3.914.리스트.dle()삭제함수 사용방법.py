aa=[10,20,30]
del(aa[1])
print(aa)
#여러개의 항목 삭제하려면
#aa[시작:끝+1]=[]
#del(aa[시작:끝+1])
bb=[10,20,30,40,50]
bb[1:4]=[]
print(bb)
cc=[10,20,30,40,5]
del(cc[1:4])
print(cc)