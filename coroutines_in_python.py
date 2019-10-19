# Coroutines in python

def searcher():
        import time
        # some 4 seconds consuming task
        book = "this is a book read with the kuldeep and some other friends"
        time.sleep(4)
        # Coroutines coroutines means start programme between the function
        while True:
                text = (yield)
                if text in book:
                        print("your text is in this book")
                else:
                        print("text is not in this book")                                


search = searcher()
next(search)
search.send("kuldeep")
input("Press any key")
search.send("kuldeep and")