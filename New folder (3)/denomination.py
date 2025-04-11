def no_of_notes(a):
    Q = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    x = 0
    for i in range(10):
        q = Q[i]
        x = a//q
        print("Notes of {} = {}".format(q, x))
        a = a%q
amount = int(input("Enter Total Amount"))
no_of_notes(amount)