def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import altair as alt" in __solution__, "¿Estás importando `altair` como `alt`?"
    assert source==data.us_employment(), "¿Estas asignado data.us_unemployment() a source?"

    __msg__.good("¡Muy bien!")
