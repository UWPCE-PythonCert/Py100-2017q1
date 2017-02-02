def rot13(str, offset=13):
    newstring=""
    for letter in str:
        numberRep=ord(letter)
        if(ord("a")<=numberRep<=ord("z")):
            newstring+=getValue(numberRep,ord("z"), offset)
        elif(ord("A")<=numberRep<=ord("Z")):
            newstring+=getValue(numberRep,ord("Z"), offset)
        else:
            newstring+=letter
    return newstring

def getValue(numberRep, higher, offset):
    newValue=numberRep+offset
    if (newValue>higher):
        newValue=newValue-26
    return chr(newValue)

if __name__ == '__main__':
    assert rot13("A sample test string.") == "N fnzcyr grfg fgevat."
    assert rot13("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner"
    assert getValue(ord("A"),ord("Z"),13) == "N"
    try:
        assert getValue(ord(" "),ord("Z"),13) == " " #Should fail, we don't pass non-letters to this function
    except AssertionError:
        print("Caught our last Assertion Error")