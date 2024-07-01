from PIL import Image
import os
import csv

image_path = 'hd.jpg' 
image = Image.open(image_path)

dictionary=dict()

image = image.convert('RGB')

width, height = image.size
maxi=1
maxipix=image.getpixel((0, 0))
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        single_value = (r << 16) + (g << 8) + b
        if single_value in dictionary:
            dictionary[single_value]+=1
            if maxi<dictionary[single_value]:
                maxi=single_value
                maxipix=single_value
        else:
            dictionary[single_value]=1

coloursarr=[]    
for key in dictionary:
    coloursarr.append(key)

coloursarr.sort()

print(len(coloursarr))

filename = 'output.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    arr=[]
    init=coloursarr[0]
    idx=0
    for value in coloursarr:
        if idx==0:
            arr.append(value)
            idx=1
            continue
        arr.append(value-init)
        init=value
    init=arr[0]
    counter=1
    last_arr=[]
    idx=0
    for value in arr:
        if idx==0:
            idx=1
            continue
        if value!=init:
            temp=[]
            if counter>1:
                temp.append(init)
                temp.append(counter)
            else:
                temp.append(init)
            counter=1
            init=value
            last_arr.append(temp)
        else:
            counter+=1
    temp=[]
    if counter>1:
        temp.append(value)
        temp.append(counter)
    else:
        temp.append(value)
    counter=1
    last_arr.append(temp)
    writer.writerows(last_arr)

dic=dict()

icnt=0
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        single_value = (r << 16) + (g << 8) + b
        if single_value in dic:
            dic[single_value].append(icnt)
        else:
            dic[single_value]=[]
            dic[single_value].append(icnt)
        icnt+=1
        if icnt==16:
            icnt=0

cnt=1

byte_arr=[]
byte=0
for value in coloursarr:
    if value==maxipix:
        cnt+=1
        continue
    binary_string=""
    strlen=0
    index=0
    binarystr_arr=[]
    for item in dic[value]:
        index+=1
        binarystr_arr.append(str(item))
        strlen+=1
        if index==len(dic[value]) or strlen==2:
            
            strlen=0
            binary_string= format(int(binarystr_arr[0]), '08b')
            newbstr=""
            if len(binarystr_arr)==2:
                bstring=format(int(binarystr_arr[1]), '08b')
                flag=0
                ri=0
                for va in bstring:
                    if flag==1 or va=='1':
                        flag=1
                        newbstr+=va
                        ri+=1
                while ri<8:
                    newbstr+=binary_string[ri]
                    ri+=1
                ri=0
                flag=0
            else:
                newbstr=binary_string
            bdigit=[]
            for w in newbstr:
                if w=='1':
                    bdigit.append(True)
                else:
                    bdigit.append(False)
            for q in range(8):
                if bdigit[q]:
                    byte |= (1 << q)
            byte_arr.append(byte)
            byte=0
            binary_string=""
            newbstr=""
            bstring=""
    folder_name = 'binaryfolder'
    file_name = str(cnt)+'.bin'
    file_path = os.path.join(folder_name, file_name)
    cnt+=1
    with open(file_path, 'wb') as out_file:
        out_file.write(bytes(byte_arr))
    byte_arr=[]


