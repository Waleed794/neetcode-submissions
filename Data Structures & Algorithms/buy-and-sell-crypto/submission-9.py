class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        # right = len(prices)-1
        buy_price = 1000
        sell_price = 0
        max_profit = 0
        min_price_index = 0
        while left<len(prices)-1:
            right = len(prices)-1
            if prices[left]<buy_price:
                buy_price = prices[left]
            while left<right:
                sell_price = prices[right]
                temp_profit = sell_price - buy_price
                if temp_profit > max_profit:
                    max_profit = temp_profit
                right-=1
            left+=1
            
        return max_profit

        # for i,price in enumerate (prices):
        #     # if i == len(prices)-1:
        #     #     break
        #     if price < buy_price and i!= len(prices)-1:
        #         min_price_index=i
        #         buy_price = price
        
        # for j in range(len(prices)-1,min_price_index,-1):
        #     sell_price = prices[j]
        #     temp_profit = sell_price - buy_price
        #     if temp_profit > max_profit:
        #         max_profit = temp_profit
        # return max_profit