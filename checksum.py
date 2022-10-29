def calculaCheckSum(pBuff):
    checksum = 0
    a = ''
    for i in pBuff:    
        checksum = checksum ^ ord(i) 
        # print(checksum)
        # i = i+1
        if a==';' and i == '*':
            break
        a = i

    return hex(checksum)
# RPU00280522050104+0000000+000000000FF0000000000C000001112301311N00000000+24100722007118C76EF_GG000000000;ID=KX93;#000C;*	

if __name__ == "__main__":
    print(calculaCheckSum(">SIDFC67;ID=FC68;#0819;*7b<"))