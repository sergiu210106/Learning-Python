'''
Get a string of paranthesis and check if it is valid
'''

def validate_paranthesis(input : str):
    paranthesis_dict  = {'(' : 1, ')' : -1, '[' : 2, ']' : -2, '{' : 3, '}' : -3}
    
    stack = []
    for character in input:
        if paranthesis_dict[character] < 0:
            if stack and paranthesis_dict[stack[-1]] + paranthesis_dict[character] == 0:
                stack.pop()
            else: 
                return False 
            
        else: 
            stack.append(character)
    return True if not stack else False


if __name__ == '__main__':
    test_cases = [
        ("", True),
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("()[]{}", True),
        ("({[]})", True),
        ("({})", True),
        ("((()))", True),
        ("({[]})", True),
        ("([)]", False),
        ("(", False),
        (")", False),
        ("(]", False),
        ("[)", False),
        ("({[}]", False),
        ("({[)", False),
        ("((()", False),
        ("()))", False),
        ("{[()]}", True),
        ("{[(])}", False),
        ("((((", False),
        ("))))", False),
        ("{", False),
        ("}", False),
        ("[", False),
        ("]", False),
        ("({})", True),
        ("({)}", False),
        ("([])", True),
        ("[()]", True),
        ("{()}", True),
        ("{[()()]}", True),
        ("{[()()]}}", False),
        ("{{[[(())]]}}", True),
        ("{{[[(())]]}]}", False),
        ("((([])))", True),
        ("((([])])", False),
        ("(()", False),
        (")(", False),
    ]
    
    for input_str, expected in test_cases:
        result = validate_paranthesis(input_str)
        if result == expected:
            print(f"PASS: '{input_str}' -> {expected}")
        else:
            print(f"FAIL: '{input_str}' -> Expected {expected}, got {result}")