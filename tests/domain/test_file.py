def test_file(file_factory):
    file = file_factory(name="test_file.txt", content="test")
    assert file.name == "test_file.txt"
    assert file.content == "test"
