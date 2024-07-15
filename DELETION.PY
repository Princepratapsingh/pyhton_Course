def deletion(name,phonebook):
    if name in phonebook:
        del phonebook[name]
        print(f"deleted key:{name}")
    else:
        print(f"{name}not found in phonebook")

phonebook={
    "Prince":9719521559,
    "SHYAM":554516512,
    "SHWETA":7668462044
}
NAME=input("Enter the name of the Person you want to delete :")
deletion("NAME",phonebook)


print(phonebook)