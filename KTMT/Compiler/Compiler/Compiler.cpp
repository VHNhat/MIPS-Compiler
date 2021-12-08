#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
//#include <sstream>
//#include <algorithm>
//#include <iterator>

using namespace std;

struct isLabel
{
	string name;
	unsigned long long address;
	int line_num;
};
typedef struct isLabel l;

vector <string> Split(string s, string d) {
	size_t pos = 0;
	vector <string> r;
	string token;
	while ((pos = s.find(d)) != string::npos) {
		token = s.substr(0, pos);
		r.push_back(token);
		s.erase(0, pos + d.length());
	}
	return r;
}

string NumberRegister(string r) {
	if (r == "$zero" || r == "$0") return "00000";
	else if (r == "$at" || r == "$1") return "00001";
	else if (r == "$v0" || r == "$2") return "00010";
	else if (r == "$v1" || r == "$3") return "00011";
	else if (r == "$a0" || r == "$4") return "00100";
	else if (r == "$a1" || r == "$5") return "00101";
	else if (r == "$a2" || r == "$6") return "00110";
	else if (r == "$a3" || r == "$7") return "00111";
	else if (r == "$t0" || r == "$8") return "01000";
	else if (r == "$t1" || r == "$9") return "01001";
	else if (r == "$t2" || r == "$10") return "01010";
	else if (r == "$t3" || r == "$11") return "01011";
	else if (r == "$t4" || r == "$12") return "01100";
	else if (r == "$t5" || r == "$13") return "01101";
	else if (r == "$t6" || r == "$14") return "01110";
	else if (r == "$t7" || r == "$15") return "01111";
	else if (r == "$s0" || r == "$16") return "10000";
	else if (r == "$s1" || r == "$17") return "10001";
	else if (r == "$s2" || r == "$18") return "10010";
	else if (r == "$s3" || r == "$19") return "10011";
	else if (r == "$s4" || r == "$20") return "10100";
	else if (r == "$s5" || r == "$21") return "10101";
	else if (r == "$s6" || r == "$22") return "10110";
	else if (r == "$s7" || r == "$23") return "10111";
	else if (r == "$t8" || r == "$24") return "11000";
	else if (r == "$t9" || r == "$25") return "11001";
	else if (r == "$k0" || r == "$26") return "11010";
	else if (r == "$k1" || r == "$27") return "11011";
	else if (r == "$gp" || r == "$28") return "11100";
	else if (r == "$sp" || r == "$29") return "11101";
	else if (r == "$fp" || r == "$30") return "11110";
	else if (r == "$ra" || r == "$31") return "11111";
}

void DeleteComment() {
	string str;
	bool comma = false, space = false;

	// Clear data
	ofstream emty1("temp.txt", ios::trunc);
	emty1.close();
	ofstream emty2("output.txt", ios::trunc);
	emty2.close();
	ofstream emty3("hex.txt", ios::trunc);
	emty3.close();

	ifstream inp("input.txt");
	ofstream output("temp.txt", ios::app);
	while (getline(inp, str)) {
		if (str == "" || str == "\t" || str == " " || str[0] == '#') continue;
		for (int i = 0; i < str.length(); i++) {
			if (str[i] == '\t') continue;
			if (comma == true) { output << " "; comma = false; }
			else if (str[i] == '#') { output << endl; break; }
			if (str[i] == ',' && str[i + 1] != ' ') comma = true;
			output << str[i];
			if (i == str.length() - 1 && str[i] != ' ') output << " " << endl;
			else if (i == str.length() - 1 && str[i] == ' ') output << endl;
		}
	}
	inp.close();
	output.close();
}

vector <l> StoreLabel() {
	string str;
	vector <l> label;
	unsigned long long address = 4194300;
	int line_num = 0;
	int index = 0, size = 1, pos;
	ifstream inp("temp.txt");
	while (getline(inp, str)) {
		vector <string> temp = Split(str, " ");
		address += 4;
		line_num += 1;
		if (str[str.length() - 2] == ':') {
			pos = str.find(":");
			label.resize(size);
			label[index].address = address;
			label[index].line_num = line_num;
			label[index].name = str.substr(0,pos);
			size += 1;
			index += 1;
		}
		if (temp[0] == "la" || temp[0] == "blt" || temp[0] == "bgt" || temp[0] == "ble" || temp[0] == "bge") {
			line_num += 1;
		}
	}
	inp.close();
	return label;
}

