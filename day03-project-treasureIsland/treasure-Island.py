print('''
=========================================================================
.                                                            ,
  |`.                                                        ,'|
  \_`-._                                                  _,-'_/
 ./ \-._`-._                                          _,-'_,-/ \,
 \._/._ `._>`-.__                                __,-'<_,' _,\_,/
 /_ \_.`-._\_-._ `--__                      __--' _,-_/_,-',_/ _\
  /._`\_./ _`_./`.-._ `-.                ,-' _,-,'\,_'_ \,_/'_,\
   \._`/ _/ _`_./  _/`\_ `.            ,' _/'\_  \,_'_ \_ \'_,/
    /._`/ _/ _`_./` _/ `\_ `\_      _/' _/' \_ '\,_'_ \_ \'_,\
     \._`/ _/ _`_./` __/  >.  `-.,-'  ,<  \__ '\,_'_ \_ \'_,/
       /_`/._/._`_./` __.`.-\_.-`'-._/-,',__ '\,_'_,\_,\'_\
             `\._`_./`\._/_/'    _   `\_\_,/'\,_'_,/'
                                /_\
                                \./
                              __/(__
                             / `--' \
                            / _    _ \
                            \'|    |`/
                             \|____|/
                             \/ -] \/
                             /   |  \
                             |   |  |
                             |   |   \
                            /    |    \
                            \__,-`\___/
                            (_)     |__)             mic


==================================================================
''')

print("Welcome to the fighting world?")
print("Fighter Mic will consist you to find the best fruit!!")

favorite_fruit = input("What is your favorite fruit?")
if favorite_fruit == "banana":
    print("Great! fighrer Mic likes it too. He can assit you!")
    want_help = input("do you want Mic help u？ Y/N")
    if want_help == "Y":
        print("Of counrse, you made the most brilline idea.")
        print(f".........Mic is trying hard to find {favorite_fruit}")
        print(f"He made it! he find {favorite_fruit}")
        want_thank = input("do you want to thank Mic for his effors? Y/N")
        if want_thank == "Y":
            print("Thank u! fighter Mic")
            print("sending message.......")
            print("he said, he's very glad")
        else:
            print(
                "of course. you can enjoy your fruit. Mic is still very happy")
    else:
        print("of course. you can find it on your own!")
else:
    print(
        f"such a pity! Fighter Mic can not assit u to find {favorite_fruit}, beacause he hates it!!!")
