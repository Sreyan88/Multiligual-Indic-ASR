
# https://github.com/sutariyaraj/indic-num2words
from num_to_word import num_to_word as ntw


def wrd_div(num):
    c = 0
    for x in num:
        if not x.isnumeric():
            break
        c += 1
    return num[:c], num[c:]

def get_iword(num):
    if num == '½':
        return 'आधा'
    elif num == '1½':
        return 'डेढ़'

    res = ""
    dig,suff = wrd_div(num)
    if len(dig)==4 and num[0] == "1":
        ps = get_iword(num[:2])
        pl = get_iword(num[2:])
        res = ps + " सौ " + pl
    else:     
        res = ntw(dig, lang='hi')
        if suff:
            try:
                lsb2 = int(dig[-2])
            except:
                lsb2 = 0
            lsb = int(dig[-1])

            if lsb == 0:
                res = res + suff
            elif lsb2 == 9 and lsb>0:
                res = res[:-2] + suff       # तिरानवे - वे + वाँ 
            elif lsb2 == 1 and lsb>0 and lsb<9:
                res = res[:-1] + suff      # बाााारह - ह + वाँ 
            elif int(dig) <10:
                matra = -1
                if suff[-1] == "ं":
                    matra = -2
                if dig == '1':
                    res = "पहल" + suff[matra:]
                elif dig == '2':
                    res = "दूसर" + suff[matra:]
                elif dig == '3':
                    res == "तीसर" + suff[matra:]
                elif dig == '4':
                    res = "चौथ" + suff[matra:] 
                elif dig == '5':
                    res = "पाँचव" + suff[matra:]
                elif dig == '6':
                    res = "छठ" + suff[matra:]
                elif dig == '7':
                    res = "सातव" + suff[matra:]
                elif dig == '8':
                    res = "आठव" + suff[matra:]
                elif dig == '9':
                    res = "नौव" + suff[matra:]
    return res

if __name__ == "__main__":
    print(get_iword("1989")) # उन्नीस सौ नवासी
    print(get_iword("95वें")) # पचानवें
    print(get_iword("95वे")) # पचानवे
    print(get_iword("4थी")) # चौथी
    print(get_iword("4थीं")) # चौथीं
    print(get_iword("1वी")) # पहली
    print(get_iword("1वीं")) # पहलीं
    print(get_iword("6ठी")) # छठी
    print(get_iword("100")) # एक सौ
    print(get_iword("1947")) # उन्नीस सौ सैंतालीस
    print(get_iword("13वी"))









