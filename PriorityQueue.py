from typing import List


class Element:
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return bool(self.priority < other.priority)

    def __gt__(self, other):
        return bool(self.priority > other.priority)

    def __str__(self):
        return str(self.priority) + ": " + str(self.data)


class Queue:
    def __init__(self):
        self.queue: List[Element] = []

    def is_empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False

    def peek(self) -> [float, int, str]:
        return self.queue[0].data

    def enqueue(self, priority, data) -> None:
        child_index = len(self.queue)
        self.queue.append(Element(priority, data))
        while child_index != 0:
            parent_index = int((child_index - 1) / 2)
            if self.queue[child_index] > self.queue[parent_index]:
                cache = self.queue[child_index]
                self.queue[child_index] = self.queue[parent_index]
                self.queue[parent_index] = cache
                child_index = parent_index
            else:
                return

    def dequeue(self) -> [None, str, float, int]:
        if self.is_empty():
            return None
        else:
            self.queue[0], self.queue[1:-2], self.queue[-1] = self.queue[-1], self.queue[1:-2], self.queue[0]
            downloaded = self.queue.pop()
            if len(self.queue) == 0:
                return downloaded.data
            else:
                last_index = len(self.queue) - 1
                parent_index = 0
                while True:
                    if (2 * parent_index) + 1 > last_index:
                        return downloaded.data
                    elif (2 * parent_index) + 2 > last_index:
                        left_child_index = (2 * parent_index) + 1
                        if self.queue[parent_index] < self.queue[left_child_index]:
                            cache = self.queue[left_child_index]
                            self.queue[left_child_index] = self.queue[parent_index]
                            self.queue[parent_index] = cache
                            parent_index = left_child_index
                        else:
                            return downloaded.data
                    else:
                        left_child_index = (2 * parent_index) + 1
                        right_child_index = (2 * parent_index) + 2
                        parent_priority = self.queue[parent_index].priority
                        left_child_priority = self.queue[left_child_index].priority
                        right_child_priority = self.queue[right_child_index].priority
                        if parent_priority < left_child_priority or parent_priority < right_child_priority:
                            if left_child_priority >= right_child_priority:
                                cache = self.queue[left_child_index]
                                self.queue[left_child_index] = self.queue[parent_index]
                                self.queue[parent_index] = cache
                                parent_index = left_child_index
                            else:
                                cache = self.queue[right_child_index]
                                self.queue[right_child_index] = self.queue[parent_index]
                                self.queue[parent_index] = cache
                                parent_index = right_child_index
                        else:
                            return downloaded.data

    def __str__(self):
        if not self.is_empty():
            string = "["
            for element in self.queue:
                string += str(element.priority) + ": " + str(element.data) + ", "
            string = string[:-2] + "]"
            return string
        else:
            return '[]'

    def print_tree(self) -> None:
        print("==============")
        max_index = len(self.queue) - 1
        if max_index:
            self._print_tree(0, 0, max_index)
        print("==============")

    def _print_tree(self, index, lvl, max_index) -> None:
        if index <= max_index:
            self._print_tree((2 * index) + 2, lvl + 10, max_index)

            print()
            for i in range(10, lvl + 10):
                print(end=" ")
            string = str(self.queue[index].priority) + ": " + str(self.queue[index].data)
            print(string)
            self._print_tree((2 * index) + 1, lvl + 10, max_index)


