class Solution:
    def average(self, salary: List[int]) -> float:
        # a = max(salary)
        # b = min(salary)
        # return (sum(salary) - a - b)/(len(salary) - 2)

        salary = sorted(salary) # salary = [1000,2000,3000,4000]
        salary_list_without_min_max = salary[1:len(salary)-1] # [2000,3000]
        avg = round(sum(salary_list_without_min_max)/len(salary_list_without_min_max),5) # 2500.00000
        return avg