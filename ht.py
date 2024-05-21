import hello

def test_hello():
    assert hello.hello_world(1) == "Hello World!"
    
def test_Nhello():
    assert hello.hello_world_n(3) == "Hello World! Hello World! Hello World!"