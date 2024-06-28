class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        connection_count = {i: 0 for i in range(n)}
        for road in roads:
            for node in road:
                connection_count[node] += 1
                
        sorted_nodes = sorted(connection_count, key=connection_count.get, reverse=True)
        node_values = {}
        current_value = n
        for node in sorted_nodes:
            node_values[node] = current_value
            current_value -= 1
        
        total = 0
        for road in roads:
            total += node_values[road[0]]
            total += node_values[road[1]]
        return total
s = Solution()
s.maximumImportance(5, [[0,3],[2,4],[1,3]])