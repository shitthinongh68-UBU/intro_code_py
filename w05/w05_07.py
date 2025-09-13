name = str(input())
name_lenght = len(name)

print(f"""
    {name[0]}
    {(name_lenght - 2) * "*"}
    {name[name_lenght - 1]}
    """
    )
