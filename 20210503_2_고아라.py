#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hi")


# In[2]:


# 예외처리를 하면 있어 보이기 때문에 코딩 테스트를 할 때 굳이 예외처리를 한 번 넣어줘라^^
# 조건문으로 예외처리(if)의 경우 if는 예외처리도 할 수 있는 애. 그러나 try는 예외처리를 위한 애.


# In[3]:


user_input_a = input("정수 입력> ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
    
else:
    print("정수를 입력하지 않았습니다.")


# In[4]:


# 프로그램을 작성할 때는 항상 예외적인 상황까지 모두 생각하는 습관을 기르는 게 좋습니다.


# In[6]:


try:
    
    number_input_a = int(input("정수 입력> "))
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

except:
    print("무언가 잘못되었습니다.")


# In[8]:


list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    
    try:
        float(item)
        list_number.append(item)
    except:
        pass
    
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

# 스파이는 float에서 걸러져서 list에 담기지 못하고 바로 pass 되므로 결과값이 출력되지 않는다.


# In[9]:


try:
    number_input_a = int(input("정수 입력> "))
    
except:
    print("정수를 입력하지 않았습니다.")
    
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)


# In[10]:


try:
    number_input_a = int(input("정수 입력> "))
    
except:
    print("정수를 입력하지 않았습니다.")
    
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)


# In[11]:


# Finally는 언제나 거쳐서 나간다. try > else > finally 또는 try > except > finally

try:
    number_input_a = int(input("정수 입력>"))
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

except:
    print("정수를 입력해달라고 했잖아요?!")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")


# In[12]:


# Finally는 언제나 거쳐서 나간다. 

try:
    number_input_a = int(input("정수 입력>"))
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

except:
    print("정수를 입력해달라고 했잖아요?!")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")


# In[15]:


def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")
    
test()

# return을 만나면 바로 나가게 되지만 finally가 있으면 무조건 finally를 거치고 나가게 된다. 
# try 구문 중간에서 탈출해도 finally 구문은 무조건 실행됩니다.


# In[16]:


print("프로그램이 시작되었습니다.")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while 반복문의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")


# In[17]:


try:
    number_input_a = int(input("정수 입력> "))
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    
    print("type(exception):", type(exception))
    print("exception:", exception)


# In[22]:


list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요!")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")


# In[21]:


list_number = [52, 273, 32, 72, 100]

try:
    number_input= int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요!")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")


# In[24]:


# 예외 구문과 예외 객체

list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)


# In[26]:


list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception), exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)


# In[ ]:


# raise 구문 (중요도는 조금 떨어져) - 에러를 강제로 발생시켜서 확실히 처리하게 하는 방법.

number = input("정수 입력> ")
number = int(number)

if number > 0:
    raise NotimplementedError
else:
    raise NotImplementedError


# In[ ]:




