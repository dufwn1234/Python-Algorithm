def solution(phone_book):
    if len(phone_book)==1:
        return True
    else:
        phone_book.sort()
        # print(phone_book)
        count=0
        for i in range(len(phone_book)-1):
            if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
                count+=1
                break

        if count>0:
            return False
        else:
            return True