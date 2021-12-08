def NumberRegister(r):
    if r == "$zero" or r == "$0":
        return 0
    elif r == "$at" or r == "$1":
        return 1
    elif r == "$v0" or r == "$2":
        return 2
    elif r == "$v1" or r == "$3":
        return 3
    elif r == "$a0" or r == "$4":
        return 4
    elif r == "$a1" or r == "$5":
        return 5
    elif r == "$a2" or r == "$6":
        return 6
    elif r == "$a3" or r == "$7":
        return 7
    elif r == "$t0" or r == "$8":
        return 8
    elif r == "$t1" or r == "$9":
        return 9
    elif r == "$t2" or r == "$10":
        return 10
    elif r == "$t3" or r == "$11":
        return 11
    elif r == "$t4" or r == "$12":
        return 12
    elif r == "$t5" or r == "$13":
        return 13
    elif r == "$t6" or r == "$14":
        return 14
    elif r == "$t7" or r == "$15":
        return 15
    elif r == "$s0" or r == "$16":
        return 16
    elif r == "$s1" or r == "$17":
        return 17
    elif r == "$s2" or r == "$18":
        return 18
    elif r == "$s3" or r == "$19":
        return 19
    elif r == "$s4" or r == "$20":
        return 20
    elif r == "$s5" or r == "$21":
        return 21
    elif r == "$s6" or r == "$22":
        return 22
    elif r == "$s7" or r == "$23":
        return 23
    elif r == "$t8" or r == "$24":
        return 24
    elif r == "$t9" or r == "$25":
        return 25
    elif r == "$k0" or r == "$26":
        return 26
    elif r == "$k1" or r == "$27":
        return 27
    elif r == "$gp" or r == "$28":
        return 28
    elif r == "$sp" or r == "$29":
        return 29
    elif r == "$fp" or r == "$30":
        return 30
    elif r == "$ra" or r == "$31":
        return 31

