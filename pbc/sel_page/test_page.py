from pbc.sel_page.webpage import MainPage


def test_python_org_search(ssh_client, web_driver):

    page = MainPage(web_driver)
    page.open_page().print_screen("python.png")
    assert "Python" in page.get_title()
    page.search_text('pycon')
    page.print_screen("pycon.png")
    assert 'No results found.' not in page.search_result()

