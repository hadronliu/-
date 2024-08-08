"""
    -*- coding: UTF-8 -*-
    @Date   : 2024/8/9 00:01
    @Author : HadronLiu
    @Email  : hadronliu@gmail.com
"""
from mealpy import PSO, Problem, GA, SMA
from mealpy.utils.space import IntegerVar

"""
问题：给定一个目标字符串，目标是从相同长度的随机字符串开始生成目标字符串。
解决思路：利用遗传算法进行个体基因编码，目标函数为相同字符的个数。
"""


GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.-;:_!"#%&/()=?@${[]}'''

TARGET = "I love Math OPT"


class COP(Problem):
    def __init__(self, bounds=None, minmax=None, GENES=None, TARGET=None, **kwargs):
        self.GENES = GENES
        self.TARGET = TARGET
        super().__init__(bounds, minmax, **kwargs)

    def obj_func(self, solution):

        fitness = 0
        for gs, gt in zip(solution, self.TARGET):
            if self.GENES[int(gs)] != gt:
                fitness += 1
        return fitness


def print_encode(solution):
    res = ""
    for gs in solution:
        res += str(GENES[int(gs)])
    print(res)


# Create an instance of COP class
# 假设 TARGET 和 GENES 已经定义
variable_count = len(TARGET)
bounds = [IntegerVar(lb=0, ub=len(GENES) - 1)] * variable_count
problem_cop = COP(bounds=bounds, GENES=GENES, TARGET=TARGET, minmax="min")


# Define the model and solve the problem
# model = PSO.OriginalPSO(epoch=3000, pop_size=500)
# model.solve(problem=problem_cop)
#
# print(model.g_best.solution)
# print_encode(model.g_best.solution)
# print(model.g_best.target.fitness)

# Define the model and solve the problem
model = GA.BaseGA(epoch=100, pop_size=50, pc=0.85, pm=0.1)
model.solve(problem=problem_cop)

print(model.g_best.solution)
print_encode(model.g_best.solution)
print(model.g_best.target.fitness)