def DecimalToBinary(num, result):
    if num >= 1:
        DecimalToBinary(num // 2, result)
        result.append(str(num % 2))
    s = "".join(result)
    return s

def NegativeBinary(b):
    a = []
    for i in range(len(b)):
        if b[i] == "0":
            a.append("1")
        else:
            a.append("0")
    s = "".join(a)
    c = int(s,2) + 1
    return bin(c)[2:].zfill(len(b))

def DeleleComment():
    count = 0
    comma = False
    emty = ""

    # clear data
    e = open("temp.txt", "w")
    e.write(emty)
    e.close()
    e = open("temp_sc.txt", "w")
    e.write(emty)
    e.close()
    e = open("output.txt", "w")
    e.write(emty)
    e.close()
    e = open("hex.txt", "w")
    e.write(emty)
    e.close()

    e = open("input.txt", "r")
    inp = open("input.txt", "r")
    output = open("temp.txt", "a")
    lines = open("input.txt", "r").read().split("\n")


    isEmty = e.read()
    if isEmty == "":
        e.close()
        return True

    for i in range(len(lines)):
        temp = inp.readline().split()
        if str(temp)[1] == "'": # delete blank lines
            if temp[0][0] != "#":  # delete comments
                for j in range(len(temp)):
                    if temp[j][0] == "#":
                        break
                    for k in range(len(temp[j])):
                        if comma == True:
                            output.write(" ")
                        comma = False
                        if temp[j][k] == "," and k < len(temp[j]) - 1:
                            comma = True
                        output.write(str(temp[j][k]))
                    output.write(" ")
                if i+1 < len(lines):
                    count += 1
                    output.write("\n")
    inp.close()
    output.close()
    # special cases (the last line is null)
    sc = False
    inp_sc = open("temp.txt", "r")
    output_sc = open("temp_sc.txt", "a")
    for i in range(count+1):
        temp_sc = inp_sc.readline().split()
        if str(temp_sc)[1] == "'":
            for j in range(len(temp_sc)):
                output_sc.write(str(temp_sc[j] + " "))
            if i+2 < (count+1):
                    output_sc.write("\n")
        else:
            sc = True
    
    if sc == True:
        inp_sc.close()
        output_sc.close()
        inp_sc = open("temp_sc.txt", "r")
        output_sc = open("temp.txt", "w")
        output_sc.write(inp_sc.read())
        inp_sc.close()
        output_sc.close()

def StoreLabel(lines):
    address = 4194300
    line_num = 0
    label = [[]]
    label_name = ""

    inp_check_label = open("temp.txt", "r")
    inp = open("temp.txt", "r")

    for i in range(lines):
        check_label = inp_check_label.readline()
        temp = inp.readline().split()

        address += 4
        line_num += 1
        if ":" in check_label:
            label_line_num = line_num
            label_address = address
            label_name = check_label[:-2].strip(":")
            label.append([label_line_num,label_address, label_name])
        if temp[0] == "la" or temp[0] == "blt" or temp[0] == "bgt" or temp[0] == "ble" or temp[0] == "bge":
            line_num += 1
            #label_line_num = line_num
    
    inp.close()
    inp_check_label.close()
    return label

def GenerateHex():
    hex = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
    result = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    inp = open("output.txt", "r")
    output = open("hex.txt", "a")
    lines = open("output.txt", "r").read().split("\n")
    st = open("output.txt", "r")
    for i in range(len(lines) - 1):
        s = st.readline()
        output.write("0x")
        for j in range(0,32,4):
            temp = s[j:j+4]
            for k in range(len(hex)):
                if temp == hex[k]:
                    output.write(result[k])
        output.write("\n")

def GenerateBinary():
    # variable
    opcode = ""
    rs = ""
    rt = ""
    rd = ""
    shamt = ""
    funct = ""
    immediate = ""
    ad = ""
    result = []
    len_rs = 5
    len_rd = 5
    len_rt = 5
    len_shamt = 5
    len_immediate = 16
    len_ad = 26
    _type = ""
    address = 4194300
    line_num = 0

    # code
    inp = open("temp.txt", "r")
    inp_check_label = open("temp.txt", "r")
    lines = open("temp.txt", "r").read().split("\n")
    label = StoreLabel(len(lines))

    for i in range(len(lines)):
        rd_tobin = []
        rs_tobin = []
        rt_tobin = []
        shamt_tobin = []
        immediate_tobin = []
        ad_tobin = []
        rs1_tobin = []
        rt1_tobin = []
        immediate1_tobin = []

        check = False
        
        check_label = inp_check_label.readline()
        temp = inp.readline().split()

        address += 4
        line_num += 1

        if ":" in check_label:
            islabel = True            
        else:
            islabel = False

        if islabel == False:
            print(temp)
            # R-Type
            if temp[0] == "add":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100000"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "addu":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100001"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "sub":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100010"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "subu":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100011"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "and":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100100"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "jr":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "001000"
                rs = temp[1].strip(",")
                rd = "$zero"
                rt = "$zero"
            elif temp[0] == "nor":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100111"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "or":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100101"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "slt":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "101010"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "sltu":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "101011"
                rd = temp[1].strip(",")
                rs = temp[2].strip(",")
                rt = temp[3].strip(",")
            elif temp[0] == "sll":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = temp[3].strip(",")
                funct = "000000"
                rd = temp[1].strip(",")
                rs = "$zero"
                rt = temp[2].strip(",")
            elif temp[0] == "srl":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = temp[3].strip(",")
                funct = "000010"
                rd = temp[1].strip(",")
                rs = "$zero"
                rt = temp[2].strip(",")
            elif temp[0] == "div":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "011010"
                rd = "$zero"
                rs = temp[1].strip(",")
                rt = temp[2].strip(",")
            elif temp[0] == "divu":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "011011"
                rd = "$zero"
                rs = temp[1].strip(",")
                rt = temp[2].strip(",")
            elif temp[0] == "mflo":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "010010"
                rd = temp[1].strip(",")
                rs = "$zero"
                rt = "$zero"
            elif temp[0] == "mfhi":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "010000"
                rd = temp[1].strip(",")
                rs = "$zero"
                rt = "$zero"
            elif temp[0] == "mfc0":
                check = True
                _type = "R"
                opcode = "010000"
                shamt = "00000"
                funct = "000000"
                rd = temp[2].strip(",")
                rs = "$zero"
                rt = temp[1].strip(",")
            elif temp[0] == "mult":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "011000"
                rd = "$zero"
                rs = temp[1].strip(",")
                rt = temp[2].strip(",")
            elif temp[0] == "multu":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "011001"
                rd = "$zero"
                rs = temp[1].strip(",")
                rt = temp[2].strip(",")
            elif temp[0] == "sra":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = temp[3].strip(",")
                funct = "000011"
                rd = temp[1].strip(",")
                rs = "$zero"
                rt = temp[2].strip(",")

            # I-Type
            if temp[0] == "addi":
                check = True
                _type = "I"
                opcode = "001000"
                rt = temp[1].strip(",")
                rs = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "addiu":
                check = True
                _type = "I"
                opcode = "001001"
                rt = temp[1].strip(",")
                rs = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "andi":
                check = True
                _type = "I"
                opcode = "001100"
                rt = temp[1].strip(",")
                rs = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "beq":
                check = True
                _type = "I"
                opcode = "000100"
                rs = temp[1].strip(",")
                rt = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "bne":
                check = True
                _type = "I"
                opcode = "000101"
                rs = temp[1].strip(",")
                rt = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "lw":
                check = True
                _type = "I"
                opcode = "100011"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "lbu":
                check = True
                _type = "I"
                opcode = "100100"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "lhu":
                check = True
                _type = "I"
                opcode = "100101"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "ll":
                check = True
                _type = "I"
                opcode = "110000"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "lui":
                check = True
                _type = "I"
                opcode = "001111"
                rt = temp[1].strip(",")
                rs = "$zero"
                immediate = temp[2].strip(",")
            elif temp[0] == "ori":
                check = True
                _type = "I"
                opcode = "001101"
                rt = temp[1].strip(",")
                rs = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "slti":
                check = True
                _type = "I"
                opcode = "001010"
                rt = temp[1].strip(",")
                rs = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "sltiu":
                check = True
                _type = "I"
                opcode = "001011"
                rt = temp[1].strip(",")
                rs = temp[2].strip(",")
                immediate = temp[3].strip(",")
            elif temp[0] == "sw":
                check = True
                _type = "I"
                opcode = "101011"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "sb":
                check = True
                _type = "I"
                opcode = "101000"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "sc":
                check = True
                _type = "I"
                opcode = "111000"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "sh":
                check = True
                _type = "I"
                opcode = "101001"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "lwc1":
                check = True
                _type = "I"
                opcode = "110001"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "ldc1":
                check = True
                _type = "I"
                opcode = "110101"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "swc1":
                check = True
                _type = "I"
                opcode = "111001"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]
            elif temp[0] == "sdc1":
                check = True
                _type = "I"
                opcode = "111101"
                rt = temp[1].strip(",")
                rs = temp[2].split("(")[1].strip(")")
                immediate = temp[2].split("(")[0]

            # J-type
            if temp[0] == "j":
                check = True
                _type = "J"
                opcode = "000010"
                ad = temp[1].strip(",")
            elif temp[0] == "jal":
                check = True
                _type = "J"
                opcode = "000011"
                ad = temp[1].strip(",")
            
            # pseudo
            if temp[0] == "li":
                check = True
                _type = "P"
                opcode = "001001"
                rt = temp[1].strip(",")
                rs = "$zero"
                immediate = temp[2].strip(",")
            elif temp[0] == "move":
                check = True
                _type = "R"
                opcode = "000000"
                shamt = "00000"
                funct = "100001"
                rd = temp[1].strip(",")
                rs = "$0"
                rt = temp[2].strip(",")
            elif temp[0] == "la":
                check = True
                _type = "P"
                opcode1 = "001111"
                rt1 = "$1"
                rs1 = "$zero"
                immediate1 = "64"
                line_num += 1
                opcode2 = "001101"
                rt2 = temp[1].strip(",")
                rs2 = "$1"
                immediate2 = temp[2].strip(",")
            elif temp[0] == "blt":
                check = True
                _type = "P"
                opcode1 = "000000"
                shamt = "00000"
                funct = "101010"
                rd1 = "$1"
                rs1 = temp[1].strip(",")
                rt1 = temp[2].strip(",")
                line_num += 1
                opcode2 = "000101"
                rs2 = "$1"
                rt2 = "$0"
                immediate = temp[3].strip(",")
            elif temp[0] == "bgt":
                check = True
                _type = "P"
                opcode1 = "000000"
                shamt = "00000"
                funct = "101010"
                rd1 = "$1"
                rs1 = temp[2].strip(",")
                rt1 = temp[1].strip(",")
                line_num += 1
                opcode2 = "000101"
                rs2 = "$1"
                rt2 = "$0"
                immediate = temp[3].strip(",")
            elif temp[0] == "ble":
                check = True
                _type = "P"
                opcode1 = "000000"
                shamt = "00000"
                funct = "101010"
                rd1 = "$1"
                rs1 = temp[2].strip(",")
                rt1 = temp[1].strip(",")
                line_num += 1
                opcode2 = "000100"
                rs2 = "$1"
                rt2 = "$0"
                immediate = temp[3].strip(",")
            elif temp[0] == "bge":
                check = True
                _type = "P"
                opcode1 = "000000"
                shamt = "00000"
                funct = "101010"
                rd1 = "$1"
                rs1 = temp[1].strip(",")
                rt1 = temp[2].strip(",")
                line_num += 1
                opcode2 = "000100"
                rs2 = "$1"
                rt2 = "$0"
                immediate = temp[3].strip(",")

            # syscall
            if temp[0] == "syscall":
                check = True
                _type = "sys"
          
            if check == False:
                print("'" + temp[0] + "'" + " is not a recognized operator")
                print("*****EROR*****")
                return ""
                      
            # Generate into bit
            if temp[0] == "la":
                rs1_dec = NumberRegister(rs1)
                rt1_dec = NumberRegister(rt1)
                rs2_dec = NumberRegister(rs2)
                rt2_dec = NumberRegister(rt2)

                rs1_bin = DecimalToBinary(rs1_dec, rs_tobin)
                rt1_bin = DecimalToBinary(rt1_dec, rt_tobin)
                rs2_bin = DecimalToBinary(rs2_dec, rs1_tobin)
                rt2_bin = DecimalToBinary(rt2_dec, rt1_tobin)            
            elif temp[0] == "blt" or temp[0] == "bgt" or temp[0] == "ble" or temp[0] == "bge":
                rs1_dec = NumberRegister(rs1)
                rt1_dec = NumberRegister(rt1)
                rs2_dec = NumberRegister(rs2)
                rt2_dec = NumberRegister(rt2)
                rd1_dec = NumberRegister(rd1)

                rd1_bin = DecimalToBinary(rd1_dec, rd_tobin)
                rs1_bin = DecimalToBinary(rs1_dec, rs_tobin)
                rt1_bin = DecimalToBinary(rt1_dec, rt_tobin)
                rs2_bin = DecimalToBinary(rs2_dec, rs1_tobin)
                rt2_bin = DecimalToBinary(rt2_dec, rt1_tobin) 

            else:
                if _type == "R":
                    rd_dec = NumberRegister(rd)
                    rd_bin = DecimalToBinary(rd_dec, rd_tobin)
                if _type != "J":
                    rs_dec = NumberRegister(rs)
                    rt_dec = NumberRegister(rt)

                    rs_bin = DecimalToBinary(rs_dec, rs_tobin)
                    rt_bin = DecimalToBinary(rt_dec, rt_tobin)
                
            if _type == "R":
                if shamt != "00000":
                    shamt = DecimalToBinary(int(shamt), shamt_tobin)
            elif _type == "I":
                if immediate.isdigit() == True:
                    immediate_bin = DecimalToBinary(int(immediate), immediate_tobin)
                else:
                    if immediate[0] == "-":
                        immediate_temp = -1
                        immediate_bin = DecimalToBinary(abs(int(immediate)), immediate_tobin)
                        immediate_bin = NegativeBinary(immediate_bin)
                    else:
                        for k in range(1, len(label)):
                            if immediate == label[k][2]:
                                a = 0
                                for l in range(1, len(label)):
                                    if label[k][0] < label[l][0] < line_num or line_num < label[l][0] < label[k][0]:
                                        a += 1
                                immediate_temp = label[k][0] - line_num
                                if immediate_temp >= 0:
                                    immediate_bin = DecimalToBinary(immediate_temp - 1 - a, immediate_tobin)
                                else:
                                    immediate_bin = DecimalToBinary(abs(immediate_temp) - a, immediate_tobin)
                                    immediate_bin = NegativeBinary(immediate_bin)
            elif _type == "J":
                for l in range(1, len(label)):
                    if ad == label[l][2]:
                        ad = label[l][1]
                        ad_bin = DecimalToBinary(ad, ad_tobin)
            elif _type == "P":
                if temp[0] == "li":
                    if immediate.isdigit() == True:
                        immediate_bin = DecimalToBinary(int(immediate), immediate_tobin)
                    else:
                        if immediate[0] == "-":
                            immediate_temp = -1
                            immediate_bin = DecimalToBinary(abs(int(immediate)), immediate_tobin)
                            immediate_bin = NegativeBinary(immediate_bin)                
                elif temp[0] == 'la':
                    immediate1_bin = DecimalToBinary(int(immediate1), immediate_tobin)
                    for k in range(1, len(label)):
                        if immediate2 == label[k][2]:
                            if line_num >= label[k][0]:
                                immediate_temp = (label[k][0]-1) * 4
                                immediate2_bin = DecimalToBinary(abs(immediate_temp), immediate1_tobin)
                            else:
                                immediate_temp = label[k][0] * 4
                                immediate2_bin = DecimalToBinary(abs(immediate_temp), immediate1_tobin)
                elif temp[0] == "blt" or temp[0] == "bgt" or temp[0] == "ble" or temp[0] == "bge":
                    for k in range(1, len(label)):
                        if immediate == label[k][2]:
                            a = 0
                            for l in range(1, len(label)):
                                if label[k][0] < label[l][0] < line_num or line_num < label[l][0] < label[k][0]:
                                        a += 1
                            immediate_temp = label[k][0] - line_num
                            if immediate_temp >= 0:
                                immediate_bin = DecimalToBinary(immediate_temp - 1 - a, immediate_tobin)
                            else:
                                immediate_bin = DecimalToBinary(abs(immediate_temp) - a, immediate_tobin)
                                immediate_bin = NegativeBinary(immediate_bin)

            # fill bit
            if _type == "R":
                if (len_rd - len(rd_bin)) > 0:
                    rd_bin = (len_rd - len(rd_bin)) * "0" + rd_bin
                if (len_rs - len(rs_bin)) > 0:
                    rs_bin = (len_rs - len(rs_bin)) * "0" + rs_bin
                if (len_rt - len(rt_bin)) > 0:
                    rt_bin = (len_rt - len(rt_bin)) * "0" + rt_bin
                if (len_shamt - len(shamt)) > 0:
                    shamt = (len_shamt - len(shamt)) * "0" + shamt
            elif _type == "I":
                if (len_rs - len(rs_bin)) > 0:
                    rs_bin = (len_rs - len(rs_bin)) * "0" + rs_bin
                if (len_rt - len(rt_bin)) > 0:
                    rt_bin = (len_rt - len(rt_bin)) * "0" + rt_bin
                if immediate.isdigit() == True:
                    if (len_immediate - len(immediate_bin) > 0):
                        immediate_bin = (len_immediate - len(immediate_bin)) * "0" + immediate_bin
                else:
                    if immediate_temp >= 0:
                        if (len_immediate - len(immediate_bin) > 0):
                            immediate_bin = (len_immediate - len(immediate_bin)) * "0" + immediate_bin
                    else:
                        if (len_immediate - len(immediate_bin) > 0):
                            immediate_bin = (len_immediate - len(immediate_bin)) * "1" + immediate_bin
            elif _type == "J":
                if (len_ad - len(ad_bin) > 0):
                    ad_bin = (len_ad - len(ad_bin)) * "0" + ad_bin
            elif _type == "P":
                if temp[0] == "la":
                    if (len_rs - len(rs1_bin)) > 0 :
                        rs1_bin = (len_rs - len(rs1_bin)) * "0" + rs1_bin
                    if (len_rt - len(rt1_bin)) > 0:
                        rt1_bin = (len_rt - len(rt1_bin)) * "0" + rt1_bin
                    if (len_rs - len(rs2_bin)) > 0 :
                        rs2_bin = (len_rs - len(rs2_bin)) * "0" + rs2_bin
                    if (len_rt - len(rt2_bin)) > 0:
                        rt2_bin = (len_rt - len(rt2_bin)) * "0" + rt2_bin
                    if (len_immediate - len(immediate1_bin) > 0):
                        immediate1_bin = (len_immediate - len(immediate1_bin)) * "0" + immediate1_bin
                    if (len_immediate - len(immediate2_bin) > 0):
                        immediate2_bin = (len_immediate - len(immediate2_bin)) * "0" + immediate2_bin
                elif temp[0] == "li": 
                    if (len_rs - len(rs_bin)) > 0:
                        rs_bin = (len_rs - len(rs_bin)) * "0" + rs_bin
                    if (len_rt - len(rt_bin)) > 0:
                        rt_bin = (len_rt - len(rt_bin)) * "0" + rt_bin
                    if immediate.isdigit() == True:
                        if (len_immediate - len(immediate_bin) > 0):
                            immediate_bin = (len_immediate - len(immediate_bin)) * "0" + immediate_bin
                    else:
                        if (len_immediate - len(immediate_bin) > 0):
                            immediate_bin = (len_immediate - len(immediate_bin)) * "1" + immediate_bin
                elif temp[0] == "blt" or temp[0] == "bgt" or temp[0] == "ble" or temp[0] == "bge":
                    if (len_rd - len(rd1_bin)) > 0:
                        rd1_bin = (len_rd - len(rd1_bin)) * "0" + rd1_bin
                    if (len_rs - len(rs1_bin)) > 0 :
                        rs1_bin = (len_rs - len(rs1_bin)) * "0" + rs1_bin
                    if (len_rt - len(rt1_bin)) > 0:
                        rt1_bin = (len_rt - len(rt1_bin)) * "0" + rt1_bin
                    if (len_rs - len(rs2_bin)) > 0 :
                        rs2_bin = (len_rs - len(rs2_bin)) * "0" + rs2_bin
                    if (len_rt - len(rt2_bin)) > 0:
                        rt2_bin = (len_rt - len(rt2_bin)) * "0" + rt2_bin
                    if immediate_temp >= 0:
                        if (len_immediate - len(immediate_bin) > 0):
                            immediate_bin = (len_immediate - len(immediate_bin)) * "0" + immediate_bin
                    else:
                        if (len_immediate - len(immediate_bin) > 0):
                            immediate_bin = (len_immediate - len(immediate_bin)) * "1" + immediate_bin
 
            # generate full bit
            if _type == "R":
                result.append(opcode + rs_bin + rt_bin + rd_bin + shamt + funct)
            elif _type == "I":
                result.append(opcode + rs_bin + rt_bin + immediate_bin)
            elif _type == "J":
                result.append(opcode + ad_bin)
            elif _type == "P":
                if temp[0] == "la":
                    result.append(opcode1 + rs1_bin + rt1_bin + immediate1_bin)
                    result.append(opcode2 + rs2_bin + rt2_bin + immediate2_bin)
                elif temp[0] == "li":
                    result.append(opcode + rs_bin + rt_bin + immediate_bin)   
                elif temp[0] == "blt" or temp[0] == "bgt" or temp[0] == "ble" or temp[0] == "bge":
                    result.append(opcode1 + rs1_bin + rt1_bin + rd1_bin + shamt + funct)
                    result.append(opcode2 + rs2_bin + rt2_bin + immediate_bin)     
            elif _type == "sys":
                result.append("00000000000000000000000000001100")

    inp.close()
    inp_check_label.close()

    return result

def WriteOutput(result):
    output = open("output.txt", "a")
    for i in range(len(result)):
        output.write(result[i] + "\n")
    output.close()

def main():
    isEmty = DeleleComment()
    if isEmty != True:    
        a = GenerateBinary()
        #print(a)
        print("----------THE END----------")
        if len(a) > 1:
            print("There are " + str(len(a)) + " instructions")
        else:
            print("There is 1 instruction")
        WriteOutput(a)
    else:
        print("There are not any instructions")
    GenerateHex()


if __name__ == "__main__":
    main()