#!/usr/bin/python3

from testflows.core import *


@TestScenario
def not_hello(self):
    with Given("Not Hello"):
        assert("hello" == "world")


@TestScenario
def hello(self):
    with Given("Hello"):
        for i in range(3):
            assert("hello" !=  "world");

@TestModule
def regression(self):
    Scenario(run=not_hello)
    Scenario(run=hello)
    Scenario(run=not_hello)


def main():
   regression()


if __name__ == '__main__':
    main()


