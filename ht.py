import hello

def test_hello():
    assert hello.hello_world(1) == "Hello World!"
    
def hello_world_n(n):
    return " ".join(["Hello World!"] * n)