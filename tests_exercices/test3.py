def outer():
    first_num = 10
    def inner():
        first_num = 0
        second_num = 1
        print(f"inner - second_num is: {second_num}")
    inner()
    print(f"outer - first_num is: {first_num}")

outer()