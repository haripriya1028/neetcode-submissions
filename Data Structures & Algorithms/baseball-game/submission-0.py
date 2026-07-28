class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        # for i, c in enumerate(operations):
        #     if c=='+':
        #         record[i]=record[i-1]+record[i-2]
        #     elif c=='D':
        #         record[i]=record[i-1]*2
        #     elif c=='C':
        #         record.pop(i-1)
        #     else:
        #         record.append(operations[i])
        # sum_r=0
        # for n in record:
        #     sum_r+=n
        # return sum_r
        for c in operations:
            if c=='D':
                record.append(record[-1]*2)
            elif c=='+':
                record.append(record[-1]+record[-2])
            elif c=='C':
                record.pop()
            else:
                record.append(int(c))
        return sum(record)

    