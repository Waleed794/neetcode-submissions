class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict_count = {}
        # for element in nums:
        #     if element not in dict_count:
        #         dict_count[element]=1
        #     else:
        #         dict_count[element]+=1
        # top_k = []
        # for i in range(k):
        #     current_max = -1000
        #     for j in dict_count.keys():
        #         if dict_count[j]>=current_max:
        #             current_max = dict_count[j] #dict_count[j]
        #             max_key = j
        #     top_k.append(max_key)
        #     dict_count.pop(max_key)
        # return top_k









        dict_numCount = {}
        results = []
        #nums_sorted() = nums.sort()
        for i,element in enumerate(nums):
            # count=0
            if element not in dict_numCount:
                dict_numCount[element]=1
            else:
                dict_numCount[element]+=1
                
        for j in range(k):
            current_max = -1000
            for k in dict_numCount.keys():
                if dict_numCount[k]>current_max:
                    current_max = dict_numCount[k]
                    max_key = k
            results.append(max_key)
            dict_numCount.pop(max_key)
        return results
                
            