string GetRigister(vector <string> temp, int index, string d) {
	int pos = temp[index].find(d);
	return temp[index].substr(0, pos);
}
string Get_Rigister(vector <string> temp, int index, string d1, string d2) {
	int pos1 = temp[index].find(d1);
	int pos2 = temp[index].find(d2);
	return temp[index].substr(pos1+1, pos2 - pos1 - 1);
}

void GenerateHex() {
	string str;
	string hex[] = { "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111" };
	string result[] = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F" };
	ifstream inp("output.txt");
	ofstream output("hex.txt", ios::app);
	while (getline(inp, str)) {
		output << "0x";
		for (int i = 0; i < 32; i+=4) {
			string temp = str.substr(i, 4);
			for (int j = 0; j < 16; j++) {
				if (temp == hex[j]) {
					output << result[j];
					break;
				}
			}
		}
		output << endl;
	}
	inp.close();
	output.close();
}


void GenerateBinary() {
	string str, _type;
	string opcode, rs, rt, rd, shamt, funct, immediate, ad;

	//pseudo
	string opcode1, opcode2, rd1, rs1, rt1, immediate1, rs2, rt2, immediate2;
	int line_num = 0, lines = 0;
	unsigned long long address = 4194300;
	bool isLabel, check;
	ifstream inp("temp.txt");
	ofstream output("output.txt", ios::app);

	vector <l> label = StoreLabel();
	while (getline(inp, str)) {
		check = false;
		vector <string> temp = Split(str, " ");
		address += 4;
		line_num += 1;
		if (str[str.length() - 2] == ':') isLabel = true;
		else { isLabel = false; }

		if (isLabel == false) {
			cout << str << endl;

			// R-type
			if (temp[0] == "add") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100000";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "addu") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100001";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "sub") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100010";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "subu") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100011";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "and") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100100";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "jr") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "001000";
				rd = "$zero";
				rs = GetRigister(temp, 1, ",");
				rt = "$zero";
			}
			else if (temp[0] == "nor") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100111";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "or") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100101";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "slt") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "101010";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "sltu") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "101011";
				rd = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				rt = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "sll") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = GetRigister(temp, 3, ",");
				funct = "000000";
				rd = GetRigister(temp, 1, ",");
				rs = "$zero";
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "srl") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = GetRigister(temp, 3, ",");
				funct = "000010";
				rd = GetRigister(temp, 1, ",");
				rs = "$zero";
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "div") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "011010";
				rd = "$zero";
				rs = GetRigister(temp, 1, ",");
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "divu") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "011011";
				rd = "$zero";
				rs = GetRigister(temp, 1, ",");
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "mflo") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "010010";
				rd = GetRigister(temp, 1, ",");
				rs = "$zero";
				rt = "$zero";
			}
			else if (temp[0] == "mfhi") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "010000";
				rd = GetRigister(temp, 1, ",");
				rs = "$zero";
				rt = "$zero";
			}
			else if (temp[0] == "mfc0") {
				check = true;
				_type = "R";
				opcode = "010000";
				shamt = "00000";
				funct = "000000";
				rd = GetRigister(temp, 2, ",");
				rs = "$zero";
				rt = GetRigister(temp, 1, ",");
			}
			else if (temp[0] == "mult") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "011000";
				rd = "$zero";
				rs = GetRigister(temp, 1, ",");
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "multu") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "011001";
				rd = "$zero";
				rs = GetRigister(temp, 1, ",");
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "sra") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = GetRigister(temp, 3, ",");
				funct = "000011";
				rd = GetRigister(temp, 1, ",");
				rs = "$zero";
				rt = GetRigister(temp, 2, ",");
			}
			// I-type
			if (temp[0] == "addi") {
				check = true;
				_type = "I";
				opcode = "001000";
				rt = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "addiu") {
				check = true;
				_type = "I";
				opcode = "001001";
				rt = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "andi") {
				check = true;
				_type = "I";
				opcode = "001100";
				rt = GetRigister(temp, 1, ",");
				rs = GetRigister(temp, 2, ",");
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "beq") {
				check = true;
				_type = "I";
				opcode = "000100";
				rs = GetRigister(temp, 1, ",");
				rt = GetRigister(temp, 2, ",");
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "bne") {
				check = true;
				_type = "I";
				opcode = "000101";
				rs = GetRigister(temp, 1, ",");
				rt = GetRigister(temp, 2, ",");
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "lw") {
				check = true;
				_type = "I";
				opcode = "100011";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "lhu") {
				check = true;
				_type = "I";
				opcode = "100101";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "lbu") {
				check = true;
				_type = "I";
				opcode = "100100";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "ll") {
				check = true;
				_type = "I";
				opcode = "110000";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "lui") {
				check = true;
				_type = "I";
				opcode = "001111";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, ",");
				rs = "$zero";
			}
			else if (temp[0] == "ori") {
				check = true;
				_type = "I";
				opcode = "001101";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 3, ",");
				rs = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "slti") {
				check = true;
				_type = "I";
				opcode = "001010";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 3, ",");
				rs = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "sltiu") {
				check = true;
				_type = "I";
				opcode = "001011";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 3, ",");
				rs = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "sw") {
				check = true;
				_type = "I";
				opcode = "101011";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "sb") {
				check = true;
				_type = "I";
				opcode = "101000";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "sc") {
				check = true;
				_type = "I";
				opcode = "111000";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "sh") {
				check = true;
				_type = "I";
				opcode = "101001";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "lwc1") {
				check = true;
				_type = "I";
				opcode = "110001";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "ldc1") {
				check = true;
				_type = "I";
				opcode = "110101";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "swc1") {
				check = true;
				_type = "I";
				opcode = "111001";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}
			else if (temp[0] == "sdc1") {
				check = true;
				_type = "I";
				opcode = "111101";
				rt = GetRigister(temp, 1, ",");
				immediate = GetRigister(temp, 2, "(");
				rs = Get_Rigister(temp, 2, "(", ")");
			}

			// J-type
			if (temp[0] == "j") {
				check = true;
				_type = "J";
				opcode = "000010";
				ad = GetRigister(temp, 1, ",");
			}
			else if (temp[0] == "jal") {
				check = true;
				_type = "J";
				opcode = "000011";
				ad = GetRigister(temp, 1, ",");
			}

			// Pseudo
			if (temp[0] == "li") {
				check = true;
				_type = "I";
				opcode = "001001";
				rt = GetRigister(temp, 1, ",");
				rs = "$zero";
				immediate = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "move") {
				check = true;
				_type = "R";
				opcode = "000000";
				shamt = "00000";
				funct = "100001";
				rd = GetRigister(temp, 1, ",");
				rs = "$0";
				rt = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "la") {
				check = true;
				_type = "P";
				opcode1 = "001111";
				rt1 = "$1";
				rs1 = "$zero";
				immediate1 = "64";
				line_num += 1;
				opcode2 = "001101";
				rt2 = GetRigister(temp, 1, ",");
				rs2 = "$1";
				immediate2 = GetRigister(temp, 2, ",");
			}
			else if (temp[0] == "blt") {
				check = true;
				_type = "P";
				opcode1 = "000000";
				shamt = "00000";
				funct = "101010";
				rd1 = "$1";
				rs1 = GetRigister(temp, 1, ",");
				rt1 = GetRigister(temp, 2, ",");
				line_num += 1;
				opcode2 = "000101";
				rs2 = "$1";
				rt2 = "$0";
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "bgt") {
				check = true;
				_type = "P";
				opcode1 = "000000";
				shamt = "00000";
				funct = "101010";
				rd1 = "$1";
				rs1 = GetRigister(temp, 2, ",");
				rt1 = GetRigister(temp, 1, ",");
				line_num += 1;
				opcode2 = "000101";
				rs2 = "$1";
				rt2 = "$0";
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "ble") {
				check = true;
				_type = "P";
				opcode1 = "000000";
				shamt = "00000";
				funct = "101010";
				rd1 = "$1";
				rs1 = GetRigister(temp, 2, ",");
				rt1 = GetRigister(temp, 1, ",");
				line_num += 1;
				opcode2 = "000100";
				rs2 = "$1";
				rt2 = "$0";
				immediate = GetRigister(temp, 3, ",");
			}
			else if (temp[0] == "bge") {
				check = true;
				_type = "P";
				opcode1 = "000000";
				shamt = "00000";
				funct = "101010";
				rd1 = "$1";
				rs1 = GetRigister(temp, 1, ",");
				rt1 = GetRigister(temp, 2, ",");
				line_num += 1;
				opcode2 = "000100";
				rs2 = "$1";
				rt2 = "$0";
				immediate = GetRigister(temp, 3, ",");
			}
			if (temp[0] == "syscall") {
				check = true;
				_type = "sys";
			}

			if (check == false) {
				cout << "'" << temp[0] << "'" << " is not a recognized operator" << endl;
				cout << "*****EROR*****";
				return;
			}
			// Generate into bit
			if (_type == "R") {
				bitset<5> bit(atoi(shamt.c_str()));
				output << opcode << NumberRegister(rs) << NumberRegister(rt) << NumberRegister(rd) << bit << funct << endl;
				lines++;
			}
			else if (_type == "I") {
				if (temp[0] == "beq" || temp[0] == "bne") {
					for (int i = 0; i < label.size(); i++) {
						if (immediate == label[i].name) { 
							int a = 0;
							for (int j = 0; j < label.size(); j++) {
								if (((label[i].line_num < label[j].line_num) && (label[j].line_num < line_num)) || ((line_num < label[j].line_num) && (label[j].line_num < label[i].line_num))) a += 1;
							}
							int immediate_bit = label[i].line_num - line_num;
							if (immediate_bit >= 0) immediate_bit = immediate_bit - 1 - a;
							else immediate_bit += a;
							bitset<16> bit(immediate_bit);
							output << opcode << NumberRegister(rs) << NumberRegister(rt) << bit << endl;
							lines++;
							break;
						}
					}
				}
				else {
					bitset<16> bit(atoi(immediate.c_str()));
					output << opcode << NumberRegister(rs) << NumberRegister(rt) << bit << endl;
					lines++;
				}
			}
			else if (_type == "J") {
				for (int i = 0; i < label.size(); i++) {
					if (ad == label[i].name) {
						int address_bin = label[i].address;
						bitset<26> bit(address_bin);
						output << opcode << bit << endl;
						lines++;
						break;
					}
				}
			}
			else if (_type == "P") {
				if (temp[0] == "la") {
					for (int i = 0; i < label.size(); i++) {
						if (immediate2 == label[i].name) {
							int immediate_temp;
							if (line_num >= label[i].line_num) {
								immediate_temp = (label[i].line_num - 1) * 4;
							}
							else immediate_temp = label[i].line_num * 4;
							bitset<16> bit1(atoi(immediate1.c_str()));
							bitset<16> bit2(immediate_temp);
							output << opcode1 << NumberRegister(rs1) << NumberRegister(rt1) << bit1 << endl;
							lines++;
							output << opcode2 << NumberRegister(rs2) << NumberRegister(rt2) << bit2 << endl;
							lines++;
							break;
						}
					}
				}
				else if (temp[0] == "blt" || temp[0] == "bgt" || temp[0] == "ble" || temp[0] == "bge") {
					for (int i = 0; i < label.size(); i++) {
						if (immediate == label[i].name) {
							int a = 0;
							for (int j = 0; j < label.size(); j++) {
								if (((label[i].line_num < label[j].line_num) && (label[j].line_num < line_num)) || ((line_num < label[j].line_num) && (label[j].line_num < label[i].line_num))) a += 1;
							}
							int immediate_bit = label[i].line_num - line_num;
							if (immediate_bit >= 0) immediate_bit = immediate_bit - 1 - a;
							else immediate_bit += a;
							bitset<16> bit(immediate_bit);
							output << opcode1 << NumberRegister(rs1) << NumberRegister(rt1) << NumberRegister(rd1) << shamt << funct << endl;
							lines++;
							output << opcode2 << NumberRegister(rs2) << NumberRegister(rt2) << bit << endl;
							lines++;
							break;
						}
					}
				}
			}
			else if (_type == "sys") {
				output << "00000000000000000000000000001100" << endl;
				lines++;
			}
		}
	}
	cout << "----------THE END----------" << endl;
	if (lines > 1) cout << "There are " << lines << " instructions" << endl;
	else if (lines == 1) cout << "There is 1 instruction" << endl;
	else cout << "There are not any instructions" << endl;

	inp.close();
	output.close();
}

int main() {
	DeleteComment();
	GenerateBinary();
	GenerateHex();
	return 0;
}