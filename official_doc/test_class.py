class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'  # Return False
        # class x: #  Return True
        #     check = 12
        assert hasattr(x, "check")
