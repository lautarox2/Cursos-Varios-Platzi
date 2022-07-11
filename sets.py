def remove_dup(ran_list):
    return list(set(ran_list))


def run():
    ran_list = [1, 2, 5 , 4 , 2 , 3, 4]
    print(remove_dup(ran_list))

if __name__ == "__main__":
    run()