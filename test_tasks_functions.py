from tasks import factorial
import allure


@allure.title("Factorial of 3 equal 6")
@allure.tag("tasks")
@allure.severity(allure.severity_level.CRITICAL)
def test_factorial():
    print("Hello!")

    with allure.step("Говорит привет"):
        print("Hello!")
    with allure.step("Проверяем, что факториал 3 равен 6"):
        assert factorial(3) == 6, "smth going wrong"
        
