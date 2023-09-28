import random 

class PopulationSort:
    """"""
    def sort(self, 
             input_list: list[int], 
             bound: int = 0, 
             is_ascending: bool = True, 
             debug: bool = False
             ) -> None:
        """"""

        input_length = len(input_list)

        if bound < 0:
            raise ValueError("INVALID INPUT: The bound for PopulationSort can not be lower than 0")
        
        elif bound != 0 and bound != input_length:
            while bound > input_length:
                input_length += 1
                self.__birth(input_list)
            while bound < input_length:
                input_length -= 1
                self.__death(input_list)
        
        while not self.__is_sorted(input_list, is_ascending):
            self.__birth(input_list)
            self.__death(input_list)


    def __is_sorted(self, input_list: list[int], is_ascending: bool) -> bool:
        """Private method to check whether the list is sorted or not"""
        if is_ascending:
            return all(input_list[i] <= input_list[i+1] for i in range(0, len(input_list) - 1))
        else:
            return all(input_list[i] >= input_list[i+1] for i in range(0, len(input_list) - 1)) 
        
    
    def __birth(self, input_list: list[int]) -> None:
        first_parent = random.randint(0, len(input_list) - 2)
        second_parent = first_parent + 1

        child = (input_list[first_parent] + input_list[second_parent]) // 2

        input_list.insert(random.randint(0, len(input_list)), child)

    def __death(self, input_list: list[int]) -> None:
        dead_person = random.randint(0, len(input_list) - 1)

        input_list.pop(dead_person)
