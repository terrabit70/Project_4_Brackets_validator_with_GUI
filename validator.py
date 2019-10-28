#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Validator:
    def __init__(self, text_to_validate: str = '', brackets: str = ''):
        self.text_to_validate = text_to_validate
        self.opened_brackets = ''
        self.closed_brackets = ''
        for i in range(len(brackets)):
            if i % 2 == 0:
                self.opened_brackets += brackets[i]
            else:
                self. closed_brackets += brackets[i]


    def validate(self) -> str:
        result = []
        for line in self.text_to_validate.split('\n'):
            is_valid = self._is_valid(line)
            is_valid_str = " is_valid" if is_valid else " is_not_valid" # Если is_valid = True, то is_valid_str = "is_valid", иначе is_valid_str = "is_not_valid"
            result.append(f'{line} {is_valid_str}')# 'python f string' загуглить
        return '\n'.join(result)

    def _is_valid(self, line) -> bool:
        stack = []
        if len(line) == 1:
            return False
        for symbol in line:
            if symbol in self.opened_brackets:
                stack.append(symbol)
            if symbol in self.closed_brackets:
                if len(stack) == 0 or self.opened_brackets.find(stack[len(stack)-1]) != self.closed_brackets.find(symbol):
                    return False
                else:
                    stack.pop()
        if stack == []:
            return True
        else:
            return False


