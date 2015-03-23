import binascii
import re
import binascii

def Byte_Hex_8bit_12bit_Dec( byteStr ):
    raw_list = [ x for x in byteStr];
    
    #Convert hex format into 2 digit formatt, e.g. 0x61 -> 61
    hex_list = [ "%02X" % ord(x) if "\\x" in r"%r" % x else x for x in byteStr ];
    
    #convert hex values into 8-bit binary
    bin_list=[];
    for x in hex_list[:-1]:
        if len(x)==2:
            bin_list.append( str(bin(int(x,16))[2:]).zfill(8));
        elif len(x)==1:
            bin_list.append(bin(int(binascii.hexlify(x),16))[2:].zfill(8));
        else:
            bin_list.append(x)
            
    #Combine three 8-bits into two 12-bits binary
    bin_12 = [];
    l = range((len(bin_list)/3)*3);
    for i in l[0::3]:
        print i, i+2;
        bit24 = ''.join(bin_list[i:i+3]);
        bin_12.append(bit24[:len(bit24)/2]);
        bin_12.append(bit24[len(bit24)/2:]);
    if len(bin_list)%3==2:
        bin_remain = ''.join(bin_list[-2:]);
        bin_12.append(bin_remain[0:12]);

    #Convert 12-bits into decimal value
    dec_list = [];
    for i in bin_12:
        dec_list.append(int(i, 2));
    return dec_list;

##    #Convert decimal value into ascii (Only for 'Hello, World!' though)
##    ascii_list = [];
##    for i in dec_list:
##        ascii_list.append(chr(i));
##    return ''.join(ascii_list);
##    ascii_list.append(hex_list[-1])    

with open('file.z',"rb") as f:
    for line in f:
##        print(int(line.encode("hex"), 16));
        print Byte_Hex_8bit_12bit_Dec(line);


