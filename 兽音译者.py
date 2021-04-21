bd = ['嗷', '呜', '啊', '~']


def str2hex(text: str):
    ret = ""
    for x in text:
        charHexStr = hex(ord(x))[2:]
        if len(charHexStr) == 3:
            charHexStr = "0" + charHexStr
        elif len(charHexStr) == 2:
            charHexStr = "00" + charHexStr
        ret += charHexStr
    return ret


def hex2str(text: str):
    ret = ""
    for i in range(0, len(text), 4):
        unicodeHexStr = text[i:i + 4]
        charStr = chr(int(unicodeHexStr, 16))
        ret += charStr
    return ret


def toBeast(rawStr):
    tfArray = list(str2hex(rawStr))
    beast = ""
    n = 0
    for x in tfArray:
        k = int(x, 16) + n % 16
        if k >= 16:
            k -= 16
        beast += bd[int(k / 4)] + bd[k % 4]
        n += 1
    return "~呜嗷" + beast + "啊"


def fromBeast(decoratedBeastStr):
    beastStr = decoratedBeastStr[3:-1]
    beastCharArr = list(beastStr)
    unicodeHexStr = ""
    for i in range(0, len(beastCharArr), 2):
        pos1 = bd.index(beastCharArr[i])
        pos2 = bd.index(beastCharArr[i + 1])
        k = ((pos1 * 4) + pos2) - (int(i / 2) % 16)
        if k < 0:
            k += 16
        unicodeHexStr += hex(k)[2:]
    return hex2str(unicodeHexStr)


if __name__ == '__main__':
    print(toBeast("https://www.baidu.com"))
    print(
        fromBeast(
            "~呜嗷嗷嗷嗷呜啊嗷啊~呜嗷呜呜~呜啊~啊嗷啊呜嗷呜~~~嗷~呜呜呜~~嗷嗷嗷呜啊呜呜啊呜嗷呜呜啊呜嗷呜啊嗷啊呜~嗷啊啊~嗷~呜嗷嗷~啊嗷嗷嗷呜啊呜啊啊呜嗷呜呜~呜~啊啊嗷啊呜嗷呜嗷啊~嗷~呜嗷嗷~呜嗷嗷嗷呜啊嗷呜呜呜嗷呜呜~嗷啊嗷啊嗷啊呜嗷嗷呜嗷~嗷~呜呜嗷嗷~嗷嗷嗷呜啊呜啊嗷呜嗷呜呜啊嗷呜呜啊嗷啊呜嗷嗷~啊~嗷~呜呜嗷~啊嗷嗷嗷呜啊嗷嗷嗷啊"
        ))
