"""
迭代器的使用
"""

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.index = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """
        如果想要一个对象称为一个可以迭代的对象，
        即可以使用for，那么必须要实现__iter__方法
        """
        return self

    def __next__(self):
        """
        迭代器取值的方法，判断取出下一个值，如果每值了要抛出StopIteration
        """
        if self.index < len(self.names):
            name = self.names[self.index]
            self.index += 1
            return name
        else:
            # 迭代器结束要抛出StopIteration
            raise StopIteration("None value.")


def main():
    classmate = Classmate()
    classmate.add("张三")
    classmate.add("李四")
    classmate.add("王五")

    for name in classmate:
        print(name)


if __name__ == "__main__":
    main()
