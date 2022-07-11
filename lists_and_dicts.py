def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Lautaro", "lastname": "Fleitas"}

    super_list = [
        {"firstname": "Lautaro", "lastname": "Fleitas"},
        {"firstname": "Duham", "lastname": "Fleitas"},
        {"firstname": "Emilse", "lastname": "Lerin"},
        {"firstname": "Agus", "lastname": "Iglesias"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 6.2, 10.85]
    }

    for values in super_list:
        for key, value in values.items():
            print(f"{key}, -, {value}")



if __name__ == "__main__":
    run()
